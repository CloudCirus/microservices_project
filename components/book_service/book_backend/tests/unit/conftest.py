from classic.messaging import Message, Publisher

from book.application import dataclasses, services

from unittest.mock import Mock

import pytest

from book.application import interfaces


@pytest.fixture(scope="function")
def book_repo(book_1, book_2):
    book_repo = Mock(interfaces.BookRepoI)
    book_repo.get_by_id = Mock(return_value=book_1)
    book_repo.get_all_by_title = Mock(return_value=[book_1, book_2])
    book_repo.get_all = Mock(return_value=[book_1, book_2])
    book_repo.create = Mock(return_value=book_1)
    book_repo.delete = Mock(return_value=book_1)
    book_repo.switch_status = Mock(return_value=book_1)
    return book_repo


@pytest.fixture(scope="function")
def publisher():
    publisher = Mock(Publisher)
    return publisher


@pytest.fixture(scope="function")
def book_1():
    return dataclasses.Book(
        id=1,
        title="test_title",
        author="test_author",
        genre="test_genre",
        status=True
    )


@pytest.fixture(scope="function")
def book_2():
    return dataclasses.Book(
        id=1,
        title="test_title",
        author="test_author",
        genre="test_genre",
        status=False
    )


@pytest.fixture(scope="function")
def book_info_1():
    return services.BookInfo(
        title="test_title_1",
        author="test_author_1",
        genre="test_genre_1"
    )


@pytest.fixture(scope="function")
def book_res_info():
    return services.BookReserveInfo(
        book_id=1,
        user_id=1

    )
