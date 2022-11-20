import flask_login
import flask
from app import app
import db
import response as r
from .permissions import render_with_permissions, role_required

message = None


def render():
    return flask.render_template(
        'admin.html',
        users=db.get_users(),
        animals=db.get_animals(),
        events=db.get_events_query()
    )


def delete_user(form):
    global message
    if int(form['id']) == flask_login.current_user.id:
        message = [r.DELETE_YOURSELF_FAILED, r.ERROR]
        return render()

    user = db.get_user(form['id'])
    db.db.session.delete(user)
    db.db.session.commit()
    return render()


def edit_user(form):
    pass


def delete_animal(form):
    animal = db.get_animal(form['id'])
    db.db.session.delete(animal)
    db.db.session.commit()
    return render()


def edit_animal(form):
    pass


def delete_event(form):
    animal = db.get_event(form['id'])
    db.db.session.delete(animal)
    db.db.session.commit()
    return render()


def edit_event(form):
    pass


@app.route('/admin', methods=['GET', 'POST'])
@flask_login.login_required
@role_required(['administrator'])
def admin():
    global message
    if flask.request.method == 'POST':
        if 'EDIT' in flask.request.form['action']:
            if flask.request.form['object'] == 'user':
                return edit_user(flask.request.form)
            if flask.request.form['object'] == 'animal':
                return edit_animal(flask.request.form)
            if flask.request.form['object'] == 'event':
                return edit_event(flask.request.form)

        if 'DELETE' in flask.request.form['action']:
            if flask.request.form['object'] == 'user':
                return delete_user(flask.request.form)
            if flask.request.form['object'] == 'animal':
                return delete_animal(flask.request.form)
            if flask.request.form['object'] == 'event':
                return delete_event(flask.request.form)

    if message is None:
        return render()
    else:
        flask.flash(*message)
        message = None
        return render()
