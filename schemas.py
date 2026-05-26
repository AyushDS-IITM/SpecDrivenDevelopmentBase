"""Pydantic schemas for request/response validation."""
from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List


class UserCreate(BaseModel):
    """User registration schema."""
    username: str
    email: str
    password: str


class UserResponse(BaseModel):
    """User response schema."""
    id: int
    username: str
    email: str
    created_at: datetime

    class Config:
        from_attributes = True


class TagCreate(BaseModel):
    """Tag creation schema."""
    name: str


class TagResponse(BaseModel):
    """Tag response schema."""
    id: int
    name: str

    class Config:
        from_attributes = True


class TaskCreate(BaseModel):
    """Task creation schema."""
    title: str
    description: Optional[str] = None
    column_id: int
    priority: Optional[str] = "medium"
    due_date: Optional[datetime] = None


class TaskUpdate(BaseModel):
    """Task update schema."""
    title: Optional[str] = None
    description: Optional[str] = None
    column_id: Optional[int] = None
    priority: Optional[str] = None
    due_date: Optional[datetime] = None
    completed: Optional[bool] = None


class TaskResponse(BaseModel):
    """Task response schema."""
    id: int
    title: str
    description: Optional[str]
    column_id: int
    priority: str
    due_date: Optional[datetime]
    completed: bool
    order: int
    created_at: datetime
    updated_at: datetime
    tags: List[TagResponse] = []

    class Config:
        from_attributes = True


class ColumnCreate(BaseModel):
    """Column creation schema."""
    name: str
    order: int = 0


class ColumnResponse(BaseModel):
    """Column response schema."""
    id: int
    name: str
    order: int
    tasks: List[TaskResponse] = []

    class Config:
        from_attributes = True


class BoardCreate(BaseModel):
    """Board creation schema."""
    name: str
    description: Optional[str] = None


class BoardResponse(BaseModel):
    """Board response schema."""
    id: int
    name: str
    description: Optional[str]
    created_at: datetime
    updated_at: datetime
    columns: List[ColumnResponse] = []
    tags: List[TagResponse] = []

    class Config:
        from_attributes = True


class LoginRequest(BaseModel):
    """Login request schema."""
    username: str
    password: str


class TokenResponse(BaseModel):
    """JWT token response."""
    access_token: str
    token_type: str
    user: UserResponse
