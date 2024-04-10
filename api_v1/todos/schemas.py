from pydantic import BaseModel


class ToDoBase(BaseModel):
    title: str
    is_complete: bool = False


class ToDoCreate(ToDoBase):
    pass


class ToDoUpdate(ToDoCreate):
    pass


class ToDoPartialUpdate(ToDoCreate):
    title: str | None = None
    is_complete: bool = False | True


class ToDo(ToDoBase):
    id: int
