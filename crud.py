"""CRUD operations for database models."""
from sqlalchemy.orm import Session
from models import User, Board, Column, Task, Tag, TaskHistory, TaskTag
from schemas import TaskCreate, TaskUpdate, BoardCreate, ColumnCreate, TagCreate
from auth import hash_password
from datetime import datetime


# User operations
def get_user_by_username(db: Session, username: str):
    """Get user by username."""
    return db.query(User).filter(User.username == username).first()


def get_user_by_id(db: Session, user_id: int):
    """Get user by ID."""
    return db.query(User).filter(User.id == user_id).first()


def create_user(db: Session, username: str, email: str, password: str):
    """Create a new user."""
    hashed_password = hash_password(password)
    db_user = User(username=username, email=email, password_hash=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# Board operations
def create_board(db: Session, board: BoardCreate, user_id: int):
    """Create a new board."""
    db_board = Board(name=board.name, description=board.description, user_id=user_id)
    db.add(db_board)
    db.commit()
    db.refresh(db_board)
    return db_board


def get_board(db: Session, board_id: int):
    """Get board by ID."""
    return db.query(Board).filter(Board.id == board_id).first()


def get_user_boards(db: Session, user_id: int):
    """Get all boards for a user."""
    return db.query(Board).filter(Board.user_id == user_id).all()


def update_board(db: Session, board_id: int, name: str, description: str):
    """Update board details."""
    db_board = get_board(db, board_id)
    if db_board:
        db_board.name = name
        db_board.description = description
        db_board.updated_at = datetime.utcnow()
        db.commit()
        db.refresh(db_board)
    return db_board


def delete_board(db: Session, board_id: int):
    """Delete a board."""
    db_board = get_board(db, board_id)
    if db_board:
        db.delete(db_board)
        db.commit()
    return db_board


# Column operations
def create_column(db: Session, board_id: int, column: ColumnCreate):
    """Create a new column."""
    db_column = Column(name=column.name, order=column.order, board_id=board_id)
    db.add(db_column)
    db.commit()
    db.refresh(db_column)
    return db_column


def get_column(db: Session, column_id: int):
    """Get column by ID."""
    return db.query(Column).filter(Column.id == column_id).first()


def get_board_columns(db: Session, board_id: int):
    """Get all columns for a board."""
    return db.query(Column).filter(Column.board_id == board_id).order_by(Column.order).all()


def update_column(db: Session, column_id: int, name: str, order: int):
    """Update column details."""
    db_column = get_column(db, column_id)
    if db_column:
        db_column.name = name
        db_column.order = order
        db.commit()
        db.refresh(db_column)
    return db_column


def delete_column(db: Session, column_id: int):
    """Delete a column."""
    db_column = get_column(db, column_id)
    if db_column:
        db.delete(db_column)
        db.commit()
    return db_column


# Task operations
def create_task(db: Session, task: TaskCreate, board_id: int):
    """Create a new task."""
    db_task = Task(
        title=task.title,
        description=task.description,
        board_id=board_id,
        column_id=task.column_id,
        priority=task.priority or "medium"
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


def get_task(db: Session, task_id: int):
    """Get task by ID."""
    return db.query(Task).filter(Task.id == task_id).first()


def get_column_tasks(db: Session, column_id: int):
    """Get all tasks in a column."""
    return db.query(Task).filter(Task.column_id == column_id).order_by(Task.order).all()


def get_board_tasks(db: Session, board_id: int):
    """Get all tasks in a board."""
    return db.query(Task).filter(Task.board_id == board_id).all()


def update_task(db: Session, task_id: int, task_update: TaskUpdate):
    """Update task details."""
    db_task = get_task(db, task_id)
    if db_task:
        if task_update.title is not None:
            db_task.title = task_update.title
        if task_update.description is not None:
            db_task.description = task_update.description
        if task_update.column_id is not None:
            db_task.column_id = task_update.column_id
        if task_update.priority is not None:
            db_task.priority = task_update.priority
        if task_update.due_date is not None:
            db_task.due_date = task_update.due_date
        if task_update.completed is not None:
            db_task.completed = task_update.completed
        db_task.updated_at = datetime.utcnow()
        db.commit()
        db.refresh(db_task)
    return db_task


def delete_task(db: Session, task_id: int):
    """Delete a task."""
    db_task = get_task(db, task_id)
    if db_task:
        db.delete(db_task)
        db.commit()
    return db_task


def reorder_tasks(db: Session, task_ids: list):
    """Reorder tasks in a column."""
    for index, task_id in enumerate(task_ids):
        db_task = get_task(db, task_id)
        if db_task:
            db_task.order = index
    db.commit()


# Tag operations
def create_tag(db: Session, board_id: int, tag: TagCreate):
    """Create a new tag."""
    db_tag = Tag(name=tag.name, board_id=board_id)
    db.add(db_tag)
    db.commit()
    db.refresh(db_tag)
    return db_tag


def get_board_tags(db: Session, board_id: int):
    """Get all tags for a board."""
    return db.query(Tag).filter(Tag.board_id == board_id).all()


def add_tag_to_task(db: Session, task_id: int, tag_id: int):
    """Add a tag to a task."""
    db_task_tag = TaskTag(task_id=task_id, tag_id=tag_id)
    db.add(db_task_tag)
    db.commit()


def remove_tag_from_task(db: Session, task_id: int, tag_id: int):
    """Remove a tag from a task."""
    db.query(TaskTag).filter(
        TaskTag.task_id == task_id,
        TaskTag.tag_id == tag_id
    ).delete()
    db.commit()
