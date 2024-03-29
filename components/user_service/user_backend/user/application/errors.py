from classic.app.errors import AppError


class NoUser(AppError):
    msg_template = "No user with id '{id}'"
    code = 'user.no_user'


class NoUsers(AppError):
    msg_template = "No users in database"
    code = 'user.no_users'
