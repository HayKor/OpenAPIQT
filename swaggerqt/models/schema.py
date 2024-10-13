from typing import Any, Optional

from pydantic import BaseModel


class Schema(BaseModel):
    type: Optional[str] = None
    format: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    default: Optional[Any] = None
    required: Optional[list[str]] = None
    properties: Optional[dict[str, "Schema"]] = None

    multipleOf: Optional[float] = None
    maximum: Optional[float] = None
    exclusiveMaximum: Optional[bool] = None
    minimum: Optional[float] = None
    exclusiveMinimum: Optional[bool] = None
    maxLength: Optional[int] = None
    minLength: Optional[int] = None
    pattern: Optional[str] = None
    maxItems: Optional[int] = None
    minItems: Optional[int] = None
    uniqueItems: Optional[bool] = None
    maxProperties: Optional[int] = None
    minProperties: Optional[int] = None
