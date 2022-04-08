from abc import ABC, abstractmethod
from typing import List, Optional

from user.application.dataclasses import User


class UserRepoI(ABC):

    @abstractmethod
    def get_by_id(self, id_: int) -> Optional[User]:
        ...

    @abstractmethod
    def get_all(self) -> Optional[List[User]]:
        ...

    @abstractmethod
    def create(self, user: User) -> User:
        ...

    @abstractmethod
    def delete(self, id_: int) -> User:
        ...
