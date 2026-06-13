# Run validation tests for all skills

Write-Host "============================================" -ForegroundColor Cyan
Write-Host "Architecture Skills Test Suite"
Write-Host "============================================" -ForegroundColor Cyan
Write-Host ""

python "$PSScriptRoot\tests\test_skills.py"

Write-Host ""
Write-Host "============================================" -ForegroundColor Cyan
Write-Host "All tests completed!" -ForegroundColor Green
Write-Host "============================================" -ForegroundColor Cyan
