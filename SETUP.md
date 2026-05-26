# TODO App - Kanban Board Scaffolding

A full-stack TODO application with Kanban board capabilities, built for easy scaling and long-term feature expansion.

## 🏗️ Architecture

- **Backend**: FastAPI + SQLAlchemy ORM + SQLite
- **Frontend**: React + Vite
- **Database**: SQLite (file-based for simplicity)
- **Containerization**: Docker & Docker Compose

## 📁 Project Structure

```
├── main.py                    # FastAPI application entry point
├── config.py                  # Configuration settings
├── database.py                # SQLAlchemy setup & session management
├── models.py                  # ORM models (User, Board, Column, Task, Tag)
├── schemas.py                 # Pydantic request/response schemas
├── auth.py                    # Authentication utilities (JWT, password hashing)
├── crud.py                    # Database CRUD operations
│
├── App.jsx                    # React main component
├── LoginForm.jsx              # Authentication UI
├── TaskBoard.jsx              # Kanban board view
├── TaskList.jsx               # List view
├── TaskCard.jsx               # Reusable task card component
│
├── index.html                 # HTML entry point
├── main.jsx                   # React entry point
├── App.css                    # Global styles
├── index.css                  # Base styles
│
├── package.json               # Node dependencies
├── requirements.txt           # Python dependencies
├── vite.config.js             # Vite configuration
│
├── Dockerfile.backend         # Backend container
├── Dockerfile.frontend        # Frontend container
├── docker-compose.yml         # Docker Compose orchestration
│
└── README.md                  # This file
```

## 🚀 Quick Start

### Option 1: Docker Compose (Recommended)

```bash
docker-compose up --build
```

- Backend runs on: http://localhost:8000
- Frontend runs on: http://localhost:5173
- API docs: http://localhost:8000/docs

### Option 2: Local Development

#### Backend Setup
```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

#### Frontend Setup
```bash
npm install
npm run dev
```

## 📚 API Endpoints

### Authentication
- `POST /api/auth/register` - Register new user
- `POST /api/auth/login` - Login and get JWT token

### Boards
- `GET /api/boards` - List all user boards
- `POST /api/boards` - Create new board
- `GET /api/boards/{id}` - Get board details

### Columns (Status stages)
- `GET /api/boards/{id}/columns` - List board columns
- `POST /api/boards/{id}/columns` - Create new column

### Tasks
- `POST /api/boards/{id}/tasks` - Create new task
- `GET /api/columns/{id}/tasks` - Get column tasks
- `PUT /api/tasks/{id}` - Update task
- `DELETE /api/tasks/{id}` - Delete task
- `POST /api/tasks/reorder` - Reorder tasks (for Kanban drag-drop)

## 🎨 UI Features

### Current Implementation
- ✅ User authentication (register/login)
- ✅ Kanban board view with columns
- ✅ Task list view with filters
- ✅ Task card components with priority levels
- ✅ Add/edit/delete tasks
- ✅ Responsive design

### Kanban-Ready Features (Foundation Built)
- ✅ Multi-board support
- ✅ Multiple columns per board
- ✅ Task ordering/reordering support
- ✅ Task metadata (priority, due date, tags)
- ✅ Task history tracking

## 🔄 Database Schema

### Users
- id, username, email, password_hash, created_at, updated_at

### Boards
- id, name, description, user_id, created_at, updated_at

### Columns (Status stages)
- id, name, order, board_id, created_at

### Tasks
- id, title, description, board_id, column_id, order, priority, due_date, completed, created_at, updated_at

### Tags & Task_Tags
- Support tagging and categorization of tasks

### Task_History
- Audit log of all task changes

## 🛠️ Future Enhancements

1. **Drag-and-Drop**: Use React Beautiful DnD or React DnD
2. **Real-time Updates**: WebSocket support for live collaboration
3. **Advanced Filters**: Search, date ranges, assignees
4. **Integrations**: Slack, GitHub, Calendar sync
5. **Analytics**: Time tracking, burndown charts
6. **Mobile**: React Native app
7. **Database**: Migrate from SQLite to PostgreSQL
8. **Cache**: Redis for performance optimization
9. **File Attachments**: Task attachments support
10. **Comments**: Inline task discussions

## 🔐 Security Notes

- Change `SECRET_KEY` in production
- Use environment variables for sensitive data
- Implement role-based access control (RBAC)
- Add rate limiting
- Enable HTTPS in production
- Regular dependency updates

## 📝 Development

### Running Tests (To be added)
```bash
pytest tests/
```

### Code Quality
```bash
pylint main.py
eslint src/
```

## 🤝 Contributing

1. Create a feature branch
2. Make your changes
3. Test thoroughly
4. Submit a PR

## 📄 License

MIT License - Feel free to use this scaffolding for your projects!
