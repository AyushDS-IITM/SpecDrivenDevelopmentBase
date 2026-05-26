@echo off
REM Quick setup script for Windows

echo 🚀 Setting up TODO App...

REM Backend setup
echo 📦 Installing Python dependencies...
pip install -r requirements.txt

REM Frontend setup
echo 📦 Installing Node dependencies...
call npm install

echo ✅ Setup complete!
echo.
echo 🎯 To start development:
echo    Option 1 (Docker): docker-compose up --build
echo    Option 2 (Local): 
echo       - Backend: uvicorn main:app --reload
echo       - Frontend: npm run dev
