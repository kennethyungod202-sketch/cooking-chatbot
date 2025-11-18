@echo off
REM Quick start script for Cooking Chatbot on Windows

echo.
echo ========================================
echo    Cooking Chatbot - Quick Start
echo ========================================
echo.

REM Check if virtual environment exists
if not exist "venv\" (
    echo [ERROR] Virtual environment not found!
    echo.
    echo Please create a virtual environment first:
    echo   python -m venv venv
    echo   .\venv\Scripts\Activate.ps1
    echo.
    pause
    exit /b 1
)

REM Activate virtual environment
call venv\Scripts\activate.bat

echo [OK] Virtual environment activated

REM Check if .env exists
if not exist ".env" (
    echo.
    echo [WARNING] .env file not found!
    echo Creating .env from template...
    copy .env.example .env
    echo [OK] .env created
    echo.
    echo [IMPORTANT] Please edit .env file and add your OpenAI API key!
    echo Get it from: https://platform.openai.com/api-keys
    echo.
    pause
)

REM Run migrations
echo.
echo [INFO] Running database migrations...
python manage.py migrate

if errorlevel 1 (
    echo [ERROR] Migration failed!
    pause
    exit /b 1
)

echo.
echo ========================================
echo    Starting Cooking Chatbot Server
echo ========================================
echo.
echo The chatbot will be available at:
echo   http://127.0.0.1:8000/
echo.
echo Press Ctrl+C to stop the server
echo.

REM Start development server
python manage.py runserver

pause
