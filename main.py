"""Main FastAPI application."""
from fastapi import FastAPI, Depends, HTTPException, status, HTTPException as HTTPExc
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import engine, get_db, Base
from models import User
from schemas import UserCreate, UserResponse, LoginRequest, TokenResponse, BoardCreate, BoardResponse, ColumnCreate, ColumnResponse, TaskCreate, TaskResponse, TaskUpdate
from crud import (
    get_user_by_username, create_user, get_user_by_id, create_board, get_user_boards,
    get_board, create_column, get_board_columns, create_task, get_column_tasks,
    update_task, delete_task, reorder_tasks
)
from auth import verify_password, create_access_token, decode_token
from config import ALLOWED_ORIGINS
from typing import List

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="TODO App API", version="1.0.0")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_current_user(token: str = None, db: Session = Depends(get_db)) -> User:
    """Get current authenticated user from token."""
    if not token:
        raise HTTPException(status_code=401, detail="Not authenticated")
    
    payload = decode_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid token")
    
    username = payload.get("sub")
    user = get_user_by_username(db, username)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    return user


# Auth endpoints
@app.post("/api/auth/register", response_model=UserResponse)
def register(user: UserCreate, db: Session = Depends(get_db)):
    """Register a new user."""
    db_user = get_user_by_username(db, user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    
    new_user = create_user(db, user.username, user.email, user.password)
    return new_user


@app.post("/api/auth/login", response_model=TokenResponse)
def login(request: LoginRequest, db: Session = Depends(get_db)):
    """Login user and return JWT token."""
    user = get_user_by_username(db, request.username)
    if not user or not verify_password(request.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    access_token = create_access_token({"sub": user.username})
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user": user
    }


# Board endpoints
@app.post("/api/boards", response_model=BoardResponse)
def create_new_board(board: BoardCreate, token: str = None, db: Session = Depends(get_db)):
    """Create a new board."""
    user = get_current_user(token, db)
    new_board = create_board(db, board, user.id)
    return new_board


@app.get("/api/boards", response_model=List[BoardResponse])
def list_boards(token: str = None, db: Session = Depends(get_db)):
    """Get all boards for current user."""
    user = get_current_user(token, db)
    boards = get_user_boards(db, user.id)
    return boards


@app.get("/api/boards/{board_id}", response_model=BoardResponse)
def get_board_detail(board_id: int, token: str = None, db: Session = Depends(get_db)):
    """Get board details by ID."""
    user = get_current_user(token, db)
    board = get_board(db, board_id)
    if not board or board.user_id != user.id:
        raise HTTPException(status_code=404, detail="Board not found")
    return board


# Column endpoints
@app.post("/api/boards/{board_id}/columns", response_model=ColumnResponse)
def create_new_column(board_id: int, column: ColumnCreate, token: str = None, db: Session = Depends(get_db)):
    """Create a new column in a board."""
    user = get_current_user(token, db)
    board = get_board(db, board_id)
    if not board or board.user_id != user.id:
        raise HTTPException(status_code=404, detail="Board not found")
    
    new_column = create_column(db, board_id, column)
    return new_column


@app.get("/api/boards/{board_id}/columns", response_model=List[ColumnResponse])
def list_board_columns(board_id: int, token: str = None, db: Session = Depends(get_db)):
    """Get all columns in a board."""
    user = get_current_user(token, db)
    board = get_board(db, board_id)
    if not board or board.user_id != user.id:
        raise HTTPException(status_code=404, detail="Board not found")
    
    columns = get_board_columns(db, board_id)
    return columns


# Task endpoints
@app.post("/api/boards/{board_id}/tasks", response_model=TaskResponse)
def create_new_task(board_id: int, task: TaskCreate, token: str = None, db: Session = Depends(get_db)):
    """Create a new task in a board."""
    user = get_current_user(token, db)
    board = get_board(db, board_id)
    if not board or board.user_id != user.id:
        raise HTTPException(status_code=404, detail="Board not found")
    
    new_task = create_task(db, task, board_id)
    return new_task


@app.get("/api/columns/{column_id}/tasks", response_model=List[TaskResponse])
def list_column_tasks(column_id: int, token: str = None, db: Session = Depends(get_db)):
    """Get all tasks in a column."""
    tasks = get_column_tasks(db, column_id)
    return tasks


@app.put("/api/tasks/{task_id}", response_model=TaskResponse)
def update_existing_task(task_id: int, task_update: TaskUpdate, token: str = None, db: Session = Depends(get_db)):
    """Update a task."""
    get_current_user(token, db)
    updated_task = update_task(db, task_id, task_update)
    if not updated_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated_task


@app.delete("/api/tasks/{task_id}")
def delete_existing_task(task_id: int, token: str = None, db: Session = Depends(get_db)):
    """Delete a task."""
    get_current_user(token, db)
    deleted_task = delete_task(db, task_id)
    if not deleted_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task deleted successfully"}


@app.post("/api/tasks/reorder")
def reorder_column_tasks(column_id: int, task_ids: List[int], token: str = None, db: Session = Depends(get_db)):
    """Reorder tasks in a column (for drag-drop support)."""
    get_current_user(token, db)
    reorder_tasks(db, task_ids)
    return {"message": "Tasks reordered successfully"}


@app.get("/api/health")
def health_check():
    """Health check endpoint."""
    return {"status": "healthy"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
