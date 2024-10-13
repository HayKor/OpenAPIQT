from typing import Any, Optional

from pydantic import BaseModel

from .components import Components
from .external_docs import ExternalDocs
from .info import Info
from .paths import Path
from .server import Server
from .tags import Tag


class OpenAPI(BaseModel):
    openapi: str
    info: Info
    externalDocs: Optional[ExternalDocs]
    servers: Optional[list[Server]]
    tags: Optional[list[Tag]]
    paths: dict[str, Path]
    components: Optional[Components]
    security: Optional[list[dict[str, list[str]]]]
    securitySchemes: Optional[dict[str, dict[str, Any]]]
