import flask
import flask_login
from app import app
import db
import utility
import response as r
from munch import DefaultMunch


@app.route('/profile/edit', methods=['GET', 'POST'])
@flask_login.login_required
def profile_edit():
    if flask.request.method == 'POST':
        user = db.get_user(flask_login.current_user.id)
        # creates object from dictionary
        user_form = DefaultMunch.fromDict(flask.request.form)

        if user is None:
            flask.flash(r.USER_NOT_FOUND, r.ERROR)
            return utility.render_with_permissions('login.html')

        if user.password == flask.request.form['password']:
            # check conflict with email
            conflict_users = db.get_users(email=flask.request.form.get('email'))
            if len(conflict_users) > 1:
                flask.flash(r.NOT_UNIQUE_EMAIL, r.ERROR)
                return utility.render_with_permissions('profile_edit.html', user=user_form)

            if len(conflict_users) == 1 and conflict_users[0] != user:
                flask.flash(r.NOT_UNIQUE_EMAIL, r.ERROR)
                return utility.render_with_permissions('profile_edit.html', user=user_form)

            # input to db
            user.email = user_form.email
            user.name = user_form.name
            user.surname = user_form.surname
            user.address = user_form.address
            user.tel_number = user_form.tel_number
            user.password = user_form.password
            db.db.session.add(user)
            db.db.session.commit()

            flask.flash(r.PROFILE_EDITED, r.OK)
            return flask.redirect('/profile')
        else:
            flask.flash(r.WRONG_PASSWORD, r.ERROR)
            return utility.render_with_permissions('profile_edit.html', user=user_form)
    return utility.render_with_permissions('profile_edit.html', user=flask_login.current_user)


@app.route('/profile/password', methods=['GET', 'POST'])
@flask_login.login_required
def profile_password():
    if flask.request.method == 'POST':
        user = db.get_user(flask_login.current_user.id)
        if user is None:
            flask.flash(r.USER_NOT_FOUND, r.ERROR)
            return utility.render_with_permissions('login.html')
        user.password = flask.request.form['password']
        db.db.session.add(user)
        db.db.session.commit()
        flask.flash(r.PASSWORD_CHANGED, r.OK)
        return flask.redirect('/profile')
    return utility.render_with_permissions('profile_password.html')


@app.route('/profile')
@flask_login.login_required
def profile():
    return utility.render_with_permissions('profile.html', user_info=flask_login.current_user.get_info())
