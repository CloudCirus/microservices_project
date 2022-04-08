from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Issue:
    action: str
    created_at: datetime = datetime.now()
    user_id: Optional[int] = None
    book_id: Optional[int] = None
    id: Optional[int] = None
