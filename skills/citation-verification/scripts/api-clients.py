#!/usr/bin/env python3
"""Minimal API clients for economics citation verification."""

from __future__ import annotations

import time
from dataclasses import dataclass
from typing import Dict, List, Optional

import requests


@dataclass
class CitationMatch:
    title: str
    authors: List[str]
    year: Optional[int]
    venue: str
    doi: str
    source: str
    url: str


class RateLimiter:
    def __init__(self, calls_per_minute: int) -> None:
        self.min_interval = 60.0 / calls_per_minute
        self.last_call = 0.0

    def wait(self) -> None:
        elapsed = time.time() - self.last_call
        if elapsed < self.min_interval:
            time.sleep(self.min_interval - elapsed)
        self.last_call = time.time()


class CrossrefClient:
    def __init__(self, calls_per_minute: int = 40) -> None:
        self.base_url = "https://api.crossref.org/works"
        self.rate_limiter = RateLimiter(calls_per_minute)

    def search_by_doi(self, doi: str) -> Optional[CitationMatch]:
        self.rate_limiter.wait()
        response = requests.get(f"{self.base_url}/{doi}", timeout=15)
        if response.status_code != 200:
            return None
        payload = response.json().get("message", {})
        return self._normalize(payload, source="crossref")

    def search_by_title(self, title: str) -> Optional[CitationMatch]:
        self.rate_limiter.wait()
        response = requests.get(self.base_url, params={"query.title": title, "rows": 1}, timeout=15)
        if response.status_code != 200:
            return None
        items = response.json().get("message", {}).get("items", [])
        if not items:
            return None
        return self._normalize(items[0], source="crossref")

    @staticmethod
    def _normalize(payload: Dict, source: str) -> CitationMatch:
        authors = []
        for author in payload.get("author", []):
            given = author.get("given", "").strip()
            family = author.get("family", "").strip()
            full = " ".join(part for part in (given, family) if part)
            if full:
                authors.append(full)

        year = None
        date_parts = payload.get("published-print", payload.get("published-online", payload.get("created", {}))).get("date-parts", [[]])
        if date_parts and date_parts[0]:
            year = int(date_parts[0][0])

        return CitationMatch(
            title=(payload.get("title") or [""])[0],
            authors=authors,
            year=year,
            venue=(payload.get("container-title") or [""])[0],
            doi=payload.get("DOI", ""),
            source=source,
            url=payload.get("URL", ""),
        )


class OpenAlexClient:
    def __init__(self, calls_per_minute: int = 20) -> None:
        self.base_url = "https://api.openalex.org/works"
        self.rate_limiter = RateLimiter(calls_per_minute)

    def search_by_title(self, title: str) -> Optional[CitationMatch]:
        self.rate_limiter.wait()
        response = requests.get(self.base_url, params={"search": title, "per-page": 1}, timeout=15)
        if response.status_code != 200:
            return None
        results = response.json().get("results", [])
        if not results:
            return None
        payload = results[0]
        authors = [author.get("author", {}).get("display_name", "") for author in payload.get("authorships", [])]
        venue = payload.get("primary_location", {}).get("source", {}).get("display_name", "")
        doi = payload.get("doi", "") or ""
        return CitationMatch(
            title=payload.get("title", ""),
            authors=[author for author in authors if author],
            year=payload.get("publication_year"),
            venue=venue,
            doi=doi.replace("https://doi.org/", ""),
            source="openalex",
            url=payload.get("id", ""),
        )


class CitationAPIManager:
    def __init__(self) -> None:
        self.crossref = CrossrefClient()
        self.openalex = OpenAlexClient()

    def verify(self, doi: Optional[str] = None, title: Optional[str] = None) -> Optional[CitationMatch]:
        if doi:
            match = self.crossref.search_by_doi(doi)
            if match:
                return match
        if title:
            match = self.crossref.search_by_title(title)
            if match:
                return match
            return self.openalex.search_by_title(title)
        return None
