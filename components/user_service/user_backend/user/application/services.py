from typing import List, Optional
from pydantic import validate_arguments

from classic.app import DTO, validate_with_dto
from classic.aspects import PointCut
from classic.components import component
from classic.messaging import Message, Publisher

from . import errors, interfaces
from .dataclasses import User

join_points = PointCut()
join_point = join_points.join_point


class UserInfo(DTO):
    name: Optional[str]
    surname: Optional[str]
    email: Optional[str]
    status: Optional[str]
    id: Optional[int]


@component
class UserService:
    user_repo: interfaces.UserRepoI
    publisher: Publisher

    @join_point
    @validate_arguments
    def get_by_id(self, id_: int) -> User:
        user = self.user_repo.get_by_id(id_)
        if user:
            return user
        raise errors.NoUser(id=id_)

    @join_point
    def get_all(self) -> List[User]:
        users = self.user_repo.get_all()
        if users:
            return users
        raise errors.NoUsers()

    def send_message(self, action: str, user_id: int) -> None:
        self.publisher.plan(
            Message(
                "create_issue",
                {"action": action, "user_id": user_id}
            )
        )

    @join_point
    @validate_with_dto
    def create(self, user_info: UserInfo) -> User:
        user = user_info.create_obj(User)
        user_created: User = self.user_repo.create(user)
        self.send_message("user_create", user_created.id)
        return user_created

    @join_point
    @validate_with_dto
    def update(self, user_info: UserInfo) -> User:
        user = self.get_by_id(user_info.id)
        user_info.populate_obj(user)
        user_updated = self.get_by_id(user.id)
        self.send_message("user_update", user_updated.id)
        return user_updated

    @join_point
    @validate_arguments
    def delete(self, id_: int) -> User:
        self.get_by_id(id_)
        user_deleted = self.user_repo.delete(id_)
        self.send_message("user_delete", user_deleted.id)
        return user_deleted
