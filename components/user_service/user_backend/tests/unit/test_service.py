from unittest.mock import Mock

import pytest

from user.application import errors
from user.application.services import UserService


@pytest.fixture(scope="function")
def service(user_repo, publisher):
    return UserService(user_repo=user_repo, publisher=publisher)


def test__get_by_id(service, user_repo, user_1):
    assert service.get_by_id(1) == user_1


def test__get_by_by_exception(service, user_repo):
    id_ = 1
    user_repo.get_by_id = Mock(return_value=None)
    with pytest.raises(errors.NoUser):
        service.get_by_id(id_)


def test__get_all(service, user_repo, user_1, user_2):
    assert service.get_all() == [user_1, user_2]


def test__get_all_exception(service, user_repo):
    user_repo.get_all = Mock(return_value=None)
    with pytest.raises(errors.NoUsers):
        service.get_all()


def test__create(service, user_repo, user_1):
    test_case = {
        "name": "test_name",
        "surname": "test_surname",
        "email": "test_email@mail.ru",
        "status": "test_status"
    }
    assert service.create(**test_case) == user_1


def test__update(service, user_repo, user_1):
    test_case = {
        "name": "test_name_upd",
        "surname": "test_surname_upd"
    }
    service.get_by_id = Mock(return_value=user_1)
    assert service.update(**test_case) == user_1


def test_delete(service, user_repo, user_1):
    id_ = 1
    service.get_by_id = Mock(return_value=user_1)
    assert service.delete(id_) == user_1
