from sqlalchemy.orm import registry

from book.application.dataclasses import Book
from .tables import book_table

mapper = registry()

mapper.map_imperatively(Book, book_table)
