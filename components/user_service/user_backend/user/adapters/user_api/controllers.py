from dataclasses import asdict

from classic.components import component
from falcon import Request, Response

from user.application import services

from .join_points import join_point


@component
class Users:
    service: services.UserService

    @join_point
    def on_get_user(self, req: Request, resp: Response):
        user_id = req.params.get("id")
        user = self.service.get_by_id(user_id)
        resp.media = asdict(user)

    @join_point
    def on_get_all_users(self, req, resp: Response):
        users = self.service.get_all()
        resp.media = [asdict(user) for user in users]

    @join_point
    def on_get_delete_user(self, req: Request, resp: Response):
        user_id = req.params.get("id")
        deleted_user = self.service.delete(user_id)
        resp.media = asdict(deleted_user)

    @join_point
    def on_post_add_user(self, req: Request, resp: Response):
        user = self.service.create(**req.media)
        resp.media = asdict(user)

    @join_point
    def on_post_update_user(self, req: Request, resp: Response):
        user = self.service.update(**req.media)
        resp.media = asdict(user)
