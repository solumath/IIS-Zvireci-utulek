from functools import wraps
import flask_login
import flask
import db


def role_required(roles):
    """
    Decorator for checking if user has required role.
    accepts multiple roles in list.
    """
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            for role in roles:
                if flask_login.current_user.user_role.name == role:
                    return f(*args, **kwargs)
            else:
                return render_with_permissions('401.html')
        return wrapper
    return decorator


def render_with_permissions(*args, **kwargs):
    perms_dict = {
        db.PERMISSION_ANIMALS_SHOW: "PERMISSION_ANIMALS_SHOW",
        db.PERMISSION_ANIMALS_DELETE: "PERMISSION_ANIMALS_DELETE",
        db.PERMISSION_ANIMALS_EDIT: "PERMISSION_ANIMALS_EDIT",
        db.PERMISSION_ANIMALS_ADD: "PERMISSION_ANIMALS_ADD",

        db.PERMISSION_USERS_SHOW: "PERMISSION_USERS_SHOW",
        db.PERMISSION_USERS_EDIT: "PERMISSION_USERS_EDIT",
        db.PERMISSION_USERS_VERIFY: "PERMISSION_USERS_VERIFY",
        db.PERMISSION_USERS_ADD: "PERMISSION_USERS_ADD",
        db.PERMISSION_USERS_DELETE: "PERMISSION_USERS_DELETE",

        db.PERMISSION_WALKS_SHOW: "PERMISSION_WALKS_SHOW",
        db.PERMISSION_WALKS_ADD: "PERMISSION_WALKS_ADD",
        db.PERMISSION_WALKS_DELETE: "PERMISSION_WALKS_DELETE",
        db.PERMISSION_WALKS_CONFIRM: "PERMISSION_WALKS_CONFIRM",

        db.PERMISSION_MY_WALKS_SHOW: "PERMISSION_MY_WALKS_SHOW",
        db.PERMISSION_MY_WALKS_ADD: "PERMISSION_MY_WALKS_ADD",
        db.PERMISSION_MY_WALKS_DELETE: "PERMISSION_MY_WALKS_DELETE",

        db.PERMISSION_EXAMINATIONS_SHOW: "PERMISSION_EXAMINATIONS_SHOW",
        db.PERMISSION_MY_EXAMINATIONS_SHOW: "PERMISSION_MY_EXAMINATIONS_SHOW",
        db.PERMISSION_EXAMINATIONS_ADD: "PERMISSION_EXAMINATIONS_ADD",
        db.PERMISSION_EXAMINATIONS_EDIT: "PERMISSION_EXAMINATIONS_EDIT",
        db.PERMISSION_EXAMINATIONS_DELETE: "PERMISSION_EXAMINATIONS_DELETE",
        db.PERMISSION_EXAMINATIONS_PERFORM: "PERMISSION_EXAMINATIONS_PERFORM",
        db.PERMISSION_EXAMINATIONS_REQUEST: "PERMISSION_EXAMINATIONS_REQUEST",
        db.PERMISSION_EXAMINATIONS_ACCEPT: "PERMISSION_EXAMINATIONS_ACCEPT",
    }

    # permissions = {x: False for x in perms_dict.values()}
    permissions = {}

    if flask_login.current_user.is_authenticated:
        user_perms = flask_login.current_user.user_role.permissions
    else:
        user_perms = db.db.session.query(db.UserRole).filter(
            db.UserRole.name == "unverified").first().permissions

    for perm in user_perms:
        perm_name = perms_dict.get(perm.action)
        if perm_name is None:
            raise ValueError("Unexpected permission value")
        permissions[perm_name] = True

    kwargs.update(permissions)

    return flask.render_template(*args, **kwargs)
