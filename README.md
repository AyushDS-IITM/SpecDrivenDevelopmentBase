# TODO App - Kanban Board Scaffolding

A production-ready scaffolding for a full-stack TODO application with Kanban board capabilities.

## 🎯 What This App Does

- **Multi-board support**: Create and manage multiple Kanban boards
- **Task management**: Add, edit, delete tasks with priority and due dates
- **Column-based workflow**: Organize tasks by status (To Do, In Progress, Done, etc.)
- **List & Kanban views**: Switch between list and board views
- **User authentication**: Secure login and registration
- **Tag system**: Categorize and filter tasks
- **Task history**: Audit trail of all changes
- **Ready for Kanban evolution**: Drag-drop foundation ready

## 🏗️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | FastAPI + SQLAlchemy ORM + SQLite |
| Frontend | React 18 + Vite |
| Styling | CSS3 with responsive design |
| Deployment | Docker & Docker Compose |

## 🚀 Quick Start

### Using Docker (Recommended)
```bash
docker-compose up --build
```
- Backend: http://localhost:8000
- Frontend: http://localhost:5173
- API Docs: http://localhost:8000/docs

### Local Development
```bash
# Backend
pip install -r requirements.txt
uvicorn main:app --reload

# Frontend (in new terminal)
npm install
npm run dev
```

## 📁 Project Structure

See `SETUP.md` for detailed documentation on:
- Complete project structure
- All API endpoints
- Database schema
- Security considerations
- Future enhancements

## ✨ Features

✅ User authentication (JWT tokens)
✅ Multi-board Kanban system
✅ Task CRUD operations
✅ Priority & due date management
✅ Tag system for categorization
✅ Task history/audit log
✅ Responsive UI design
✅ Docker containerization
✅ SQLite database with ORM

## 🎨 UI Views

- **Kanban Board**: Drag-drop ready column view
- **List View**: Table-like task listing with filters
- **Login/Register**: Secure authentication

## 🔒 Security

- Password hashing with bcrypt
- JWT token-based authentication
- CORS support
- SQL injection protection (via SQLAlchemy ORM)

## 📚 Documentation

- `SETUP.md` - Comprehensive setup and feature documentation
- API docs available at `/docs` when backend is running

## 🛠️ Development

Install dependencies:
```bash
./setup.sh        # Mac/Linux
setup.bat         # Windows
```

## 🚢 Deployment Ready

- Fully containerized with Docker
- Environment configuration support
- Database migrations ready
- Production-grade code structure

---

**Built for scale**: This scaffolding is designed to evolve from a simple task list to a complex collaboration platform.

