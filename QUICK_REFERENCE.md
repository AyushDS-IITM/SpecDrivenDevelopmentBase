# 🚀 Quick Reference Guide

## Command Cheat Sheet

### 🐳 Docker (Recommended)
```bash
# Start everything
docker-compose up --build

# Start specific service
docker-compose up backend
docker-compose up frontend

# View logs
docker-compose logs -f backend
docker-compose logs -f frontend

# Stop everything
docker-compose down

# Remove volumes too
docker-compose down -v
```

### 🐍 Backend (Local)
```bash
# Install dependencies
pip install -r requirements.txt

# Run development server
uvicorn main:app --reload

# Run with specific host/port
uvicorn main:app --host 0.0.0.0 --port 8000

# Generate API documentation
# Available at http://localhost:8000/docs
```

### ⚛️ Frontend (Local)
```bash
# Install dependencies
npm install

# Development server
npm run dev

# Build for production
npm build

# Preview production build
npm run preview
```

## 📍 URLs When Running

| Service | URL | Purpose |
|---------|-----|---------|
| Frontend | http://localhost:5173 | React app |
| Backend API | http://localhost:8000 | REST API |
| API Docs | http://localhost:8000/docs | Swagger UI |
| API ReDoc | http://localhost:8000/redoc | ReDoc docs |

## 🔐 Demo Login

After setup, create an account by registering on the frontend.

Credentials (after registration):
- Username: `your_username`
- Password: `your_password`

## 📂 Key File Locations

### Backend
- **API Routes**: `main.py` (lines 50-200)
- **Database Models**: `models.py` (all models)
- **CRUD Operations**: `crud.py` (all operations)
- **Authentication**: `auth.py` (tokens & hashing)

### Frontend
- **Main App**: `App.jsx` (component logic)
- **Authentication**: `LoginForm.jsx`
- **Kanban View**: `TaskBoard.jsx`
- **List View**: `TaskList.jsx`
- **Styles**: `App.css` (all styling)

## 🔧 Configuration

### Backend (`config.py`)
```python
DATABASE_URL = "sqlite:///./todo_app.db"
SECRET_KEY = "your-secret-key"  # Change in production
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
ALLOWED_ORIGINS = ["http://localhost:3000", "http://localhost:5173"]
```

### Frontend (`vite.config.js`)
```javascript
server: {
  port: 5173,
  proxy: {
    '/api': 'http://localhost:8000'  // Backend proxy
  }
}
```

## 📦 Dependencies

### Python (Backend)
- fastapi: Web framework
- uvicorn: ASGI server
- sqlalchemy: ORM
- pydantic: Validation
- python-jose: JWT tokens
- passlib: Password hashing

### JavaScript (Frontend)
- react: UI framework
- react-dom: DOM rendering
- axios: HTTP client (ready to add)
- vite: Build tool

## 🧪 Testing the API

### Using Swagger UI (Recommended)
1. Go to http://localhost:8000/docs
2. Try API endpoints with "Try it out" button

### Using curl

**Register**
```bash
curl -X POST "http://localhost:8000/api/auth/register" \
  -H "Content-Type: application/json" \
  -d '{"username":"testuser","email":"test@example.com","password":"password123"}'
```

**Login**
```bash
curl -X POST "http://localhost:8000/api/auth/login" \
  -H "Content-Type: application/json" \
  -d '{"username":"testuser","password":"password123"}'
```

**Create Board** (replace TOKEN with access_token from login)
```bash
curl -X POST "http://localhost:8000/api/boards" \
  -H "Authorization: Bearer TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"name":"My First Board","description":"Test board"}'
```

## 🐛 Troubleshooting

### Port Already in Use
```bash
# Linux/Mac - Kill process on port
lsof -ti:8000 | xargs kill -9
lsof -ti:5173 | xargs kill -9

# Windows - Kill process on port
netstat -ano | findstr :8000
taskkill /PID <PID> /F
```

### Database Issues
```bash
# Remove database file to reset
rm todo_app.db
# Or start fresh with docker
docker-compose down -v && docker-compose up --build
```

### Frontend Not Connecting to Backend
- Check CORS configuration in `config.py`
- Verify backend is running on port 8000
- Check browser console for errors
- Ensure `http://localhost:5173` is in ALLOWED_ORIGINS

### Python Version Issues
```bash
# Ensure Python 3.11+
python --version
python3 --version
```

## 📊 Database Schema Quick View

```
Users
  ├── id (PK)
  ├── username (UNIQUE)
  ├── email (UNIQUE)
  └── password_hash

Boards
  ├── id (PK)
  ├── name
  ├── user_id (FK)
  └── created_at

Columns (Status)
  ├── id (PK)
  ├── name
  ├── board_id (FK)
  └── order

Tasks
  ├── id (PK)
  ├── title
  ├── column_id (FK)
  ├── priority
  ├── due_date
  └── completed

Tags
  ├── id (PK)
  ├── name
  └── board_id (FK)

Task_Tags (Junction)
  ├── task_id (FK)
  └── tag_id (FK)

Task_History (Audit)
  ├── id (PK)
  ├── task_id (FK)
  ├── action
  └── timestamp
```

## 🎯 Next Development Steps

1. **Add Drag-Drop**: Install `react-beautiful-dnd`
2. **Add Testing**: pytest for backend, Vitest for frontend
3. **Add Validation**: More detailed error messages
4. **Add Pagination**: For large task lists
5. **Add Sorting**: Sort by priority, date, etc.
6. **Add Search**: Full-text task search
7. **Add Collaboration**: Real-time updates with WebSocket
8. **Add Themes**: Dark mode support
9. **Add Mobile**: Responsive improvements or React Native

## 📞 Common Tasks

### Add a new API endpoint
1. Add function to `crud.py`
2. Add route to `main.py`
3. Add schema to `schemas.py` if needed

### Add a new React component
1. Create `.jsx` file in project root
2. Import in `App.jsx`
3. Add styling to `App.css`

### Deploy to production
1. Set environment variables
2. Use PostgreSQL instead of SQLite
3. Set up Nginx/Apache reverse proxy
4. Configure HTTPS/SSL
5. Use Docker in production

---

**Happy coding! 🎉**
