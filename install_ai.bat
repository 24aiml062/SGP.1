@echo off
echo ========================================
echo AI Digital Growth Agent - AI Setup
echo ========================================
echo.
echo This will install AI capabilities using OpenAI GPT
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
echo Installing AI dependencies...
cd backend
pip install -r requirements-ai.txt
if errorlevel 1 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)
cd ..
echo.
echo ========================================
echo AI Dependencies Installed!
echo ========================================
echo.
echo Next Steps:
echo 1. Get your OpenAI API key from: https://platform.openai.com/api-keys
echo 2. Set environment variable:
echo    set OPENAI_API_KEY=sk-your-key-here
echo 3. Run: start.bat
echo.
echo For detailed setup instructions, see: AI_SETUP_GUIDE.md
echo.
pause
