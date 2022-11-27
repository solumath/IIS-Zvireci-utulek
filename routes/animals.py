import datetime
import flask
import flask_login
from app import app
import db
import utility
import response as r
from munch import DefaultMunch
from collections import namedtuple
import os.path as path


WalkInterval = namedtuple("WalkInterval", ["start", "end", "free"])
walk_windows = [
    WalkInterval(datetime.time(8, 0), datetime.time(10, 0), False),
    WalkInterval(datetime.time(10, 0), datetime.time(12, 0), False),
    WalkInterval(datetime.time(14, 0), datetime.time(16, 0), False),
    WalkInterval(datetime.time(16, 0), datetime.time(18, 0), False),
]


def get_intervals(animal, days):
    for day in days:
        for window in walk_windows:
            start = datetime.datetime.combine(day, window.start)
            end = datetime.datetime.combine(day, window.end)
            free = db.animal_has_free_time(animal, start, end)
            if start < datetime.datetime.now():
                continue
            yield WalkInterval(start, end, free)


@app.route('/animals/delete', methods=['GET', 'POST'])
@flask_login.login_required
@utility.role_required(['administrator', 'caretaker'])
def animals_delete():
    if flask.request.method == 'POST':
        animal = db.get_animal(flask.request.form['id'])
        if animal is None:
            flask.flash(r.ANIMAL_NOT_FOUND, r.ERROR)
            return flask.redirect(flask.url_for('animals'))
        for event in animal.events:
            db.db.session.delete(event)

        db.db.session.delete(animal)
        db.db.session.commit()
    return flask.redirect(flask.url_for('animals'))


@app.route('/animals', methods=['GET', 'POST'])
def animals():
    return utility.render_with_permissions('animals.html',  animal_info=db.get_animals(), now=datetime.date.today())


@app.route('/animals/<id>')
def animals_detail(id):
    animal = db.get_animal(id)
    if animal is None:
        flask.flash(r.ANIMAL_NOT_FOUND, r.ERROR)
        return flask.redirect(flask.url_for('animals'))

    today = datetime.date.today()
    intervals = [interval for interval in get_intervals(
        animal, utility.days_iter(today, today+datetime.timedelta(7)))]

    return utility.render_with_permissions('animal_detail.html', animal=animal, intervals=intervals)


@app.route('/animals/medical_records/delete', methods=['POST'])
@flask_login.login_required
@utility.role_required(['administrator', 'caretaker', 'veterinarian'])
def animals_medical_records_delete():
    try:
        medical_record = db.get_event(flask.request.form['id'])
        animal = medical_record.animal
        db.db.session.delete(medical_record)
        db.db.session.commit()
    except:
        flask.flash(r.UNSPECIFIED_ERROR, r.ERROR)
        return flask.redirect('/')
    return flask.redirect(flask.url_for("animals_medical_record", id=animal.id))


@app.route('/animals/medical_records/<id>')
@flask_login.login_required
@utility.role_required(['administrator', 'caretaker', 'veterinarian'])
def animals_medical_record(id):
    animal = db.get_animal(id)
    if animal is None:
        flask.flash(r.ANIMAL_NOT_FOUND, r.ERROR)
        return flask.redirect(flask.url_for('animals'))
    return utility.render_with_permissions(
        'animal_medical_records.html',
        animal=animal,
        requests=db.get_examination_requests(animal=animal),
        records=db.get_medical_records(animal=animal)
    )


@app.route('/animals/add', methods=['POST', 'GET'])
@flask_login.login_required
@utility.role_required(['administrator', 'caretaker'])
def animals_add():
    if flask.request.method == "POST":
        name = flask.request.form.get("name")
        sex = flask.request.form.get("sex")
        color = flask.request.form.get("color")
        weight = flask.request.form.get("weight")

        if (int(weight) < 0):
            flask.flash(r.NEGATIVE_WEIGHT, r.ERROR)
            return utility.render_with_permissions('animal_add.html')
        height = flask.request.form.get("height")

        if (int(height) < 0):
            flask.flash(r.NEGATIVE_HEIGHT, r.ERROR)
            return utility.render_with_permissions('animal_add.html')
        kind = flask.request.form.get("kind")
        breed = flask.request.form.get("breed")
        chip_id = flask.request.form.get("chip_id")

        if (int(chip_id) < 0):
            flask.flash(r.NEGATIVE_CHIP_ID, r.ERROR)
            return utility.render_with_permissions('animal_add.html')
        birthday = utility.parse_date(flask.request.form.get("birthday"))
        discovery_day = utility.parse_date(
            flask.request.form.get("discovery_day"))

        if (discovery_day < birthday):
            flask.flash(r.WRONG_DISCOVERY_DATE, r.ERROR)
            return utility.render_with_permissions('animal_add.html')
        discovery_place = flask.request.form.get("discovery_place")
        description = flask.request.form.get("description")

        new_animal = db.Animal(name, sex, color, weight, height, kind, breed,
                               chip_id, birthday, discovery_day, discovery_place, description)
        db.db.session.add(new_animal)
        db.db.session.commit()

        image = flask.request.files["image"]
        image_path = path.join(
            "assets", f"animal-image-{new_animal.id}-{image.filename}")
        image.save(path.join("static", image_path))
        new_animal.image = image_path

        db.db.session.commit()
        return flask.redirect(f'{new_animal.id}')

    return utility.render_with_permissions('animal_add.html')


