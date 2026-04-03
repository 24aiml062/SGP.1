@echo off
echo ========================================
echo  Digital Growth Agent
echo ========================================
echo.

echo Killing any process on port 8080 or 8001...
for /f "tokens=5" %%a in ('netstat -ano ^| findstr :8080 2^>nul') do taskkill /PID %%a /F >nul 2>&1
for /f "tokens=5" %%a in ('netstat -ano ^| findstr :8001 2^>nul') do taskkill /PID %%a /F >nul 2>&1
timeout /t 1 >nul

echo Starting Backend on http://localhost:8080 ...
start "Backend" cmd /k "python main.py"
timeout /t 4 >nul

echo Starting Frontend on http://localhost:8001 ...
start "Frontend" cmd /k "cd frontend && python -m http.server 8001"
timeout /t 2 >nul

echo Opening browser...
start http://localhost:8001/index.html

echo.
echo ========================================
echo  App is running!
echo ========================================
echo  Homepage  : http://localhost:8001/index.html
echo  Analyze   : http://localhost:8001/analyze.html
echo  Content   : http://localhost:8001/content.html
echo  API check : http://localhost:8080
echo ========================================
echo.
echo Close the Backend and Frontend windows to stop.
pause
