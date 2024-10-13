from typing import Any, Optional

from pydantic import BaseModel

from .request_body import RequestBody
from .response import Response
from .schema import Schema


class Components(BaseModel):
    schemas: Optional[dict[str, Schema]]
    responses: Optional[dict[str, Response]]
    parameters: Optional[dict[str, dict[str, Any]]]
    examples: Optional[dict[str, dict[str, Any]]]
    requestBodies: Optional[dict[str, RequestBody]]
    headers: Optional[dict[str, dict[str, Any]]]
    securitySchemes: Optional[dict[str, dict[str, Any]]]
