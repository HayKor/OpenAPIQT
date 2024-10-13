from typing import Any, Optional

from pydantic import BaseModel, Field

from .schema import Schema


class MediaType(BaseModel):
    schema_field: Schema = Field(default=None, serialization_alias="schema")
    example: Optional[Any] = None
    examples: Optional[dict[str, dict[str, Any]]] = None
    encoding: Optional[dict[str, dict[str, Any]]] = None
