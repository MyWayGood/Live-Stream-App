@echo off
:: Batch script to create an executable for the Live Stream Windows App using PyInstaller

:: Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed. Please install Python 3.12.5 and rerun the script.
    exit /b 1
)

:: Check if PyInstaller is installed
pip show pyinstaller >nul 2>&1
if %errorlevel% neq 0 (
    echo PyInstaller is not installed. Installing PyInstaller...
    pip install pyinstaller
)

:: Navigate to the app directory
cd /d "%~dp0"

:: Create executable using PyInstaller
echo Creating executable for Live Stream Windows App...
pyinstaller --onefile --windowed --icon=assets/icons/icon.ico main.py

:: Check if the executable was created
if exist dist\main.exe (
    echo Executable created successfully in the dist folder.
) else (
    echo Failed to create the executable.
    exit /b 1
)

:: Notify the user
echo The executable has been created and saved in the "dist" folder.
pause
