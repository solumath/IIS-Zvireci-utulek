from functools import wraps
import inspect
from textwrap import wrap
import db
from app import app
import flask
from flask_cors import cross_origin
import response as r


@cross_origin
@app.route('/login', methods=['POST'])
def login():
    json = flask.request.json

    # check if needed data was sent
    if "login" not in json or "password" not in json:
        return r.generate_response(r.MISSING_USERNAME_OR_PASSWORD, r.STAUTS_BAD_REQUEST)
    login = json["login"]
    password = json["password"]

    # user lookup
    user = db.db.session.query(db.User).filter(db.User.login == login).first()

    # checking username and password
    if user is None or user.password != password:
        return r.generate_response(r.WRONG_USERNAME_OR_PASSWORD, r.STATUS_FORBIDDEN)

    # deleting old session
    if user.session is not None:
        print("deleting session:", user.session)
        db.db.session.delete(user.session)

    # creating new session
    session = db.Session(user)
    print("creating session", session)
    db.db.session.add(session)
    db.db.session.commit()

    # creating response
    resp = r.generate_OK()
    resp.set_cookie("token", session.token, expires=session.expire)

    return resp


def authtenticate(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        cookies = flask.request.cookies

        # checking for token in cookies
        if "token" not in cookies:
            return r.generate_response(r.AUTHENTICATION_FAILED, r.STAUTS_BAD_REQUEST)
        token = cookies["token"]

        # searching session
        session = db.db.session.query(db.Session).filter(
            db.Session.token == token).first()

        # checking if session exists and is active
        if session is None or not session.is_active():
            # deleting expired session from db
            if session is not None:
                db.db.session.delete(session)
                db.db.session.commit()
            return r.generate_response(r.AUTHENTICATION_FAILED, r.STATUS_UNAUTHORIZED)

        # if needed passing user into wrapped function
        user = session.user
        if "user" in inspect.getargspec(func).args:
            print("passing user")
            kwargs["user"] = user

        return func(*args, **kwargs)
    return wrapper


@cross_origin
@app.route('/logout', methods=['GET'])
@authtenticate
def logout(user):
    print("deleting session:", user.session)

    # deleting session
    db.db.session.delete(user.session)
    db.db.session.commit()

    return r.generate_OK()


def authorize(user, event_type, action):
    # assuming authentification already passed
    permission = db.db.session.query(db.Permission).filter(
        db.Permission.user_role == user.user_role and db.Permission.event_type == event_type).first()

    return permission.has_permission(action)
