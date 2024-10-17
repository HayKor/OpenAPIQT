from typing import Any, Optional

from pydantic import BaseModel

from .request_body import RequestBody
from .response import Response


class Components(BaseModel):
    schemas: Optional[dict[str, Any]] = None
    responses: Optional[dict[str, Response]] = None
    parameters: Optional[dict[str, dict[str, Any]]] = None
    examples: Optional[dict[str, dict[str, Any]]] = None
    requestBodies: Optional[dict[str, RequestBody]] = None
    headers: Optional[dict[str, dict[str, Any]]] = None
    securitySchemes: Optional[dict[str, dict[str, Any]]] = None
