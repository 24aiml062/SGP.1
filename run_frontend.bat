@echo off
echo ========================================
echo AI Digital Growth Agent - Frontend
echo ========================================
echo.
echo Starting frontend server on http://localhost:8001
echo Make sure backend is running on http://localhost:8000
echo.
echo Open your browser to: http://localhost:8001
echo Press Ctrl+C to stop the server
echo.
cd frontend
python -m http.server 8001
