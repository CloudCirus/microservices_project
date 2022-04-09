from typing import List, Optional, Union

from sqlalchemy import select

from classic.components import component
from classic.sql_storage import BaseRepository

from issue.application.dataclasses import Issue
from issue.application.interfaces import IssueRepoI


@component
class IssueRepo(BaseRepository, IssueRepoI):

    def get_by_user_id(self, id_: int) -> Optional[Union[List[Issue], Issue]]:
        query = select(Issue).where(Issue.user_id == id_)
        return self.session.execute(query).scalars().all()

    def get_by_book_id(self, id_: int) -> Optional[Union[List[Issue], Issue]]:
        query = select(Issue).where(Issue.book_id == id_)
        return self.session.execute(query).scalars().all()

    def get_by_action(self, act: str) -> Optional[Union[List[Issue], Issue]]:
        query = select(Issue).where(Issue.action == act)
        return self.session.execute(query).scalars().all()

    def get_all(self) -> Optional[Union[List[Issue], Issue]]:
        return self.session.query(Issue).all()

    def create(self, issue: Issue) -> Issue:
        self.session.add(issue)
        self.session.flush()
        self.session.refresh(issue)
        return issue
