from typing import Optional

from pydantic import BaseModel

from .external_docs import ExternalDocs
from .request_body import RequestBody
from .response import Response


class Operation(BaseModel):
    tags: list[str]
    summary: str
    description: str
    externalDocs: Optional[ExternalDocs]
    operationId: Optional[str]
    requestBody: Optional[RequestBody]
    responses: dict[str, Response]
