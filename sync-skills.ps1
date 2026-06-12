# Sync skills from workspace to Codex
# Run this after making changes to skills

$source = "C:\Users\Bassem\Code\arch-skills\skills"
$destination = "C:\Users\Bassem\.codex\skills"

Write-Host "Syncing skills..." -ForegroundColor Cyan

Copy-Item -Path "$source\arch-doc" -Destination "$destination\arch-doc" -Recurse -Force
Copy-Item -Path "$source\arch-review" -Destination "$destination\arch-review" -Recurse -Force
Copy-Item -Path "$source\arch-fitness" -Destination "$destination\arch-fitness" -Recurse -Force
Copy-Item -Path "$source\arch-decision" -Destination "$destination\arch-decision" -Recurse -Force

Write-Host "Done! Skills synced:" -ForegroundColor Green
Get-ChildItem -Path $destination -Directory | Where-Object { $_.Name -like "arch-*" } | ForEach-Object {
    Write-Host "  - $($_.Name)" -ForegroundColor Yellow
}
