from typing import Optional

from pydantic import BaseModel

from .media_type import MediaType


class RequestBody(BaseModel):
    description: Optional[str] = None
    content: dict[str, MediaType]
    required: Optional[bool] = None
