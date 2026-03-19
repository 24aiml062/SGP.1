@echo off
echo Installing backend dependencies...
cd backend
pip install -r requirements.txt
cd ..
echo.
echo Setup complete!
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
