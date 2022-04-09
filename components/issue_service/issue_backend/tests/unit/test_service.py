from unittest.mock import Mock

import pytest

from issue.application import errors
from issue.application.services import IssueService


@pytest.fixture(scope="function")
def service(issue_repo):
    return IssueService(issue_repo=issue_repo)


def test__get_by_user_id(service, issue_repo, issue_1):
    assert service.get_by_user_id(1) == issue_1


def test__get_by_by_exception(service, issue_repo):
    id_ = 1
    issue_repo.get_by_user_id = Mock(return_value=None)
    with pytest.raises(errors.NoUserId):
        service.get_by_user_id(id_)


def test__get_all(service, issue_repo, issue_1, issue_2):
    assert service.get_all() == [issue_1, issue_2]


def test__get_all_exception(service, issue_repo):
    issue_repo.get_all = Mock(return_value=None)
    with pytest.raises(errors.NoIssues):
        service.get_all()


def test__create(service, issue_repo, issue_1):
    test_case = {
        "action": "test",
        "user_id": 1,
        "book_id": 1
    }
    assert service.create(**test_case) == issue_1


def test__create_issue_from_rabbitmq(service, issue_repo, issue_1):
    test_case = {
        "action": "test",
        "user_id": 1,
        "book_id": 1
    }
    assert service.create_issue_from_rabbitmq(**test_case) is None
