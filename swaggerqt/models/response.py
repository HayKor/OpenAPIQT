from typing import Any, Optional

from pydantic import BaseModel

from .media_type import MediaType


class Response(BaseModel):
    description: str
    content: dict[str, MediaType]
    headers: Optional[dict[str, dict[str, Any]]]
