from abc import ABC, abstractmethod
from typing import List, Optional

from book.application.dataclasses import Book


class BookRepoI(ABC):

    @abstractmethod
    def get_by_id(self, id_: int) -> Optional[Book]:
        ...

    @abstractmethod
    def get_all_by_title(self, title: str) -> Optional[List[Book]]:
        ...

    @abstractmethod
    def get_all(self) -> Optional[List[Book]]:
        ...

    @abstractmethod
    def create(self, book: Book) -> Book:
        ...

    @abstractmethod
    def delete(self, id_: int) -> Book:
        ...

    @abstractmethod
    def switch_status(self, book: Book) -> Book:
        ...
