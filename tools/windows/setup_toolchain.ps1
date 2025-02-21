# Usage: powershell -ExecutionPolicy Bypass -File xxx.ps1

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location -Path $scriptDir

# Make sure you have chocolatey installed: https://chocolatey.org/install
choco install -y python312
python3.12 -m pip install -U pip nuitka
python3.12 -m pip install -r ..\..\third_party\requirements_lock_cpu.txt