@app.route('/animals/edit/<id>', methods=['GET', 'POST'])
@flask_login.login_required
@utility.role_required(['administrator', 'caretaker'])
def animals_edit(id):
    animal = db.get_animal(id)
    if animal is None:
        flask.flash(r.ANIMAL_NOT_FOUND, r.ERROR)
        return utility.render_with_permissions(flask.url_for('animals'))

    if flask.request.method == 'POST':
        animal_form = DefaultMunch.fromDict(flask.request.form)

        animal.name = flask.request.form.get('name')
        animal.sex = flask.request.form.get('sex')
        animal.color = flask.request.form.get('color')
        animal.weight = flask.request.form.get('weight')

        if (float(animal.weight) < 0):
            flask.flash(r.NEGATIVE_WEIGHT, r.ERROR)
            return utility.render_with_permissions('animal_edit.html', animal=animal_form)
        animal.height = flask.request.form.get('height')

        if (float(animal.height) < 0):
            flask.flash(r.NEGATIVE_HEIGHT, r.ERROR)
            return utility.render_with_permissions('animal_edit.html', animal=animal_form)
        animal.kind = flask.request.form.get('kind')
        animal.breed = flask.request.form.get('breed')
        animal.chip_id = flask.request.form.get('chip_id')

        if (int(animal.chip_id) < 0):
            flask.flash(r.NEGATIVE_CHIP_ID, r.ERROR)
            return utility.render_with_permissions('animal_edit.html', animal=animal_form)
        animal.birthday = utility.parse_date(
            flask.request.form.get('birthday'))
        animal.discovery_day = utility.parse_date(
            flask.request.form.get('discovery_day'))

        if (animal.discovery_day < animal.birthday):
            flask.flash(r.WRONG_DISCOVERY_DATE, r.ERROR)
            return utility.render_with_permissions('animal_edit.html', animal=animal_form)
        animal.discovery_place = flask.request.form.get('discovery_place')
        animal.description = flask.request.form.get('description')
        db.db.session.commit()
        return flask.redirect(flask.url_for('animals_detail', id=id))

    return utility.render_with_permissions('animal_edit.html', animal=animal)


@app.route('/animals/request/<id>', methods=['GET', 'POST'])
@flask_login.login_required
@utility.role_required(['administrator', 'caretaker', 'veterinarian'])
def medical_request(id):
    veterinarians = db.get_users(role="veterinarian")
    animal = db.get_animal(id)
    if animal is None:
        flask.flash(r.ANIMAL_NOT_FOUND, r.ERROR)
        return flask.redirect(flask.url_for('animals'))
    request_form = DefaultMunch.fromDict(flask.request.form)
    if flask.request.method == 'POST':
        date = flask.request.form.get("date")
        start = utility.datetime_from_date(date, "08:00")
        end = utility.datetime_from_date(date, "18:00")
        if start <= datetime.datetime.now():
            flask.flash(r.PLANNING_HISTORY, r.ERROR)
            return utility.render_with_permissions('examination_request_add.html', animal=request_form, users=veterinarians)
        description = flask.request.form.get("description")

        user_id = flask.request.form.get("veterinarian")
        print(user_id)
        animal_id = animal.id

        new_request = db.ExaminationRequest(start, end, description)
        new_request.user = db.get_user(user_id)
        new_request.animal = db.get_animal(animal_id)
        db.db.session.add(new_request)
        db.db.session.commit()
        flask.flash(r.REQUEST_SUCCEED, r.OK)
        return flask.redirect(flask.url_for('animals_detail', id=animal.id))

    return utility.render_with_permissions('examination_request_add.html', animal=animal, users=veterinarians)


@app.route("/animal/walk_request/<id>", methods=["POST"])
@flask_login.login_required
@utility.role_required(['administrator', 'caretaker', 'veterinarian', 'volunteer'])
def request_walk(id):
    form = flask.request.form
    try:
        start = utility.parse_datetime(form["start"])
        end = utility.parse_datetime(form["end"])
        animal = db.get_animal(id)
        assert animal is not None
        assert db.animal_has_free_time(animal, start, end)
    except:
        flask.flash(r.UNSPECIFIED_ERROR, r.ERROR)
        return flask.redirect(flask.url_for("animals_detial", id=id))

    walk_request = db.Walk(start, end)
    walk_request.animal = animal
    walk_request.user = flask_login.current_user
    db.db.session.add(walk_request)
    db.db.session.commit()

    flask.flash(r.WALK_CREATED_SUCCESSFULLY, r.OK)
    return flask.redirect(flask.url_for("animals_detail", id=id))
