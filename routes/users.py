import flask
import flask_login
from app import app
import db
import utility
import response as r


def delete_user(form):
    if int(form['id']) == flask_login.current_user.id:
        flask.flash(r.DELETE_YOURSELF_FAILED, r.ERROR)
        return flask.redirect(flask.url_for('users'))

    user = db.get_user(form['id'])

    for event in db.get_future_events(user):
        db.db.session.delete(event)

    db.db.session.delete(user)
    db.db.session.commit()
    return flask.redirect(flask.url_for('users'))


@app.route('/users/delete', methods=['GET', 'POST'])
@flask_login.login_required
@utility.role_required(['administrator'])
def users_delete():
    if flask.request.method == 'POST':
        return delete_user(flask.request.form)
    return flask.redirect(flask.url_for('users'))


# TODO admin si nemuze zmenit roli
@app.route('/users/edit/<id>', methods=['GET', 'POST'])
@flask_login.login_required
@utility.role_required(['administrator'])
def users_edit(id):
    if flask.request.method == "POST":
        user = db.get_user(id)
        id = user.id
        user.name = flask.request.form.get('name')
        user.surname = flask.request.form.get('surname')
        user.address = flask.request.form.get('address')
        user.tel_number = flask.request.form.get('tel_number')
        user.rating = flask.request.form.get('rating')
        if int(user.rating) < 0:
            flask.flash(r.NEGATIVE_USER_RATING, r.ERROR)
            return flask.redirect(flask.url_for('users_edit', id=str(id)))

        user.user_role = db.get_user_role(flask.request.form.get('user_role'))
        db.db.session.commit()
        return flask.redirect(flask.url_for('users'))

    return utility.render_with_permissions('user_edit.html',
                                           user=db.get_user(id),
                                           user_roles=db.get_user_roles())


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

@app.route('/user/add', methods=['POST', 'GET'])
@flask_login.login_required
@utility.role_required(['administrator'])
def user_add():
    if flask.request.method == "POST":
        login = flask.request.form.get("login")
        user_login = db.db.session.query(db.User).filter(db.User.login == login).first()
        # login conflict
        if user_login is not None:
            flask.flash(r.NOT_UNIQUE_LOGIN, r.ERROR)
            return flask.redirect(flask.url_for('users_edit', id=str(id)))

        password = flask.request.form.get("password")
        email = flask.request.form.get("email")
        user_email = db.db.session.query(db.User).filter(db.User.email == email).first()
        # email conflict
        if user_email is not None:
            flask.flash(r.NOT_UNIQUE_EMAIL, r.ERROR)
            return flask.redirect(flask.url_for('users_edit', id=str(id)))
        name = flask.request.form.get("name")
        surname = flask.request.form.get("surname")
        address = flask.request.form.get("address")
        tel_number = flask.request.form.get("tel_number")
        # TODO check tel. number
        rating = flask.request.form.get("rating")
        if (int(rating) < 0):
            flask.flash(r.NEGATIVE_USER_RATING, r.ERROR)
            return flask.redirect(flask.url_for('users_edit', id=str(id)))

        new_user = db.User(login,password,  name, surname, address, email, tel_number, rating)
        db.db.session.add(new_user)
        db.db.session.commit()
        new_user.user_role = db.get_user_role(flask.request.form.get("user_role"))
        if new_user.user_role == None:
            new_user.user_role = db.get_user_role('unverified')
        if new_user.user_role == 'administrator':
             new_user.role_id = 1
        elif new_user.user_role == 'caretaker':
             new_user.role_id = 2
        elif new_user.user_role == 'veteranian':
            new_user.role_id = 3
        elif new_user.user_role == 'volunteer':
             new_user.role_id = 4
        else:
            new_user.role_id = 5
        db.db.session.commit()
        print(db.get_user(new_user.id))
        return flask.redirect(flask.url_for('users'))
    return utility.render_with_permissions('add_user.html', roles=db.get_user_roles())