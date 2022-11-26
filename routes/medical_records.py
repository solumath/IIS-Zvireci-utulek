import db
import flask
import flask_login
from app import app
import utility
import response as r


@app.route('/medical_records/add', methods=['GET', 'POST'])
@flask_login.login_required
@utility.role_required(['administrator', 'caretaker', 'veterinarian'])
def medical_records_add():

    if flask.request.method == "POST":

        # POST

        form = flask.request.form

        try:
            start = utility.parse_html_datetime(form["start"])
            end = utility.parse_html_datetime(form["end"])
            if start > end:
                flask.flash(r.WRONG_DATETIME, r.ERROR)
                flask.redirect(flask.url_for("medical_records_add"))
            desc = form["description"]
            user_id = int(form["veterinarian"])
            animal_id = int(form["animal"])
            record_type = form["record_type"]
        except:
            flask.flash(r.UNSPECIFIED_ERROR, r.ERROR)
            return flask.redirect(flask.url_for("medical_records_add"))

        new_record = db.MedicalRecord(start, end, desc)
        new_record.user = db.get_user(user_id)
        new_record.animal = db.get_animal(animal_id)
        new_record.record_type = db.get_record_type(record_type)
        db.db.session.add(new_record)
        db.db.session.commit()

        return flask.redirect(flask.url_for("medical_records"))

    # GET

    record_types = db.get_record_types()
    veterinarians = db.get_users(role="veterinarian")
    return utility.render_with_permissions('medical_record_add.html', record_types=record_types, users=veterinarians, animals=db.get_animals())


@app.route('/medical_records/edit/<id>', methods=['GET', 'POST'])
@flask_login.login_required
@utility.role_required(['administrator', 'caretaker', 'veterinarian'])
def medical_records_edit(id):
    # load default values from db
    record_types = db.get_record_types()
    record = db.get_medical_record(id)
    animal = db.get_animal(id)
    record_type = record.record_type
    start = record.start
    end = record.end
    description = record.description

    if flask.request.method == "POST":
        # for POST method parse form
        form = flask.request.form

        try:
            message = r.UNSPECIFIED_ERROR
            record_type = db.get_record_type(form["record_type"])
            start = utility.parse_html_datetime(form["start"])
            end = utility.parse_html_datetime(form["end"])
            description = form["description"]

            message = r.WRONG_DATETIME
            assert start <= end
        except Exception as e:
            flask.flash(message, r.ERROR)
            return utility.render_with_permissions(
                'medical_record_edit.html', record_type=record_type, animal_name=animal.name, start=start, end=end, description=description, record_types=record_types)

        # changing values in db
        record.record_type = record_type
        record.start = start
        record.end = end
        record.description = description

        db.db.session.commit()

        # if successfull redirect
        return flask.redirect(flask.url_for("medical_records"))

    # for GET method, just render site
    return utility.render_with_permissions(
        'medical_record_edit.html', record_type=record_type, animal_name=animal.name, start=start, end=end, description=description, record_types=record_types)


@app.route('/medical_records/delete', methods=['POST'])
@flask_login.login_required
@utility.role_required(['administrator', 'caretaker', 'veterinarian'])
def medical_records_delete():
    try:
        medical_record = db.get_event(flask.request.form['id'])
        db.db.session.delete(medical_record)
        db.db.session.commit()
    except:
        flask.flash(r.UNSPECIFIED_ERROR, r.ERROR)
        
    return flask.redirect('/medical_records')


@app.route('/medical_records')
@flask_login.login_required
@utility.role_required(['administrator', 'caretaker', 'veterinarian'])
def medical_records():
    if flask_login.current_user.user_role == db.get_user_role("veterinarian"):
        return utility.render_with_permissions(
            'medical_records.html',
            requests=db.get_examination_requests(
                user=flask_login.current_user),
            medical_records=db.get_medical_records(user=flask_login.current_user))

    return utility.render_with_permissions(
        'medical_records.html', requests=db.get_examination_requests(), medical_records=db.get_medical_records())
