from typing import Optional

from pydantic import BaseModel, Field


class Path(BaseModel):
    tags: list[str]
    api_path: str = Field(min_length=1)
    http_method: str = Field(min_length=1)
    request_schema: Optional[str] = None
    response_schema: Optional[str] = None

    def __repr__(self) -> str:
        return f"{self.http_method} {self.api_path}"
