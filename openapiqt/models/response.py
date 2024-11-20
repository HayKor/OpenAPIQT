from typing import Any, Optional

from pydantic import BaseModel


class Response(BaseModel):
    description: str
    content: dict[str, Any]
    headers: Optional[dict[str, dict[str, Any]]] = None
