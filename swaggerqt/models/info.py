from pydantic import BaseModel


class Info(BaseModel):
    title: str
    version: str
    description: str
