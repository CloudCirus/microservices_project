from classic.app.errors import AppError


class NoBookId(AppError):
    msg_template = "No issues with title '{id}'"
    code = "issue.no_book_id"


class NoUserId(AppError):
    msg_template = "No issue with user id '{id}'"
    code = "issue.no_user_id"


class NoIssues(AppError):
    msg_template = "No issues in database"
    code = "issue.no_issues"


class NoAction(AppError):
    msg_template = "No action '{act}' in database"
    code = "issue.no_action"


class UnexpectedSearchValue(AppError):
    msg_template = "Search value can be integer or string equal title"
    code = "issue.search_value"
