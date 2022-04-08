from classic.app.errors import AppError


class NoBookTitle(AppError):
    msg_template = "No book with title '{title}'"
    code = "book.no_book_title"


class NoBookId(AppError):
    msg_template = "No book with id '{id}'"
    code = "book.no_book_id"


class NoBooks(AppError):
    msg_template = "No books in database"
    code = "book.no_books"


class ActionProblem(AppError):
    msg_template = "Book status is invalid for with action"
    code = "book.action_invalid"


class UnexpectedSearchValue(AppError):
    msg_template = "Search value can be integer or string equal title"
    code = "book.search_value"
