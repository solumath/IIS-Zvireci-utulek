import db
import flask
import flask_login
from app import app
import utility


@app.route('/examinations/add', methods=['GET', 'POST'])
@flask_login.login_required
@utility.role_required(['administrator', 'caretaker', 'vet'])
def examinations_add():
    return utility.render_with_permissions('examination_add.html', events=db.get_events_query(), animals=db.get_animals())

@app.route('/examinations/edit/<id>', methods=['GET', 'POST'])
@flask_login.login_required
@utility.role_required(['administrator', 'caretaker', 'vet'])
def examinations_edit(id):
    return utility.render_with_permissions('examination_edit.html', event=db.get_event(id), events=db.get_events_query())


@app.route('/examinations/delete', methods=['GET', 'POST'])
@flask_login.login_required
@utility.role_required(['administrator', 'caretaker', 'vet'])
def examinations_delete():
    if flask.request.method == 'POST':
        animal = db.get_event(flask.request.form['id'])
        db.db.session.delete(animal)
        db.db.session.commit()
        return flask.redirect('/examinations')
    return flask.redirect('/examinations')


@app.route('/examinations', methods=['GET', 'POST'])
@flask_login.login_required
@utility.role_required(['administrator', 'caretaker', 'vet'])
def examinations():
    return utility.render_with_permissions('examinations.html', records=db.get_medical_records())
