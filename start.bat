@echo off
echo ========================================
echo AI Digital Growth Agent
echo ========================================
echo.
echo This will start both backend and frontend servers
echo.
echo Backend: http://localhost:8000
echo Frontend: http://localhost:8001
echo.
echo Press any key to continue...
pause > nul

start "Backend Server" cmd /k "cd backend && python main.py"
timeout /t 3 > nul
start "Frontend Server" cmd /k "cd frontend && python -m http.server 8001"
timeout /t 2 > nul

echo.
echo ========================================
echo Servers are starting...
echo ========================================
echo.
echo Backend: http://localhost:8000
echo Frontend: http://localhost:8001
echo.
echo Opening browser...
timeout /t 3 > nul
start http://localhost:8001/index.html
echo.
echo Close the server windows to stop the application
echo.
pause
