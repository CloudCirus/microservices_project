from dataclasses import dataclass
from typing import Optional


@dataclass
class Book:
    title: str
    author: str
    genre: str
    status: bool = True
    id: Optional[int] = None
