from typing import List, Optional

from sqlalchemy import select

from classic.components import component
from classic.sql_storage import BaseRepository

from user.application.dataclasses import User
from user.application.interfaces import UserRepoI


@component
class UserRepo(BaseRepository, UserRepoI):

    def get_by_id(self, id_: int) -> Optional[User]:
        query = select(User).where(User.id == id_)
        return self.session.execute(query).scalars().one_or_none()

    def get_all(self) -> Optional[List[User]]:
        return self.session.query(User).all()

    def create(self, user: User) -> User:
        self.session.add(user)
        self.session.flush()
        self.session.refresh(user)
        return user

    def delete(self, id_: int) -> User:
        user = self.session.query(User).get(id_)
        self.session.delete(user)
        self.session.flush()
        return user
