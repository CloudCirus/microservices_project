from dataclasses import asdict
from typing import List, Union

from falcon import Request, Response

from classic.components import component

from issue.application import services
from issue.application.dataclasses import Issue
from .join_points import join_point


@component
class Issues:
    service: services.IssueService

    @staticmethod
    def convert_for_response(issue_or_issues: Union[List[Issue], Issue]) -> Union[List[dict], dict]:
        if isinstance(issue_or_issues, list):
            response = []
            for issue_obj in issue_or_issues:
                issue_obj.created_at = issue_obj.created_at.strftime("%m.%d.%Y, %H:%M:%S")
                response.append(asdict(issue_obj))
        else:
            issue_or_issues.created_at = issue_or_issues.created_at.strftime("%m.%d.%Y, %H:%M:%S")
            response = asdict(issue_or_issues)
        return response

    @join_point
    def on_get_by_book_id(self, req: Request, resp: Response):
        book_id = req.params.get("id")
        issues = self.service.get_by_book_id(book_id)
        resp.media = self.convert_for_response(issues)

    @join_point
    def on_get_by_user_id(self, req: Request, resp: Response):
        user_id = req.params.get("id")
        issues = self.service.get_by_user_id(user_id)
        resp.media = self.convert_for_response(issues)

    @join_point
    def on_get_by_action(self, req: Request, resp: Response):
        act = req.params.get("act")
        issues = self.service.get_by_action(act)
        resp.media = self.convert_for_response(issues)

    @join_point
    def on_get_all(self, req, resp: Response):
        issues = self.service.get_all()
        resp.media = self.convert_for_response(issues)

    @join_point
    def on_post_create(self, req: Request, resp: Response):
        issue = self.service.create(**req.media)
        resp.media = self.convert_for_response(issue)
