import db
import flask
import flask_login
from app import app
import utility


@app.route('/examinations/add', methods=['GET', 'POST'])
@flask_login.login_required
@utility.role_required(['administrator', 'caretaker', 'vet'])
def examinations_add():

    if flask.request.method == "GET":
        record_types = db.get_record_types()
        veterinarians = db.get_users(role="veterinarian")
        return utility.render_with_permissions('examination_add.html', record_types=record_types, users=veterinarians, animals=db.get_animals())

    # POST

    date = flask.request.form.get("date")
    start = utility.datetime_from_date(date)
    end = utility.datetime_from_date(date, "12:00:00")
    description = flask.request.form.get("description")

    user_id = 5
    animal_id = 4

    new_request = db.MedicalRecord(start, end, description)
    new_request.user = db.get_user(user_id)
    new_request.animal = db.get_animal(animal_id)
    new_request.record_type = db.get_record_type("requested examination")
    db.db.session.add(new_request)
    db.db.session.commit()


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
