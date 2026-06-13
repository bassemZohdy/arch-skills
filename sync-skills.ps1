# Sync skills from workspace to Codex
# Run this after making changes to skills

$source = "C:\Users\Bassem\Code\arch-skills\skills"
$destination = "C:\Users\Bassem\.codex\skills"

Write-Host "Syncing skills..." -ForegroundColor Cyan

Copy-Item -Path "$source\*" -Destination "$destination" -Recurse -Force

Write-Host "Done! Skills synced:" -ForegroundColor Green
Get-ChildItem -Path $destination -Directory | Where-Object { $_.Name -like "arch-*" } | ForEach-Object {
    Write-Host "  - $($_.Name)" -ForegroundColor Yellow
}
