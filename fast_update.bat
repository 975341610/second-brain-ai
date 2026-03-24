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

echo [2/4] 智能检测前端是否需要重新构建...
set "BUILD_FRONTEND=0"

:: 1. 检查 frontend_dist 是否存在
if not exist "%ROOT%frontend_dist" (
    echo [*] 未找到 frontend_dist 目录，强制构建前端...
    set "BUILD_FRONTEND=1"
) else (
    :: 2. 比较 frontend 源码与 frontend_dist 产物的修改时间
    :: 寻找 frontend/src 下最近修改的文件
    for /f "tokens=1-3" %%a in ('dir /s /b /a-d /o-d "%ROOT%frontend\src" 2^>nul') do (
        set "LATEST_SRC=%%a"
        goto :compare_time
    )
    :compare_time
    
    :: 寻找 frontend_dist 下最近修改的文件
    for /f "tokens=1-3" %%a in ('dir /s /b /a-d /o-d "%ROOT%frontend_dist" 2^>nul') do (
        set "LATEST_DIST=%%a"
        goto :do_compare
    )
    :do_compare

    if defined LATEST_SRC (
        for /f "usebackq" %%i in (`powershell -NoProfile -Command "(Get-Item '%LATEST_SRC%').LastWriteTime -gt (Get-Item '%LATEST_DIST%').LastWriteTime"`) do (
            if "%%i"=="True" (
                echo [*] 检测到前端源码有更新，正在重新构建...
                set "BUILD_FRONTEND=1"
            )
        )
    )
)

if "!BUILD_FRONTEND!"=="1" (
    echo [*] 正在执行前端构建 (npm run build)...
    cd /d "%ROOT%frontend"
    call npm run build
    if errorlevel 1 (
        echo [!] 前端构建失败，请检查 Node.js 环境。
        pause
        exit /b 1
    )
    cd /d "%ROOT%"
    if exist "frontend_dist" rmdir /s /q "frontend_dist"
    mkdir "frontend_dist"
    xcopy /e /i /y "frontend\dist" "frontend_dist" >nul
) else (
    echo [*] 前端代码无变化，跳过构建加速流程。
)

echo [3/4] 正在重新打包后端 EXE...
"%VENV_PY%" -m PyInstaller second_brain_ai.spec --noconfirm --clean
if errorlevel 1 (
    echo [!] 打包失败，请检查报错。
    pause
    exit /b 1
)

echo [4/4] 正在覆盖更新到 %APP_DIR% ...
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
