import flask
import flask_login
from app import app
import db
import utility
import response as r
from munch import DefaultMunch


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
    return utility.render_with_permissions('animals.html',  animal_info=db.get_animals())


@app.route('/animals/<id>')
def animals_detail(id):
    animal = db.get_animal(id)
    if animal is None:
        flask.flash(r.ANIMAL_NOT_FOUND, r.ERROR)
        return flask.redirect(flask.url_for('animals'))
    return utility.render_with_permissions('animal_detail.html', animal=animal)


@app.route('/animals/medical_records/<id>')
@flask_login.login_required
@utility.role_required(['administrator', 'caretaker', 'vet'])
def animals_medical_record(id):
    animal = db.get_animal(id)
    if animal is None:
        flask.flash(r.ANIMAL_NOT_FOUND, r.ERROR)
        return flask.redirect(flask.url_for('animals'))
    return utility.render_with_permissions(
        'animal_medical_records.html',
        animal=animal,
        future_examinations=db.get_future_medical_records(animal=animal),
        history_examinations=db.get_past_medical_records(animal=animal)
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
        discovery_day = utility.parse_date(flask.request.form.get("discovery_day"))

        if (discovery_day < birthday):
            flask.flash(r.WRONG_DISCOVERY_DATE, r.ERROR)
            return utility.render_with_permissions('animal_add.html')
        discovery_place = flask.request.form.get("discovery_place")
        description = flask.request.form.get("description")

        new_animal = db.Animal(name, sex, color, weight, height, kind, breed,
                            chip_id, birthday, discovery_day, discovery_place, description)
        db.db.session.add(new_animal)
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

        if (int(animal.weight) < 0):
            flask.flash(r.NEGATIVE_WEIGHT, r.ERROR)
            return utility.render_with_permissions('animal_edit.html', animal=animal_form)
        animal.height = flask.request.form.get('height')

        if (int(animal.height) < 0):
            flask.flash(r.NEGATIVE_HEIGHT, r.ERROR)
            return utility.render_with_permissions('animal_edit.html', animal=animal_form)
        animal.kind = flask.request.form.get('kind')
        animal.breed = flask.request.form.get('breed')
        animal.chip_id = flask.request.form.get('chip_id')

        if (int(animal.chip_id) < 0):
            flask.flash(r.NEGATIVE_CHIP_ID, r.ERROR)
            return utility.render_with_permissions('animal_edit.html', animal=animal_form)
        animal.birthday = utility.parse_date(flask.request.form.get('birthday'))
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
@utility.role_required(['administrator', 'caretaker'])
def medical_request(id):
    animal = db.get_animal(id)
    if animal is None:
        flask.flash(r.ANIMAL_NOT_FOUND, r.ERROR)
        return flask.redirect(flask.url_for('animals'))
    return utility.render_with_permissions('medical_request.html', animal=animal)
