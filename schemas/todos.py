from pydantic import BaseModel
from datetime import datetime


# Base model containing common fields for todos
class TodoBase(BaseModel):
    title: str
    description: str | None = None
    completed: bool = False


# Model for creating a new todo_ (inherits from TodoBase)
class TodoCreate(TodoBase):
    pass


# Model for updating an existing _todo (all fields are optional)
class TodoUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    completed: bool | None = None


# Model for returning a _todo in API responses
class TodoResponse(TodoBase):
    id: int
    created_at: datetime
    updated_at: datetime





