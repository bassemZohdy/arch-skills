# Run the offline release checks from any working directory.
$ErrorActionPreference = 'Stop'

Push-Location -LiteralPath $PSScriptRoot
try {
    python tests/test_skills.py
    if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

    python -m unittest discover -s tests -p 'test_*.py'
    if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

    python tests/test_activation.py
    if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

    Write-Host 'All offline checks passed.' -ForegroundColor Green
}
finally {
    Pop-Location
}
