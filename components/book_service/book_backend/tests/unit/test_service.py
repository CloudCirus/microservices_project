import pytest

from book.application.services import BookService
from book.application import errors
from unittest.mock import Mock


@pytest.fixture(scope="function")
def service(book_repo, publisher):
    return BookService(book_repo=book_repo, publisher=publisher)


def test__get_by_id(service, book_repo, book_1):
    assert service.get_by_id(1) == book_1


def test__get_by_by_exception(service, book_repo):
    ...


def test__get_all_by_title(service, book_repo, book_1, book_2):
    assert service.get_all_by_title("test_title") == [book_1, book_2]


def test__get_all(service, book_repo, book_1, book_2):
    assert service.get_all() == [book_1, book_2]


def test__get_all_exception(service, book_repo):
    book_repo.get_all = Mock(return_value=None)
    with pytest.raises(errors.NoBooks):
        service.get_all()


def test__create(service, book_repo, book_1):
    test_case = {
        "title": "test_title",
        "author": "test_author",
        "genre": "test_genre"
    }
    assert service.create(**test_case) == book_1


def test__update(service, book_repo, book_1):
    test_case = {
        "title": "test_title",
        "author": "test_author",
        "genre": "test_genre"
    }
    service.get_by_id = Mock(return_value=book_1)
    assert service.update(**test_case) == book_1


def test_delete(service, book_repo, book_1):
    id_ = 1
    service.get_by_id = Mock(return_value=book_1)
    assert service.delete(id_) == book_1

def test__take(service, book_repo, book_1):
    test_case = {
        "user_id": 1,
        "book_id": 1
    }
    service.get_by_id = Mock(return_value=book_1)
    assert service.take(**test_case) == book_1


def test_give_back(service, book_repo, book_1, book_2):
    test_case = {
        "user_id": 1,
        "book_id": 1
    }
    book_repo.get_by_id = Mock(return_value=book_2)
    service.get_by_id = Mock(return_value=book_2)
    assert service.give_back(**test_case) == book_1

#
#
# def give_back(self, reserve_info: BookReserveInfo) -> Book:
#     book = self.get_by_id(reserve_info.book_id)
#     if book.status:
#         raise errors.ActionProblem()
#     if book:
#         book_returned = self.book_repo.switch_status(book)
#         self.send_message("book_return", reserve_info.user_id, book_returned.id)
#         return book_returned
#     raise errors.UnexpectedSearchValue()
