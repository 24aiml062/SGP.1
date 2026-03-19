@echo off
echo Installing backend dependencies (lightweight version)...
cd backend
pip install -r requirements-lite.txt
cd ..
echo.
echo Setup complete!
echo.
echo This version uses rule-based AI logic without heavy ML models.
echo For full AI capabilities, run setup.bat instead.
echo.
echo To run the backend server:
echo   cd backend
echo   python main.py
echo.
echo To run the frontend:
echo   cd frontend
echo   python -m http.server 8000
echo.
pause
