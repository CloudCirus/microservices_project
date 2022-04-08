from typing import List, Optional, Union
from datetime import datetime
from pydantic import validate_arguments

from classic.app import DTO, validate_with_dto
from classic.aspects import PointCut
from classic.components import component

from . import errors, interfaces
from .dataclasses import Issue

join_points = PointCut()
join_point = join_points.join_point


class IssueInfo(DTO):
    action: Optional[str]
    user_id: Optional[int]
    book_id: Optional[int]
    created_ad: Optional[datetime]
    id: Optional[int]


@component
class IssueService:
    issue_repo: interfaces.IssueRepoI

    @join_point
    @validate_arguments
    def get_by_user_id(self, id_: int) -> Union[List[Issue], Issue]:
        issues = self.issue_repo.get_by_user_id(id_)
        if issues:
            return issues
        raise errors.NoUserId(id=id_)

    @join_point
    @validate_arguments
    def get_by_book_id(self, id_: int) -> Union[List[Issue], Issue]:
        issues = self.issue_repo.get_by_book_id(id_)
        if issues:
            return issues
        raise errors.NoBookId(id=id_)

    @join_point
    @validate_arguments
    def get_by_action(self, act: str) -> Union[List[Issue], Issue]:
        issues = self.issue_repo.get_by_action(act)
        if issues:
            return issues
        raise errors.NoAction(act=act)

    @join_point
    def get_all(self) -> Union[List[Issue], Issue]:
        issues = self.issue_repo.get_all()
        if issues:
            return issues
        raise errors.NoIssues()

    @join_point
    @validate_with_dto
    def create(self, issue_info: IssueInfo) -> Issue:
        issue = issue_info.create_obj(Issue)
        created = self.issue_repo.create(issue)
        return created

    @join_point
    @validate_arguments
    def create_issue_from_rabbitmq(self,
                                   action: str,
                                   user_id: int = None,
                                   book_id: int = None
                                   ) -> None:
        print(action, user_id)
        issue = Issue(action=action, user_id=user_id, book_id=book_id)
        self.issue_repo.create(issue)
