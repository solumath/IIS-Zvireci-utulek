import flask
import flask_login
from app import app
from functools import wraps
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
                return flask.render_template('401.html')
        return wrapper
    return decorator


@app.route('/')
def index():
    return flask.render_template('index.html')


@app.route('/animals')
def animals():
    return flask.render_template('animals.html')


@app.route('/about')
def about():
    return flask.render_template('about.html')


@app.route('/walks')
@flask_login.login_required
def walks():
    return flask.render_template('walks.html')


@app.route('/examinations')
@flask_login.login_required
@role_required(['administrator', 'vet'])
def examinations():
    return flask.render_template('examinations.html')


@app.route('/admin')
@flask_login.login_required
@role_required(['administrator'])
def admin():
    return flask.render_template('admin.html')

@app.route('/profile')
@flask_login.login_required
def profile():
    return flask.render_template('profile.html', user_info=flask_login.current_user.get_info())


@app.errorhandler(401)
def not_enough_perms(e):
    return flask.render_template('401.html')


@app.errorhandler(404)
def not_enough_perms(e):
    return flask.render_template('404.html')
