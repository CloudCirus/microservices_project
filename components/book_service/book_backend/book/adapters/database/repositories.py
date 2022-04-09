from typing import List, Optional

from sqlalchemy import select

from classic.components import component
from classic.sql_storage import BaseRepository

from book.application.dataclasses import Book
from book.application.interfaces import BookRepoI


@component
class BookRepo(BaseRepository, BookRepoI):

    def get_by_id(self, id_: int) -> Optional[Book]:
        query = select(Book).where(Book.id == id_)
        return self.session.execute(query).scalars().one_or_none()

    def get_all_by_title(self, title: str) -> Optional[Book]:
        book = self.session.query(Book).filter(Book.title == title).all()
        return book if book else None

    def get_all(self) -> Optional[List[Book]]:
        return self.session.query(Book).all()

    def create(self, book: Book) -> Book:
        self.session.add(book)
        self.session.flush()
        self.session.refresh(book)
        return book

    def delete(self, id_: int) -> Book:
        book = self.session.query(Book).get(id_)
        self.session.delete(book)
        self.session.flush()
        return book

    def switch_status(self, book: Book) -> Book:
        book = self.session.query(Book).get(book.id)
        book.status = False if book.status else True
        self.session.flush()
        self.session.refresh(book)
        return book
