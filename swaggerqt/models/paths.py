from typing import Optional

from pydantic import BaseModel

from .operation import Operation


class Path(BaseModel):
    put: Optional[Operation]
    post: Optional[Operation]
    get: Optional[Operation]
    delete: Optional[Operation]
    patch: Optional[Operation]
