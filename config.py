"""Configuration settings for the TODO app backend."""
import os
from pathlib import Path

# Database
DATABASE_URL = "sqlite:///./todo_app.db"
BASE_DIR = Path(__file__).parent

# API
API_TITLE = "TODO App API"
API_VERSION = "1.0.0"

# JWT
SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key-change-in-production")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# CORS
ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://localhost:5173",
    "http://127.0.0.1:3000",
    "http://127.0.0.1:5173",
]
