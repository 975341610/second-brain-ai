@echo off
setlocal enabledelayedexpansion

echo ==========================================
echo    Nova Project - One-Click Startup Script
echo ==========================================

:: 1. Check Python environment
echo [*] Checking Python environment...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [!] Python is not installed or not in PATH. Please install Python.
    pause
    exit /b 1
)

:: 2. Check npm environment
echo [*] Checking npm environment...
npm --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [!] npm is not installed or not in PATH. Please install Node.js/npm.
    pause
    exit /b 1
)

:: 3. Install backend dependencies
echo [*] Installing backend dependencies...
python -m pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo [!] Failed to install backend dependencies.
    pause
    exit /b 1
)

:: 4. Start backend service in a new window
echo [*] Starting backend service in a new window...
start "Nova Backend" cmd /k "python start_backend.py"

:: 5. Frontend startup
echo [*] Moving to frontend directory: nova-block/
cd nova-block
if %errorlevel% neq 0 (
    echo [!] Directory nova-block not found.
    pause
    exit /b 1
)

echo [*] Installing frontend dependencies (npm install)...
call npm install
if %errorlevel% neq 0 (
    echo [!] Failed to install frontend dependencies.
    pause
    exit /b 1
)

:: 6. Prompt and start frontend
echo.
echo ==========================================
echo    [SUCCESS] Frontend is starting...
echo    URL: http://localhost:5173
echo ==========================================
echo.
npm run dev

pause
