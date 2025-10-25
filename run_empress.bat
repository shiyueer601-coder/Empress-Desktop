@echo off
chcp 65001 >nul
title 女帝启示录 - 启动器

echo.
echo ========================================
echo           女帝启示录启动器
echo ========================================
echo.

:: 检查Python是否安装
python --version >nul 2>&1
if errorlevel 1 (
    echo [错误] 未检测到Python，请先安装Python 3.6或更高版本
    echo 下载地址: https://www.python.org/downloads/
    pause
    exit /b 1
)

echo [信息] 检测到Python环境
python --version

:: 切换到项目目录
cd /d "%~dp0"
echo [信息] 当前目录: %CD%

:: 检查main.py是否存在
if not exist "src\main.py" (
    echo [错误] 未找到 src\main.py 文件
    echo 请确保在正确的项目目录中运行此脚本
    pause
    exit /b 1
)

echo [信息] 找到主程序文件

:: 检查依赖
echo [信息] 检查依赖包...
python -c "import tkinter" >nul 2>&1
if errorlevel 1 (
    echo [警告] tkinter模块可能未正确安装
    echo 请确保Python安装时包含了tkinter
)

:: 启动应用
echo.
echo [信息] 正在启动女帝启示录...
echo 请稍候...
echo.

python src\main.py

:: 检查程序退出状态
if errorlevel 1 (
    echo.
    echo [错误] 程序异常退出，错误代码: %errorlevel%
    echo 请检查错误信息或联系开发者
) else (
    echo.
    echo [信息] 程序正常退出
)

echo.
echo 按任意键退出...
pause >nul
