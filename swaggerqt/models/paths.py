from typing import Optional

from pydantic import BaseModel

from .operation import Operation


class Path(BaseModel):
    put: Optional[Operation] = None
    post: Optional[Operation] = None
    get: Optional[Operation] = None
    delete: Optional[Operation] = None
    patch: Optional[Operation] = None
