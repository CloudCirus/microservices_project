from typing import List, Optional

from pydantic import validate_arguments

from classic.app import DTO, validate_with_dto
from classic.aspects import PointCut
from classic.components import component
from classic.messaging import Message, Publisher

from . import errors, interfaces
from .dataclasses import Book

join_points = PointCut()
join_point = join_points.join_point


class BookInfo(DTO):
    title: Optional[str]
    author: Optional[str]
    genre: Optional[str]
    id: Optional[int]


class BookReserveInfo(DTO):
    book_id: int
    user_id: int


@component
class BookService:
    book_repo: interfaces.BookRepoI
    publisher: Publisher

    def send_message(self, action: str, user_id: int = None, book_id: int = None) -> None:
        self.publisher.plan(
            Message(
                "create_issue",
                {"action": action, "user_id": user_id, "book_id": book_id}
            )
        )

    @join_point
    @validate_arguments
    def get_by_id(self, id_: int) -> Book:
        book = self.book_repo.get_by_id(id_)
        if book:
            return book
        raise errors.NoBookId(id=id_)

    @join_point
    @validate_arguments
    def get_all_by_title(self, title: str) -> List[Book]:
        books = self.book_repo.get_all_by_title(title)
        if books:
            return books
        raise errors.NoBookTitle(title=title)

    @join_point
    def get_all(self) -> List[Book]:
        books = self.book_repo.get_all()
        if books:
            return books
        raise errors.NoBooks()

    @join_point
    @validate_with_dto
    def create(self, book_info: BookInfo) -> Book:
        book = book_info.create_obj(Book)
        book_created = self.book_repo.create(book)
        self.send_message("book_create", book_id=book_created.id)
        return book_created

    @join_point
    @validate_with_dto
    def update(self, book_info: BookInfo) -> Book:
        book = self.get_by_id(book_info.id)
        book_info.populate_obj(book)
        book_updated = self.get_by_id(book.id)
        self.send_message("book_update", book_id=book_updated.id)
        return book_updated

    @join_point
    @validate_arguments
    def delete(self, id_: int) -> Book:
        self.get_by_id(id_)
        book_deleted = self.book_repo.delete(id_)
        self.send_message("book_delete", book_id=book_deleted.id)
        return book_deleted

    @join_point
    @validate_with_dto
    def take(self, reserve_info: BookReserveInfo) -> Book:
        book = self.get_by_id(reserve_info.book_id)
        if not book.status:
            raise errors.ActionProblem()
        if book:
            book_taken = self.book_repo.switch_status(book)
            self.send_message("book_reserve", reserve_info.user_id, book_id=book_taken.id)
            return book_taken
        raise errors.UnexpectedSearchValue()

    @join_point
    @validate_with_dto
    def give_back(self, reserve_info: BookReserveInfo) -> Book:
        book = self.get_by_id(reserve_info.book_id)
        if book.status:
            raise errors.ActionProblem()
        if book:
            book_returned = self.book_repo.switch_status(book)
            self.send_message("book_return", reserve_info.user_id, book_id=book_returned.id)
            return book_returned
        raise errors.UnexpectedSearchValue()
