from unittest.mock import Mock

import pytest

from classic.messaging import Publisher
from user.application import dataclasses, interfaces, services


@pytest.fixture(scope="function")
def user_repo(user_1, user_2):
    user_repo = Mock(interfaces.UserRepoI)
    user_repo.get_by_id = Mock(return_value=user_1)
    user_repo.get_all = Mock(return_value=[user_1, user_2])
    user_repo.create = Mock(return_value=user_1)
    user_repo.delete = Mock(return_value=user_1)
    return user_repo


@pytest.fixture(scope="function")
def publisher():
    publisher = Mock(Publisher)
    return publisher


@pytest.fixture(scope="function")
def user_1():
    return dataclasses.User(
        name="test_name",
        surname="test_surname",
        email="test_email@mail.ru",
        status="test_status",
        id=1
    )


@pytest.fixture(scope="function")
def user_2():
    return dataclasses.User(
        name="test_name",
        surname="test_surname",
        email="test_email@mail.ru",
        status="test_status",
        id=2
    )


@pytest.fixture(scope="function")
def user_info_1():
    return services.UserInfo(
        name="test_name_upd",
        surname="test_surname_upd"
    )
