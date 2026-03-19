@echo off
echo ========================================
echo System Check
echo ========================================
echo.

echo Checking Python...
python --version
if errorlevel 1 (
    echo [FAIL] Python not found
    goto :error
) else (
    echo [OK] Python installed
)
echo.

echo Checking pip...
pip --version
if errorlevel 1 (
    echo [FAIL] pip not found
    goto :error
) else (
    echo [OK] pip installed
)
echo.

echo Checking required packages...
python -c "import fastapi; print('[OK] fastapi installed')" 2>nul || echo [MISSING] fastapi - run install.bat
python -c "import uvicorn; print('[OK] uvicorn installed')" 2>nul || echo [MISSING] uvicorn - run install.bat
python -c "import pydantic; print('[OK] pydantic installed')" 2>nul || echo [MISSING] pydantic - run install.bat
echo.

echo Checking project files...
if exist "backend\main.py" (echo [OK] backend\main.py) else (echo [FAIL] backend\main.py missing)
if exist "backend\agent.py" (echo [OK] backend\agent.py) else (echo [FAIL] backend\agent.py missing)
if exist "frontend\index.html" (echo [OK] frontend\index.html) else (echo [FAIL] frontend\index.html missing)
if exist "frontend\script.js" (echo [OK] frontend\script.js) else (echo [FAIL] frontend\script.js missing)
echo.

echo Testing agent...
python test_agent.py
if errorlevel 1 (
    echo [FAIL] Agent test failed
    goto :error
) else (
    echo.
    echo [OK] Agent test passed
)
echo.

echo ========================================
echo All checks passed!
echo ========================================
echo.
echo You can now run: start.bat
echo.
pause
exit /b 0

:error
echo.
echo ========================================
echo Setup incomplete!
echo ========================================
echo.
echo Please run: install.bat
echo.
pause
exit /b 1
