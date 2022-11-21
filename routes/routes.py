import flask
import flask_login
from app import app
import db
import datetime
import response as r
from .permissions import role_required, render_with_permissions


def parse_date(date: str) -> datetime.date:
    return datetime.datetime.strptime(date, "%Y-%m-%d").date()


def date_from_datetime(date: str) -> datetime.datetime:
    return datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S").date()


@app.route('/')
def index():
    return render_with_permissions('index.html')


@app.route('/animals', methods=['GET', 'POST'])
def animals():
    return flask.render_template('animals.html',  animal_info=db.get_animals())


@app.route('/animal/<id>')
def detail(id):
    return render_with_permissions('animal_detail.html', animal=db.get_animal(id))


@app.route('/about')
def about():
    return render_with_permissions('about.html')


@app.route('/walks', methods=['GET', 'POST'])
@flask_login.login_required
def walks():
    if flask.request.method == 'POST':
        if 'DELETE' in flask.request.form['action']:
            # todo admin může mazat všechny eventy
            if date_from_datetime(flask.request.form['start']) == datetime.datetime.today().date():
                flask.flash(r.DELETE_PRESENT_WALK, r.ERROR)
                return render_with_permissions(
                    'walks.html',
                    past_events=db.get_past_events(
                        user=flask_login.current_user.id),
                    future_events=db.get_future_events(
                        user=flask_login.current_user.id)
                )

            event = db.get_event(flask.request.form['id'])
            db.db.session.delete(event)
            db.db.session.commit()
            return render_with_permissions(
                'walks.html',
                past_events=db.get_past_events(
                    user=flask_login.current_user.id),
                future_events=db.get_future_events(
                    user=flask_login.current_user.id)
            )

    return render_with_permissions(
        'walks.html',
        past_events=db.get_past_events(user=flask_login.current_user.id),
        future_events=db.get_future_events(
            user=flask_login.current_user.id)
    )


@app.route('/animal/add', methods=['GET'])
@flask_login.login_required
@role_required(['administrator', 'caretaker'])
def add_get():
    return render_with_permissions('add_animal.html')


@app.route('/animal/add', methods=['POST'])
@flask_login.login_required
@role_required(['administrator', 'caretaker'])
def add_post():
    name = flask.request.form.get("name")
    sex = flask.request.form.get("sex")
    color = flask.request.form.get("color")
    weight = flask.request.form.get("weight")
    if(int(weight) < 0):
        flask.flash('Váha nesmí být záporná.')
        return flask.redirect(flask.url_for('add_post', id=str(id)))
    height = flask.request.form.get("height")
    if(int(height) < 0):
            flask.flash('Výška nesmí být záporná.')
            return flask.redirect(flask.url_for('add_post', id=str(id)))
    kind = flask.request.form.get("kind")
    breed = flask.request.form.get("breed")
    chip_id = flask.request.form.get("chip_id")
    if(int(chip_id) < 0):
        flask.flash('Číslo čipu nesmí být záporné.')
        return flask.redirect(flask.url_for('add_post', id=str(id)))
    birthday = parse_date(flask.request.form.get("birthday"))
    discovery_day = parse_date(flask.request.form.get("discovery_day"))
    if(discovery_day < birthday):
        flask.flash('Špatné datum přijetí nebo narození.')
        return flask.redirect(flask.url_for('add_post', id=str(id)))
    discovery_place = flask.request.form.get("discovery_place")
    description = flask.request.form.get("description")

    new_animal = db.Animal(name, sex, color, weight, height, kind, breed,
                           chip_id, birthday, discovery_day, discovery_place, description)
    db.db.session.add(new_animal)
    db.db.session.commit()
    return flask.redirect(f'{new_animal.id}')

@app.route('/animals/edit/<id>', methods=['GET', 'POST'])
@flask_login.login_required
@role_required(['administrator', 'caretaker'])
def edit_animal(id):
    if flask.request.method == 'POST':
        animal = db.get_animal(id)
        id=animal.id
        animal.name=flask.request.form.get('name')
        animal.sex=flask.request.form.get('sex')
        animal.color=flask.request.form.get('color')
        animal.weight=flask.request.form.get('weight')
        if(int(animal.weight) < 0):
            flask.flash('Váha nesmí být záporná.')
            return flask.redirect(flask.url_for('edit_animal', id=str(id)))
        animal.height=flask.request.form.get('height')
        if(int(animal.height) < 0):
            flask.flash('Výška nesmí být záporná.')
            return flask.redirect(flask.url_for('edit_animal', id=str(id)))
        animal.kind=flask.request.form.get('kind')
        animal.breed=flask.request.form.get('breed')
        animal.chip_id=flask.request.form.get('chip_id')
        if(int(animal.chip_id) < 0):
            flask.flash('Číslo čipu nesmí být záporné.')
            return flask.redirect(flask.url_for('edit_animal', id=str(id)))
        animal.birthday=parse_date(flask.request.form.get('birthday'))
        animal.discovery_day=parse_date(flask.request.form.get('discovery_day'))
        if(animal.discovery_day < animal.birthday):
            flask.flash('Špatné datum přijetí nebo narození.')
            return flask.redirect(flask.url_for('edit_animal', id=str(id)))
        animal.discovery_place=flask.request.form.get('discovery_place')
        animal.description=flask.request.form.get('description')
        db.db.session.commit()
        return flask.redirect(flask.url_for('detail', id=str(id)))
    return flask.render_template('edit_animal.html', animal=db.get_animal(id))

@app.route('/examinations')
@flask_login.login_required
@role_required(['administrator', 'vet'])
def examinations():
    return render_with_permissions('examinations.html')


@app.route('/profile')
@flask_login.login_required
def profile():
    return render_with_permissions(
        'profile.html',
        user_info=flask_login.current_user.get_info(),
        past_events=db.get_past_events(user=flask_login.current_user.id),
        future_events=db.get_future_events(user=flask_login.current_user.id)
    )


@app.errorhandler(401)
def not_enough_perms(e):
    return render_with_permissions('401.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_with_permissions('404.html')
