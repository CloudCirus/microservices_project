from dataclasses import asdict

from classic.components import component
from falcon import Request, Response

from book.application import services

from .join_points import join_point


@component
class Books:
    service: services.BookService

    @join_point
    def on_get_book(self, req: Request, resp: Response):
        book_id = req.params.get("id")
        book = self.service.get_by_id(book_id)
        resp.media = asdict(book)

    @join_point
    def on_get_all(self, req: Request, resp: Response):
        books = self.service.get_all()
        resp.media = [asdict(book) for book in books]

    @join_point
    def on_get_all_by_title(self, req, resp: Response):
        title = req.params.get("title")
        books = self.service.get_all_by_title(title)
        resp.media = sorted([asdict(book) for book in books], key=lambda x: "status")

    @join_point
    def on_get_delete_book(self, req: Request, resp: Response):
        book = req.params.get("id")
        deleted_book = self.service.delete(book)
        resp.media = asdict(deleted_book)

    @join_point
    def on_post_add_book(self, req: Request, resp: Response):
        book = self.service.create(**req.media)
        resp.media = asdict(book)

    @join_point
    def on_post_update_book(self, req: Request, resp: Response):
        book = self.service.update(**req.media)
        resp.media = asdict(book)

    @join_point
    def on_post_take_book(self, req: Request, resp: Response):
        book = self.service.take(**req.media)
        resp.media = asdict(book)

    @join_point
    def on_post_return_book(self, req: Request, resp: Response):
        book = self.service.give_back(**req.media)
        resp.media = asdict(book)
