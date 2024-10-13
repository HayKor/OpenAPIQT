from typing import Any, Optional

from pydantic import BaseModel, Field


class MediaType(BaseModel):
    schema_: Optional[dict[str, str]] = Field(default=None, alias="schema")
    example: Optional[Any] = None
    examples: Optional[dict[str, dict[str, Any]]] = None
    encoding: Optional[dict[str, dict[str, Any]]] = None
