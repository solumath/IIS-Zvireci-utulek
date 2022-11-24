import flask
import flask_login
from app import app
import db
import utility
import response as r


@app.route('/users/delete', methods=['GET', 'POST'])
@flask_login.login_required
@utility.role_required(['administrator'])
def users_delete():
    if flask.request.method == 'POST':
        if int(flask.request.form['id']) == flask_login.current_user.id:
            flask.flash(r.DELETE_YOURSELF_FAILED, r.ERROR)
            return utility.render_with_permissions(flask.url_for('users'))

        user = db.get_user(flask.request.form['id'])
        if user is None:
            flask.flash(r.USER_NOT_FOUND, r.ERROR)
            return utility.render_with_permissions(flask.url_for('users'))

        for event in db.get_future_events(user):
            db.db.session.delete(event)

        db.db.session.delete(user)
        db.db.session.commit()

    return flask.redirect(flask.url_for('users'))


@app.route('/users/edit/<id>', methods=['GET', 'POST'])
@flask_login.login_required
@utility.role_required(['administrator'])
def users_edit(id):
    if flask.request.method == "POST":
        user = db.get_user(id)
        if user is None:
            flask.flash(r.USER_NOT_FOUND, r.ERROR)
            return utility.render_with_permissions(flask.url_for('users'))

        id = user.id
        user.name = flask.request.form.get('name')
        user.surname = flask.request.form.get('surname')
        user.address = flask.request.form.get('address')
        user.tel_number = flask.request.form.get('tel_number')

        role_name = flask.request.form.get('user_role')

        user.user_role = db.get_user_role(role_name)
        db.db.session.add(user)
        db.db.session.commit()
        return flask.redirect(flask.url_for('users'))

    return utility.render_with_permissions('user_edit.html',
                                           user=db.get_user(id),
                                           user_roles=db.get_user_roles())


@app.route('/users/add', methods=['POST', 'GET'])
@flask_login.login_required
@utility.role_required(['administrator'])
def user_add():
    if flask.request.method == "POST":
        login = flask.request.form.get("login")
        user_login = db.db.session.query(db.User).filter(
            db.User.login == login).first()
        # login conflict
        if user_login is not None:
            flask.flash(r.NOT_UNIQUE_LOGIN, r.ERROR)
            return utility.render_with_permissions('user_add.html', roles=db.get_user_roles())

        password = flask.request.form.get("password")
        email = flask.request.form.get("email")
        user_email = db.db.session.query(db.User).filter(
            db.User.email == email).first()
        # email conflict
        if user_email is not None:
            flask.flash(r.NOT_UNIQUE_EMAIL, r.ERROR)
            return utility.render_with_permissions('user_add.html', roles=db.get_user_roles())
        name = flask.request.form.get("name")
        surname = flask.request.form.get("surname")
        address = flask.request.form.get("address")
        tel_number = flask.request.form.get("tel_number")
        # TODO check tel. number

        role_name = flask.request.form.get("user_role")

        new_user = db.User(login, password,  name, surname,
                           address, email, tel_number)
        db.db.session.add(new_user)
        new_user.user_role = db.get_user_role(role_name)
        db.db.session.commit()
        return flask.redirect(flask.url_for('users'))
    return utility.render_with_permissions('user_add.html', roles=db.get_user_roles())


@app.route('/users/verify/<id>', methods=['POST', 'GET'])
@flask_login.login_required
@utility.role_required(['administrator', 'caretaker'])
def users_verify(id):
    user = db.get_user(id)
    user.user_role = db.get_user_role("volunteer")
    db.db.session.add(user)
    db.db.session.commit()
    return flask.redirect(flask.url_for('users'))


@app.route('/users/unverify/<id>', methods=['POST', 'GET'])
@flask_login.login_required
@utility.role_required(['administrator', 'caretaker'])
def users_unverify(id):
    user = db.get_user(id)
    user.user_role = db.get_user_role("unverified")
    db.db.session.add(user)
    db.db.session.commit()
    return flask.redirect(flask.url_for('users'))


@app.route('/users', methods=['GET'])
@flask_login.login_required
@utility.role_required(['administrator', 'caretaker'])
def users():

    if flask_login.current_user.user_role.name == "administrator":
        return utility.render_with_permissions(
            'users.html',
            users=db.get_users()
        )

    if flask_login.current_user.user_role.name == "caretaker":
        users = db.get_users(role="unverified")
        users.extend(db.get_users(role="volunteer"))

        return utility.render_with_permissions(
            'users.html',
            users=users
        )
