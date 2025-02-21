# Usage: powershell -ExecutionPolicy Bypass -File xxx.ps1

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location -Path $scriptDir

# Make sure you have run third_party/setup_toolchain.ps once to install python,
# nuitka and other dependencies.
# Optional options:
#    --windows-console-mode=disable  # Disable console window.
python3.12 -m nuitka `
    --enable-plugin=tk-inter `
    --onefile `
    --standalone `
    ..\..\tabio\main.py
