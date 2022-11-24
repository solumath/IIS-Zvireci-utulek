import flask_login
from app import app
import db
import utility


@app.route('/')
def index():
    return utility.render_with_permissions('index.html')


@app.route('/about')
def about():
    return utility.render_with_permissions('about.html')


@app.route('/profile')
@flask_login.login_required
def profile():
    return utility.render_with_permissions('profile.html', user_info=flask_login.current_user.get_info())


@app.errorhandler(401)
def not_enough_perms(e):
    return utility.render_with_permissions('401.html')


@app.errorhandler(404)
def page_not_found(e):
    return utility.render_with_permissions('404.html')
