#!/usr/bin/env python3
"""Verify BibTeX entries against DOI-first metadata sources."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from difflib import SequenceMatcher
from pathlib import Path
from typing import Dict, List, Optional

import bibtexparser
from bibtexparser.bparser import BibTexParser

from api-clients import CitationAPIManager


@dataclass
class VerificationResult:
    citation_key: str
    status: str
    match_score: float
    source: Optional[str]
    message: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Verify economics BibTeX entries against DOI-first metadata sources.")
    parser.add_argument("bibfile", help="Path to the BibTeX file")
    parser.add_argument("--threshold", type=float, default=0.85, help="Minimum title match score")
    parser.add_argument("--output", help="Optional JSON output path")
    return parser.parse_args()


def load_entries(path: str) -> List[Dict]:
    with open(path, "r", encoding="utf-8") as handle:
        parser = BibTexParser(common_strings=True)
        return bibtexparser.load(handle, parser).entries


def clean_title(title: str) -> str:
    title = re.sub(r"[{}]", "", title or "")
    title = re.sub(r"\s+", " ", title).strip().lower()
    return title


def similarity(left: str, right: str) -> float:
    return SequenceMatcher(None, clean_title(left), clean_title(right)).ratio()


def verify_entry(entry: Dict, manager: CitationAPIManager, threshold: float) -> VerificationResult:
    citation_key = entry.get("ID", "<missing-key>")
    title = entry.get("title", "")
    doi = entry.get("doi", "")

    if not title:
        return VerificationResult(citation_key, "failed", 0.0, None, "Missing title field")

    match = manager.verify(doi=doi, title=title)
    if not match:
        return VerificationResult(citation_key, "not_found", 0.0, None, "No metadata match found")

    score = similarity(title, match.title)
    if score >= threshold:
        return VerificationResult(citation_key, "verified", score, match.source, f"Matched {match.source}")
    if score >= 0.65:
        return VerificationResult(citation_key, "partial_match", score, match.source, "Title is close but should be checked manually")
    return VerificationResult(citation_key, "low_match", score, match.source, "Possible metadata mismatch")


def main() -> int:
    args = parse_args()
    entries = load_entries(args.bibfile)
    manager = CitationAPIManager()
    results = [verify_entry(entry, manager, args.threshold) for entry in entries]

    for result in results:
        print(f"{result.citation_key}: {result.status} ({result.match_score:.2f}) - {result.message}")

    if args.output:
        payload = [asdict(result) for result in results]
        Path(args.output).write_text(json.dumps(payload, indent=2), encoding="utf-8")

    return 0


if __name__ == "__main__":
    sys.exit(main())
