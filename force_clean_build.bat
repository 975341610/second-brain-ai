@echo off
echo ====================================================
echo   Performing Forced Clean Build - Bypassing Local Cache
echo ====================================================

echo Removing project build folder...
if exist "build" rd /s /q "build"

echo Removing frontend dist folder...
if exist "frontend\dist" rd /s /q "frontend\dist"

echo Updating frontend dependencies and building...
cd frontend
call npm install
call npm run build
cd ..

echo Running PyInstaller with --clean...
set "VERSION=unknown"
if exist "VERSION.txt" (
    for /f "usebackq delims=" %%v in ("VERSION.txt") do set "VERSION=%%v"
)
echo Current Version: !VERSION!
call pyinstaller --clean second_brain_ai.spec

echo Cleaning up top-level standalone EXE in dist...
if exist "dist\SecondBrainAI.exe" del /f /q "dist\SecondBrainAI.exe"

echo ====================================================
echo   Clean Build Completed Successfully!
echo ====================================================
pause
