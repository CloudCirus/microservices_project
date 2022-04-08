from dataclasses import dataclass
from typing import Optional


@dataclass
class User:
    name: str
    surname: str
    email: str
    status: str
    id: Optional[int] = None
