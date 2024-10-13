from typing import Optional

from pydantic import BaseModel

from .media_type import MediaType


class RequestBody(BaseModel):
    description: Optional[str]
    content: dict[str, MediaType]
    required: Optional[bool]
