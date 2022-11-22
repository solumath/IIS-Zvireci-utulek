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
            flask.flash(r.NEGATIVE_USER_RATING, r.ERROR)
            return flask.redirect(flask.url_for('users_edit', id=str(id)))

        # translate czech version to english to find in db
        if flask.request.form.get('user_role') == "Veterinář":
            user.user_role = db.get_user_role("veterinarian")
        elif flask.request.form.get('user_role') == "Pečovatel":
            user.user_role = db.get_user_role("caretaker")
        elif flask.request.form.get('user_role') == "Dobrovolník":
            user.user_role = db.get_user_role("volunteer")

        db.db.session.commit()
        return flask.redirect(flask.url_for('users'))
    return utility.render_with_permissions('edit_user.html', user=db.get_user(id))

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