@echo off
title macOS Recovery Downloader
cd /d "%~dp0"
echo ==============================================================
echo       macOS Official Recovery Image Downloader Launcher
echo ==============================================================
echo.

where python >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Python was not found in your system PATH!
    echo Please install Python 3.8 or newer from https://www.python.org/
    echo or via Windows Terminal: winget install Python.Python.3.11
    echo.
    pause
    exit /b 1
)

python download_recovery.py
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo An error occurred during download.
    pause
    exit /b %ERRORLEVEL%
)

echo.
pause
