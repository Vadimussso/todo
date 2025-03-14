from typing import Protocol
from schemas.todos import TodoCreate


class TodoRepoProtocol(Protocol):
    async def get_todos(self):
        pass