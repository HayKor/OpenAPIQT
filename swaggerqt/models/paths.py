from typing import Optional

from pydantic import BaseModel


class Path(BaseModel):
    tags: list[str]
    api_path: str
    http_method: str
    request_schema: Optional[str] = None
    response_schema: Optional[str] = None

    def __repr__(self) -> str:
        return f"{self.http_method} {self.api_path}"
