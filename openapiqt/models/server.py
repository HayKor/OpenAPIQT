from typing import Optional

from pydantic import BaseModel


class Server(BaseModel):
    url: str
    description: Optional[str] = None
    variables: Optional[dict[str, dict[str, str]]] = None
