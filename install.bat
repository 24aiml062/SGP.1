@echo off
echo ========================================
echo AI Digital Growth Agent - Installation
echo ========================================
echo.
echo Checking Python installation...
python --version
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python from https://www.python.org/downloads/
    pause
    exit /b 1
)
echo.
echo Installing backend dependencies...
cd backend
pip install -r requirements-lite.txt
if errorlevel 1 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)
cd ..
echo.
echo ========================================
echo Installation Complete!
echo ========================================
echo.
echo To start the application, run: start.bat
echo.
pause
