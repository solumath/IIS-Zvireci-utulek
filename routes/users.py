import flask
import flask_login
from app import app
import db
import utility
import response as r


@app.route('/users')
@flask_login.login_required
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

@app.route('/users/edit/<id>', methods=['GET', 'POST'])
@flask_login.login_required
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
            flask.flash('Hodnocení uživatele nesmí být záporné.', r.ERROR)
            return flask.redirect(flask.url_for('users_edit', id=str(id)))

        print(flask.request.form.get('user_role'))
        if flask.request.form.get('user_role') == "Veterinář":
            user.user_role = db.get_user_role("veterinarian")
        elif flask.request.form.get('user_role') == "Pečovatel":
            user.user_role = db.get_user_role("caretaker")
        elif flask.request.form.get('user_role') == "Dobrovolník":
            user.user_role = db.get_user_role("volunteer")
        print(user.user_role)

        db.db.session.commit()
        return flask.redirect(flask.url_for('users'))
    return utility.render_with_permissions('edit_user.html', user=db.get_user(id))
