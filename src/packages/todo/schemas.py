from pydantic import BaseModel


class TodoSchema(BaseModel):
    id: int | None = None
    title: str
    description: str | None = None

    class Config:
        orm_mode = True
