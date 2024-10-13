from typing import Any, Optional

from pydantic import BaseModel, Field


class MediaType(BaseModel):
    _schema: Optional[dict[str, str]] = Field(alias="schema")
    example: Optional[Any]
    examples: Optional[dict[str, dict[str, Any]]]
    encoding: Optional[dict[str, dict[str, Any]]]
