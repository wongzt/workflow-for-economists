param(
    [Parameter(Mandatory = $true)]
    [string]$Keyword,

    [string]$BaseDir = "D:\Desktop\科研相关",

    [string]$WorkflowRepo = "D:\Desktop\科研相关\workflow-for-economists",

    [switch]$InitGit
)

$ErrorActionPreference = "Stop"

$stamp = Get-Date -Format "yyyyMM"
$projectName = "$stamp$Keyword"
$target = Join-Path $BaseDir $projectName
$template = Join-Path $WorkflowRepo "templates\private-study-skeleton"

if (-not (Test-Path $template)) {
    throw "Private study skeleton not found: $template"
}

if (Test-Path $target) {
    throw "Target project already exists: $target"
}

New-Item -ItemType Directory -Path $target | Out-Null
Copy-Item -Path (Join-Path $template "*") -Destination $target -Recurse -Force

$textFiles = Get-ChildItem -Path $target -Recurse -File |
    Where-Object { $_.Extension -in @(".md", ".txt", ".yaml", ".yml", ".ps1") -or $_.Name -eq ".gitignore" }

foreach ($file in $textFiles) {
    $content = Get-Content -Path $file.FullName -Raw -Encoding UTF8
    $content = $content.Replace("{{PROJECT_NAME}}", $projectName)
    $content = $content.Replace("{{WORKFLOW_REPO_PATH}}", $WorkflowRepo)
    Set-Content -Path $file.FullName -Value $content -Encoding UTF8
}

if ($InitGit) {
    git -C $target init
    git -C $target add .
    git -C $target commit -m "Initialize private research workspace"
}

Write-Host "Created private research workspace:"
Write-Host $target
Write-Host ""
Write-Host "Next step:"
Write-Host "  cd `"$target`""
Write-Host "  codex"
