import flask
import flask_login
from app import app
import db
import utility
import response as r


@app.route('/animals', methods=['GET', 'POST'])
def animals():
    return utility.render_with_permissions('animals.html',  animal_info=db.get_animals())


@app.route('/animals/<id>')
def animals_detail(id):
    return utility.render_with_permissions('animal_detail.html', animal=db.get_animal(id))


@app.route('/animals/add', methods=['POST', 'GET'])
@flask_login.login_required
@utility.role_required(['administrator', 'caretaker'])
def animals_add():

    if flask.request.method == "GET":
        return utility.render_with_permissions('add_animal.html')

    name = flask.request.form.get("name")
    sex = flask.request.form.get("sex")
    color = flask.request.form.get("color")
    weight = flask.request.form.get("weight")
    if (int(weight) < 0):
        flask.flash('Váha nesmí být záporná.', r.ERROR)
        return flask.redirect(flask.url_for('animals_add', id=str(id)))
    height = flask.request.form.get("height")
    if (int(height) < 0):
        flask.flash('Výška nesmí být záporná.', r.ERROR)
        return flask.redirect(flask.url_for('animals_add', id=str(id)))
    kind = flask.request.form.get("kind")
    breed = flask.request.form.get("breed")
    chip_id = flask.request.form.get("chip_id")
    if (int(chip_id) < 0):
        flask.flash('Číslo čipu nesmí být záporné.', r.ERROR)
        return flask.redirect(flask.url_for('animals_add', id=str(id)))
    birthday = utility.parse_date(flask.request.form.get("birthday"))
    discovery_day = utility.parse_date(flask.request.form.get("discovery_day"))
    if (discovery_day < birthday):
        flask.flash('Špatné datum přijetí nebo narození.', r.ERROR)
        return flask.redirect(flask.url_for('animals_add', id=str(id)))
    discovery_place = flask.request.form.get("discovery_place")
    description = flask.request.form.get("description")

    new_animal = db.Animal(name, sex, color, weight, height, kind, breed,
                           chip_id, birthday, discovery_day, discovery_place, description)
    db.db.session.add(new_animal)
    db.db.session.commit()
    return flask.redirect(f'{new_animal.id}')


@app.route('/animals/edit/<id>', methods=['GET', 'POST'])
@flask_login.login_required
@utility.role_required(['administrator', 'caretaker'])
def animals_edit(id):
    if flask.request.method == 'POST':
        animal = db.get_animal(id)
        id = animal.id
        animal.name = flask.request.form.get('name')
        animal.sex = flask.request.form.get('sex')
        animal.color = flask.request.form.get('color')
        animal.weight = flask.request.form.get('weight')
        if (int(animal.weight) < 0):
            flask.flash('Váha nesmí být záporná.', r.ERROR)
            return flask.redirect(flask.url_for('animals_edit', id=str(id)))
        animal.height = flask.request.form.get('height')
        if (int(animal.height) < 0):
            flask.flash('Výška nesmí být záporná.', r.ERROR)
            return flask.redirect(flask.url_for('animals_edit', id=str(id)))
        animal.kind = flask.request.form.get('kind')
        animal.breed = flask.request.form.get('breed')
        animal.chip_id = flask.request.form.get('chip_id')
        if (int(animal.chip_id) < 0):
            flask.flash('Číslo čipu nesmí být záporné.', r.ERROR)
            return flask.redirect(flask.url_for('animals_edit', id=str(id)))
        animal.birthday = utility.parse_date(flask.request.form.get('birthday'))
        animal.discovery_day = utility.parse_date(
            flask.request.form.get('discovery_day'))
        if (animal.discovery_day < animal.birthday):
            flask.flash('Špatné datum přijetí nebo narození.', r.ERROR)
            return flask.redirect(flask.url_for('animals_edit', id=str(id)))
        animal.discovery_place = flask.request.form.get('discovery_place')
        animal.description = flask.request.form.get('description')
        db.db.session.commit()
        return flask.redirect(flask.url_for('animals_detail', id=str(id)))
    return utility.render_with_permissions('edit_animal.html', animal=db.get_animal(id))
