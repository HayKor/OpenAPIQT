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
    externalDocs: Optional[ExternalDocs] = None
    servers: Optional[list[Server]] = None
    tags: Optional[list[Tag]] = None
    paths: dict[str, Path]
    components: Optional[Components] = None
    security: Optional[list[dict[str, list[str]]]] = None
    securitySchemes: Optional[dict[str, dict[str, Any]]] = None
