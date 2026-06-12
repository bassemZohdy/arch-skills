# Sync skills from workspace to Codex
# Run this after making changes to skills

$source = "C:\Users\Bassem\Code\arch-skills\skills"
$destination = "C:\Users\Bassem\.codex\skills"

Write-Host "Syncing skills..." -ForegroundColor Cyan

# Core Architecture
Copy-Item -Path "$source\arch-doc" -Destination "$destination\arch-doc" -Recurse -Force
Copy-Item -Path "$source\arch-review" -Destination "$destination\arch-review" -Recurse -Force
Copy-Item -Path "$source\arch-fitness" -Destination "$destination\arch-fitness" -Recurse -Force
Copy-Item -Path "$source\arch-decision" -Destination "$destination\arch-decision" -Recurse -Force
Copy-Item -Path "$source\arch-governance" -Destination "$destination\arch-governance" -Recurse -Force

# Technical Architecture
Copy-Item -Path "$source\arch-security" -Destination "$destination\arch-security" -Recurse -Force
Copy-Item -Path "$source\arch-perf" -Destination "$destination\arch-perf" -Recurse -Force
Copy-Item -Path "$source\arch-resilience" -Destination "$destination\arch-resilience" -Recurse -Force
Copy-Item -Path "$source\arch-test" -Destination "$destination\arch-test" -Recurse -Force

# System Architecture
Copy-Item -Path "$source\arch-api" -Destination "$destination\arch-api" -Recurse -Force
Copy-Item -Path "$source\arch-cloud" -Destination "$destination\arch-cloud" -Recurse -Force
Copy-Item -Path "$source\arch-event" -Destination "$destination\arch-event" -Recurse -Force
Copy-Item -Path "$source\arch-ddd" -Destination "$destination\arch-ddd" -Recurse -Force
Copy-Item -Path "$source\arch-data" -Destination "$destination\arch-data" -Recurse -Force
Copy-Item -Path "$source\arch-metrics" -Destination "$destination\arch-metrics" -Recurse -Force
Copy-Item -Path "$source\arch-integration" -Destination "$destination\arch-integration" -Recurse -Force
Copy-Item -Path "$source\arch-microservices" -Destination "$destination\arch-microservices" -Recurse -Force
Copy-Item -Path "$source\arch-patterns" -Destination "$destination\arch-patterns" -Recurse -Force
Copy-Item -Path "$source\arch-refactoring" -Destination "$destination\arch-refactoring" -Recurse -Force

# Frontend
Copy-Item -Path "$source\arch-frontend" -Destination "$destination\arch-frontend" -Recurse -Force

# Operations
Copy-Item -Path "$source\arch-observability" -Destination "$destination\arch-observability" -Recurse -Force
Copy-Item -Path "$source\arch-migration" -Destination "$destination\arch-migration" -Recurse -Force
Copy-Item -Path "$source\arch-deployment" -Destination "$destination\arch-deployment" -Recurse -Force
Copy-Item -Path "$source\arch-devops" -Destination "$destination\arch-devops" -Recurse -Force
Copy-Item -Path "$source\arch-cost" -Destination "$destination\arch-cost" -Recurse -Force

# Feature Management
Copy-Item -Path "$source\arch-features" -Destination "$destination\arch-features" -Recurse -Force

# NFR
Copy-Item -Path "$source\arch-usability" -Destination "$destination\arch-usability" -Recurse -Force
Copy-Item -Path "$source\arch-accessibility" -Destination "$destination\arch-accessibility" -Recurse -Force
Copy-Item -Path "$source\arch-compliance" -Destination "$destination\arch-compliance" -Recurse -Force

Write-Host "Done! Skills synced:" -ForegroundColor Green
Get-ChildItem -Path $destination -Directory | Where-Object { $_.Name -like "arch-*" } | ForEach-Object {
    Write-Host "  - $($_.Name)" -ForegroundColor Yellow
}
