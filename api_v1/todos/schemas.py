import json

from pydantic import BaseModel, model_validator
from fastapi import Form, Path
from typing import Annotated, Any


class ToDoBase(BaseModel):
    title: str
    is_complete: bool = False

    # def __hash__(self):
    #     return hash(self.title)

    # @model_validator(mode="before")
    # @classmethod
    # def validate_to_json(cls, value: Any) -> Any:
    #     print(value)
    #     if isinstance(value, str):
    #         return cls(**json.loads(value))
    #     return value


class ToDoCreate(ToDoBase):
    pass


class ToDoUpdate(ToDoCreate):
    pass


class ToDoPartialUpdate(ToDoCreate):
    title: str | None = None
    is_complete: bool = False | True


class ToDo(ToDoBase):
    id: int
