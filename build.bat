@echo off
echo ================================================
echo BUILD EXECUTABLE - PyWebView + Svelte
echo ================================================

REM Check that Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python not found
    echo Install Python from https://python.org
    pause
    exit /b 1
)

REM Install dependencies if necessary
echo Installing dependencies...
pip install -r requirements.txt

REM Build frontend if necessary
if not exist "dist\index.html" (
    echo Building frontend...
    python run.py --build-only
)

REM Build executable
echo Building executable...
python build_exe.py

echo.
echo ================================================
echo BUILD COMPLETED!
echo ================================================
echo Executable: dist\app.exe
echo.
pause
