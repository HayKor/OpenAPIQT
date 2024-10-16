from typing import Any, Optional

from pydantic import BaseModel
from typing_extensions import deprecated


@deprecated("Common `model.model_json_schema()` converted to dict is used")
class Schema(BaseModel):
    type: Optional[str] = None
    format: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    default: Optional[Any] = None
    required: Optional[list[str]] = None
    properties: Optional[dict[str, "Schema"]] = None
    items: Optional["Schema"] | Optional[list["Schema"]] = None
