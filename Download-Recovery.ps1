<#
.SYNOPSIS
    macOS Recovery Downloader & Direct USB Provisioner
    Part of Dell Inspiron 14 5410 2-in-1 OpenCore Project
#>

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Definition
Set-Location $ScriptDir

Write-Host "==============================================================" -ForegroundColor Cyan
Write-Host "      macOS Official Recovery Image Downloader (PowerShell)    " -ForegroundColor Green
Write-Host "==============================================================" -ForegroundColor Cyan
Write-Host ""

# Check python
$pythonCmd = Get-Command python -ErrorAction SilentlyContinue
if (-not $pythonCmd) {
    Write-Host "[ERROR] Python was not found in PATH." -ForegroundColor Red
    Write-Host "Please install Python or run: winget install Python.Python.3.11" -ForegroundColor Yellow
    exit 1
}

# Run python engine
& python "$ScriptDir\download_recovery.py"
