from typing import Optional

from pydantic import BaseModel

from .external_docs import ExternalDocs
from .request_body import RequestBody
from .response import Response


class Operation(BaseModel):
    tags: list[str]
    summary: str
    description: str
    externalDocs: Optional[ExternalDocs] = None
    operationId: Optional[str] = None
    requestBody: Optional[RequestBody] = None
    responses: dict[str, Response]
