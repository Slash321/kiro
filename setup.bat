@echo off
REM Kiro Bypass Tool - Windows Setup Script

echo ========================================
echo Kiro IDE Bypass Tool - Setup
echo ========================================
echo.

REM Check Python installation
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python is not installed or not in PATH
    echo Please install Python 3.8 or higher from python.org
    pause
    exit /b 1
)

echo [OK] Python found
python --version
echo.

REM Install dependencies
echo Installing dependencies...
pip install -r requirements.txt
if errorlevel 1 (
    echo [ERROR] Failed to install dependencies
    pause
    exit /b 1
)

echo.
echo [OK] Dependencies installed
echo.

REM Verify Kiro installation
echo Verifying Kiro installation...
python kiro_config.py
if errorlevel 1 (
    echo [WARNING] Kiro verification had issues
    echo Please check the output above
)

echo.
echo ========================================
echo Setup Complete!
echo ========================================
echo.
echo To run the tool:
echo   python kiro_main.py
echo.
echo For help, see docs\QUICKSTART.md
echo.
pause
