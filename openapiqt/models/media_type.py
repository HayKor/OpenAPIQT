from typing import Any, Optional

from pydantic import BaseModel, Field


class MediaType(BaseModel):
    schema_field: dict[str, Any] = Field(
        default=None, serialization_alias="schema"
    )
    example: Optional[Any] = None
    examples: Optional[dict[str, dict[str, Any]]] = None
    encoding: Optional[dict[str, dict[str, Any]]] = None
