import flask_login
import flask
from app import app
import db
from flask_cors import cross_origin
import response as r
import utility


login_manager = flask_login.LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def user_loader(user_id):
    """Given *user_id*, return the associated User object.

    :param unicode user_id: user_id (login) user to retrieve

    """
    return db.db.session.query(db.User).filter(
        db.User.login == user_id).first()


def register_form(form):
    # check if needed data was sent
    needed_fields = {"login", "password", "name",
                     "surname", "address", "email", "tel_number"}
    data = {}
    for field in needed_fields:
        if field not in form:
            flask.flash(r.MISSING_FIELD, r.ERROR)
            return utility.render_with_permissions("login.html")
        data[field] = form[field]

    # user lookup
    login = form["login"].lower()
    user_login = db.db.session.query(db.User).filter(db.User.login == login).first()

    if user_login is not None:
        flask.flash(r.USER_ALREADY_EXISTS, r.ERROR)
        return utility.render_with_permissions('login.html')

    email = form["email"]
    user_email = db.db.session.query(db.User).filter(db.User.email == email).first()
    if user_email is not None:
        flask.flash(r.USER_ALREADY_EXISTS, r.ERROR)
        return utility.render_with_permissions('login.html')

    # create user and insert to db
    data['login'] = data['login'].lower()
    new_user = db.User(**data)
    db.db.session.add(new_user)
    new_user.user_role = db.get_user_role("unverified")
    db.db.session.commit()

    flask.flash(r.REGISTER_SUCCESS, r.OK)
    return utility.render_with_permissions("login.html")


def login_form(form):
    login = form['login'].lower()
    password = form['password']

    user = db.db.session.query(db.User).filter(
        db.User.login == login).first()
    if user:
        if user.password == password:
            user.authenticated = True
            db.db.session.add(user)
            db.db.session.commit()
            flask_login.login_user(user, remember=True)

            flask.flash(r.LOGIN_SUCCESS, r.OK)
            return utility.render_with_permissions("index.html")

    flask.flash(r.WRONG_LOGIN_OR_PASSWORD, r.ERROR)
    return utility.render_with_permissions("login.html")


@cross_origin
@app.route("/login", methods=["GET", "POST"])
def login():
    """For GET requests, display the login form. 
    For POSTS, login the current user by processing the form.

    """
    if flask.request.method == 'POST':
        if 'loginSubmit' in flask.request.form:
            return login_form(flask.request.form)
        if 'registerSubmit' in flask.request.form:
            return register_form(flask.request.form)

        flask.flash(r.STATUS_BAD_REQUEST, "Bez dopice")
        return utility.render_with_permissions("login.html")

    return utility.render_with_permissions("login.html")


@cross_origin
@app.route("/logout", methods=["GET"])
@flask_login.login_required
def logout():
    """Logout the current user."""
    user = flask_login.current_user
    user.authenticated = False
    db.db.session.add(user)
    db.db.session.commit()
    flask_login.logout_user()
    flask.flash(r.LOGOUT_SUCCESS, r.OK)
    return utility.render_with_permissions("index.html")
