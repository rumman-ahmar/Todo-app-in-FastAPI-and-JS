from pydantic import BaseModel


class ItemSchema(BaseModel):
    task: str
