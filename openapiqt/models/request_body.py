from typing import Any, Optional

from pydantic import BaseModel


class RequestBody(BaseModel):
    description: Optional[str] = None
    content: dict[str, Any]
    required: Optional[bool] = None
