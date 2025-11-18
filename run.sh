#!/bin/bash
# Quick start script for Cooking Chatbot on macOS/Linux

echo ""
echo "========================================"
echo "   Cooking Chatbot - Quick Start"
echo "========================================"
echo ""

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "[ERROR] Virtual environment not found!"
    echo ""
    echo "Please create a virtual environment first:"
    echo "  python3 -m venv venv"
    echo "  source venv/bin/activate"
    echo ""
    exit 1
fi

# Activate virtual environment
source venv/bin/activate

echo "[OK] Virtual environment activated"

# Check if .env exists
if [ ! -f ".env" ]; then
    echo ""
    echo "[WARNING] .env file not found!"
    echo "Creating .env from template..."
    cp .env.example .env
    echo "[OK] .env created"
    echo ""
    echo "[IMPORTANT] Please edit .env file and add your OpenAI API key!"
    echo "Get it from: https://platform.openai.com/api-keys"
    echo ""
    read -p "Press Enter to continue..."
fi

# Run migrations
echo ""
echo "[INFO] Running database migrations..."
python manage.py migrate

if [ $? -ne 0 ]; then
    echo "[ERROR] Migration failed!"
    exit 1
fi

echo ""
echo "========================================"
echo "   Starting Cooking Chatbot Server"
echo "========================================"
echo ""
echo "The chatbot will be available at:"
echo "  http://127.0.0.1:8000/"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

# Start development server
python manage.py runserver
