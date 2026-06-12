# Run validation tests for all skills
# Usage: .\run-tests.ps1 [-DarOnly]

param(
    [switch]$DarOnly
)

Write-Host "============================================" -ForegroundColor Cyan
Write-Host "Architecture Skills Test Suite"
Write-Host "============================================" -ForegroundColor Cyan
Write-Host ""

if ($DarOnly) {
    # Only run DAR validation
    Write-Host "Running DAR math validation..." -ForegroundColor Yellow
    $testDarPath = Join-Path $PSScriptRoot "tests\test-dar.md"
    $validateScript = Join-Path $PSScriptRoot "skills\arch-decision\scripts\validate_math.py"
    
    if (Test-Path $testDarPath) {
        python $validateScript $testDarPath
    } else {
        Write-Host "No test-dar.md found, skipping." -ForegroundColor Yellow
    }
} else {
    # Run all tests
    Write-Host "Running structural validation tests..." -ForegroundColor Yellow
    $testScript = Join-Path $PSScriptRoot "tests\test_skills.py"
    python $testScript

    Write-Host ""
    Write-Host "Running DAR math validation..." -ForegroundColor Yellow
    $testDarPath = Join-Path $PSScriptRoot "tests\test-dar.md"
    $validateScript = Join-Path $PSScriptRoot "skills\arch-decision\scripts\validate_math.py"
    
    if (Test-Path $testDarPath) {
        python $validateScript $testDarPath
    } else {
        Write-Host "No test-dar.md found, skipping." -ForegroundColor Yellow
    }
}

Write-Host ""
Write-Host "============================================" -ForegroundColor Cyan
Write-Host "All tests completed!" -ForegroundColor Green
Write-Host "============================================" -ForegroundColor Cyan
