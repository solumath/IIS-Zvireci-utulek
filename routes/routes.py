import flask
import flask_login
from app import app
import db
import datetime
from .permissions import role_required, render_with_permissions


def parse_date(date: str) -> datetime.date:
    return datetime.datetime.strptime(date, "%Y-%m-%d").date()


@app.route('/')
def index():
    return flask.render_template('index.html')


@app.route('/animals')
def animals():
    return flask.render_template('animals.html',  animal_info=db.get_animals())


@app.route('/animal/<id>')
def detail(id):
    return flask.render_template('animal_detail.html', animal=db.get_animal(id))
    # return flask.render_template('404.html')


@app.route('/about')
def about():
    return flask.render_template('about.html')


@app.route('/walks', methods=['GET', 'POST'])
@flask_login.login_required
def walks():
    if flask.request.method == 'POST':
        if 'DELETE' in flask.request.form['action']:
            event = db.get_event(flask.request.form['id'])
            db.db.session.delete(event)
            db.db.session.commit()
            return flask.render_template(
                'walks.html',
                past_events=db.get_past_events(
                    user=flask_login.current_user.id),
                future_events=db.get_future_events(
                    user=flask_login.current_user.id)
            )

    return flask.render_template(
        'walks.html',
        past_events=db.get_past_events(user=flask_login.current_user.id),
        future_events=db.get_future_events(
            user=flask_login.current_user.id)
    )


@app.route('/add', methods=['GET'])
@flask_login.login_required
@role_required(['administrator', 'caretaker'])
def add_get():
    return flask.render_template('add_animal.html')


@app.route('/add', methods=['POST'])
@flask_login.login_required
@role_required(['administrator', 'caretaker'])
def add_post():
    name = flask.request.form.get("name")
    if name is None:
        return flask.redirect("404")
    try:
        name = str(name)
    except:
        return flask.redirect("404")

    sex = flask.request.form.get("sex")
    if sex is None:
        return flask.redirect("404")
    try:
        sex = str(sex)
    except:
        return flask.redirect("404")

    color = flask.request.form.get("color")
    if color is None:
        return flask.redirect("404")
    try:
        color = str(color)
    except:
        return flask.redirect("404")

    weight = flask.request.form.get("weight")
    if weight is None:
        return flask.redirect("404")
    try:
        weight = int(weight)
    except:
        return flask.redirect("404")

    height = flask.request.form.get("height")
    if height is None:
        return flask.redirect("404")
    try:
        height = int(height)
    except:
        return flask.redirect("404")

    kind = flask.request.form.get("kind")
    if kind is None:
        return flask.redirect("404")
    try:
        kind = str(kind)
    except:
        return flask.redirect("404")

    breed = flask.request.form.get("breed")
    if breed is None:
        return flask.redirect("404")
    try:
        breed = str(breed)
    except:
        return flask.redirect("404")

    chip_id = flask.request.form.get("chip_id")
    if chip_id is None:
        return flask.redirect("404")
    try:
        chip_id = int(chip_id)
    except:
        return flask.redirect("404")

    birthday = flask.request.form.get("birthday")
    if birthday is None:
        return flask.redirect("404")
    try:
        birthday = parse_date(birthday)
    except:
        return flask.redirect("404")

    discovery_day = flask.request.form.get("discovery_day")
    if discovery_day is None:
        return flask.redirect("404")
    try:
        discovery_day = parse_date(discovery_day)
    except:
        return flask.redirect("404")

    discovery_place = flask.request.form.get("discovery_place")
    if discovery_place is None:
        return flask.redirect("404")
    try:
        discovery_place = str(discovery_place)
    except:
        return flask.redirect("404")

    description = flask.request.form.get("description")
    if description is None:
        return flask.redirect("404")
    try:
        description = str(description)
    except:
        return flask.redirect("404")

    if discovery_day < birthday:
        return flask.redirect("404")

    new_animal = db.Animal(name, sex, color, weight, height, kind, breed,
                           chip_id, birthday, discovery_day, discovery_place, description)
    db.db.session.add(new_animal)
    db.db.session.commit()
    return flask.redirect(f'animal/{new_animal.id}')


@app.route('/examinations')
@flask_login.login_required
@role_required(['administrator', 'vet'])
def examinations():
    return flask.render_template('examinations.html')


@app.route('/profile')
@flask_login.login_required
def profile():
    return flask.render_template(
        'profile.html',
        user_info=flask_login.current_user.get_info(),
        past_events=db.get_past_events(user=flask_login.current_user.id),
        future_events=db.get_future_events(user=flask_login.current_user.id)
    )


@app.errorhandler(401)
def not_enough_perms(e):
    return flask.render_template('401.html')


@app.errorhandler(404)
def page_not_found(e):
    return flask.render_template('404.html')
