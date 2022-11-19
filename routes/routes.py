import flask
import flask_login
from app import app
from functools import wraps
import db

from flask import redirect, request

def role_required(roles):
    """
    Decorator for checking if user has required role.
    accepts multiple roles in list.
    """
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            for role in roles:
                if flask_login.current_user.user_role.name == role:
                    return f(*args, **kwargs)
            else:
                return flask.render_template('401.html')
        return wrapper
    return decorator


@app.route('/')
def index():
    return flask.render_template('index.html')


@app.route('/animals')
def animals():
    return flask.render_template('animals.html',  animal_info=db.get_animals())

@app.route('/animal/<id>')
def detail(id):
    for animal in db.get_animals():
        sameId = int(animal.id)
        if sameId == int(id):
            return flask.render_template('animal_detail.html', animal=animal)
    # return flask.render_template('404.html')


@app.route('/about')
def about():
    return flask.render_template('about.html')


@app.route('/walks')
@flask_login.login_required
def walks():
    return flask.render_template('walks.html')

@app.route('/add', methods=['GET'])
@flask_login.login_required
@role_required(['administrator', 'caretaker'])
def add_get():
    return flask.render_template('add_animal.html')

@app.route('/add', methods=['POST'])
@flask_login.login_required
@role_required(['administrator', 'caretaker'])
def add_post():
    name = request.form.get('name')
    sex = request.form.get('sex')
    color = request.form.get('color')
    weight = request.form.get('weight')
    height = request.form.get('height')
    kind = request.form.get('kind')
    breed = request.form.get('breed')
    chip = request.form.get('chip')
    birthday = request.form.get('birtday')
    discovery_day = request.form.get('date')
    discovery_place = request.form.get('place')
    description = request.form.get('description')
    pic = request.form.get('pic')

    new_animal = db.Animal(name = name, sex=sex, color = color, weight=weight, height=height, kind=kind, breed=breed, chip_id = chip, birthday=birthday, discovery_day=discovery_day, discovery_place=discovery_place, description=description)
    db.db.session.add(new_animal)
    db.db.session.commit()
    return flask.redirect('animal/' + str(new_animal.id))


@app.route('/examinations')
@flask_login.login_required
@role_required(['administrator', 'vet'])
def examinations():
    return flask.render_template('examinations.html')


@app.route('/admin')
@flask_login.login_required
@role_required(['administrator'])
def admin():
    return flask.render_template('admin.html')


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
