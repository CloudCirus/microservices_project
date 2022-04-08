from abc import ABC, abstractmethod
from typing import List, Optional, Union

from issue.application.dataclasses import Issue


class IssueRepoI(ABC):

    @abstractmethod
    def get_by_book_id(self, id_: int) -> Optional[Union[List[Issue], Issue]]:
        ...

    @abstractmethod
    def get_by_user_id(self, id_: int) -> Optional[Union[List[Issue], Issue]]:
        ...

    @abstractmethod
    def get_by_action(self, act: str) -> Optional[Union[List[Issue], Issue]]:
        ...

    @abstractmethod
    def get_all(self) -> Optional[Union[List[Issue], Issue]]:
        ...

    @abstractmethod
    def create(self, issue: Issue) -> Issue:
        ...
