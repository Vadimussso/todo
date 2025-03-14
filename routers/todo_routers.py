from fastapi import APIRouter
from typing import Protocol
from schemas.todos import TodoCreate, TodoUpdate


router = APIRouter()


class TodoServiceProtocol(Protocol):
    def create_todo(self, todo: TodoCreate):
        pass

    def get_todos(self):
        pass

    def update_todo(self, todo_id: TodoUpdate):
        pass

    def delete_todo(self, todo_id: int):
        pass


@router.get("/todos")
async def get_todos(todo_service: TodoServiceProtocol = Depends(TodoService)):
    pass
