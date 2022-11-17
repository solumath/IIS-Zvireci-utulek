import flask
import flask_login
from app import app


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


@app.route('/admin')
@flask_login.login_required
def admin():
    return flask.render_template('admin.html')

@app.route('/401')
def unauthorized():
    return flask.render_template('401.html')

@app.errorhandler(401)
def not_enough_perms(e):
    return flask.render_template('401.html')
