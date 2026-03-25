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
call pyinstaller --clean second_brain_ai.spec

echo ====================================================
echo   Clean Build Completed Successfully!
echo ====================================================
pause
