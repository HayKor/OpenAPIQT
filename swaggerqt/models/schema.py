from typing import Any, Optional

from pydantic import BaseModel


class Schema(BaseModel):
    type: Optional[str]
    format: Optional[str]
    title: Optional[str]
    description: Optional[str]
    default: Optional[Any]
    required: Optional[list[str]]
    properties: Optional[dict[str, "Schema"]]

    multipleOf: Optional[float]
    maximum: Optional[float]
    exclusiveMaximum: Optional[bool]
    minimum: Optional[float]
    exclusiveMinimum: Optional[bool]
    maxLength: Optional[int]
    minLength: Optional[int]
    pattern: Optional[str]
    maxItems: Optional[int]
    minItems: Optional[int]
    uniqueItems: Optional[bool]
    maxProperties: Optional[int]
    minProperties: Optional[int]
