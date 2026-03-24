@echo off
setlocal enabledelayedexpansion
title Second Brain AI - Fast Update (Backend Only)

set "ROOT=%~dp0"
set "OUT_DIR=C:\AI"
set "APP_DIR=%OUT_DIR%\SecondBrainAI"
set "VENV_PY=%ROOT%.venv\Scripts\python.exe"

echo ==============================================
echo   Second Brain AI - 极速热更新 (仅更新后端)
echo ==============================================
echo.

if not exist "%VENV_PY%" (
    echo [!] 虚拟环境不存在，请先运行一次 build_windows.bat
    pause
    exit /b 1
)

echo [1/3] 正在清理旧的构建缓存...
if exist build rmdir /s /q build
if exist dist rmdir /s /q dist

echo [2/3] 正在重新打包后端 EXE (跳过前端编译)...
"%VENV_PY%" -m PyInstaller second_brain_ai.spec --noconfirm --clean
if errorlevel 1 (
    echo [!] 打包失败，请检查报错。
    pause
    exit /b 1
)

echo [3/3] 正在覆盖更新到 %APP_DIR% ...
:: 尝试结束正在运行的程序，防止文件占用
taskkill /f /im SecondBrainAI.exe >nul 2>nul
timeout /t 1 >nul

xcopy /e /i /y dist\SecondBrainAI "%APP_DIR%" >nul
if errorlevel 1 (
    echo [!] 覆盖失败！请确保程序已完全关闭，或者尝试以管理员权限运行此脚本。
    pause
    exit /b 1
)

echo.
echo ==============================================
echo   ✨ 更新完成！
echo   现在你可以直接双击桌面或 %APP_DIR% 下的程序了。
echo ==============================================
echo.
pause
exit /b 0
