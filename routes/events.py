import flask_login
import flask
from app import app
import db
import response as r
import utility

def edit_event(form):
    pass

@app.route('/events/delete', methods=['GET', 'POST'])
@flask_login.login_required
@utility.role_required(['administrator'])
def events_delete():
    if flask.request.method == 'POST':
        animal = db.get_event(flask.request.form['id'])
        db.db.session.delete(animal)
        db.db.session.commit()
        return flask.redirect('/events')
    return flask.redirect('/events')


@app.route('/events', methods=['GET', 'POST'])
@flask_login.login_required
@utility.role_required(['administrator', 'caretaker'])
def events():
    return utility.render_with_permissions('events.html', events=db.get_events_query())

@app.route('/events/edit/<id>', methods=['GET', 'POST'])
@flask_login.login_required
# @utility.role_required([]) TODO
def events_edit(id):
    return utility.render_with_permissions('event_edit.html', event=db.get_event(id), events=db.get_events_query())


@app.route('/events/add', methods=['GET', 'POST'])
@flask_login.login_required
# @utility.role_required([]) TODO
def events_add():
    return utility.render_with_permissions('event_add.html', events=db.get_events_query(), animals=db.get_animals())