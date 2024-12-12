@echo off
:: Set application directories
set APP_DIR=%~dp0
set CONFIG_DIR=%APP_DIR%config
set LOGS_DIR=%APP_DIR%logs
set DEPENDENCIES_DIR=%APP_DIR%dependencies

:: Set specific dependency zip files
set PYTHON_ZIP=Python-3.12.5.zip
set PYINSTALLER_ZIP=pyinstaller-6.10.0.zip
set FFMPEG_ZIP=ffmpeg-master-latest-win64-gpl.zip
set KIVY_ZIP=kivy-2.3.0.zip
set YTDLP_ZIP=yt-dlp-2024.08.06.zip
set FLATPICKR_ZIP=flatpickr-4.6.13.zip

:: Log file
set LOG_FILE=%LOGS_DIR%\install.log

:: PowerShell extraction helper function
:ExtractZip
echo Extracting %1 to %2 >> %LOG_FILE%
PowerShell -Command "Expand-Archive -Path '%1' -DestinationPath '%2' -Force"
if %errorlevel% neq 0 (
    echo ERROR: Failed to extract %1 >> %LOG_FILE%
    exit /b 1
)
goto :eof

:: Create necessary directories
echo Creating necessary directories... >> %LOG_FILE%
if not exist %CONFIG_DIR% mkdir %CONFIG_DIR%
if not exist %LOGS_DIR% mkdir %LOGS_DIR%
if not exist %CONFIG_DIR%\python mkdir %CONFIG_DIR%\python
if not exist %CONFIG_DIR%\pyinstaller mkdir %CONFIG_DIR%\pyinstaller
if not exist %CONFIG_DIR%\ffmpeg mkdir %CONFIG_DIR%\ffmpeg
if not exist %CONFIG_DIR%\kivy mkdir %CONFIG_DIR%\kivy
if not exist %CONFIG_DIR%\yt-dlp mkdir %CONFIG_DIR%\yt-dlp
if not exist %CONFIG_DIR%\flatpickr mkdir %CONFIG_DIR%\flatpickr

:: Extract dependencies
echo Extracting dependencies... >> %LOG_FILE%
call :ExtractZip "%DEPENDENCIES_DIR%\%PYTHON_ZIP%" "%CONFIG_DIR%\python"
call :ExtractZip "%DEPENDENCIES_DIR%\%PYINSTALLER_ZIP%" "%CONFIG_DIR%\pyinstaller"
call :ExtractZip "%DEPENDENCIES_DIR%\%FFMPEG_ZIP%" "%CONFIG_DIR%\ffmpeg"
call :ExtractZip "%DEPENDENCIES_DIR%\%KIVY_ZIP%" "%CONFIG_DIR%\kivy"
call :ExtractZip "%DEPENDENCIES_DIR%\%YTDLP_ZIP%" "%CONFIG_DIR%\yt-dlp"
call :ExtractZip "%DEPENDENCIES_DIR%\%FLATPICKR_ZIP%" "%CONFIG_DIR%\flatpickr"

:: Upgrade pip and install Python dependencies
echo Installing Python and required modules... >> %LOG_FILE%
set PYTHON_DIR=%CONFIG_DIR%\python
set PATH=%PYTHON_DIR%\Scripts;%PYTHON_DIR%;%PATH%

%PYTHON_DIR%\python.exe -m ensurepip
%PYTHON_DIR%\python.exe -m pip install --upgrade pip

if exist "%APP_DIR%\requirements.txt" (
    %PYTHON_DIR%\python.exe -m pip install -r "%APP_DIR%\requirements.txt" >> %LOG_FILE% 2>&1
) else (
    echo ERROR: requirements.txt is missing! >> %LOG_FILE%
    exit /b 1
)

:: Install specific dependencies via pip
echo Installing PyInstaller... >> %LOG_FILE%
%PYTHON_DIR%\python.exe -m pip install %CONFIG_DIR%\pyinstaller

echo Installing Kivy... >> %LOG_FILE%
%PYTHON_DIR%\python.exe -m pip install %CONFIG_DIR%\kivy

echo Installing YT-DLP... >> %LOG_FILE%
%PYTHON_DIR%\python.exe -m pip install %CONFIG_DIR%\yt-dlp

:: Flatpickr setup (manual placement since it's a JS library)
echo Setting up Flatpickr... >> %LOG_FILE%
copy "%CONFIG_DIR%\flatpickr\flatpickr.js" "%APP_DIR%\assets\flatpickr.js"
copy "%CONFIG_DIR%\flatpickr\flatpickr.css" "%APP_DIR%\assets\flatpickr.css"

:: Fonts setup
echo Installing Fonts... >> %LOG_FILE%
copy "%APP_DIR%\assets\fonts\Arial.ttf" "%windir%\Fonts"
copy "%APP_DIR%\assets\fonts\Arial_Bold.ttf" "%windir%\Fonts"

:: Finalize installation
echo Installation completed successfully! >> %LOG_FILE%
echo Please check the install.log for detailed information.
pause
