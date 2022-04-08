from classic.messaging import Message, Publisher
from datetime import datetime

from issue.application import dataclasses, services

from unittest.mock import Mock

import pytest

from issue.application import interfaces


@pytest.fixture(scope="function")
def issue_repo(issue_1, issue_2):
    issue_repo = Mock(interfaces.IssueRepoI)
    issue_repo.get_by_user_id = Mock(return_value=issue_1)
    issue_repo.get_all = Mock(return_value=[issue_1, issue_2])
    issue_repo.create = Mock(return_value=issue_1)
    issue_repo.delete = Mock(return_value=issue_1)
    return issue_repo


@pytest.fixture(scope="function")
def publisher():
    publisher = Mock(Publisher)
    return publisher


@pytest.fixture(scope="function")
def issue_1():
    return dataclasses.Issue(
        action="test",
        created_at=datetime.now(),
        user_id=1,
        book_id=1,
        id=1
    )


@pytest.fixture(scope="function")
def issue_2():
    return dataclasses.Issue(
        action="test",
        created_at=datetime.now(),
        user_id=1,
        book_id=1,
        id=2
    )
