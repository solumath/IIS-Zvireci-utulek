import flask
import flask_login
from app import app
from functools import wraps
import db
import datetime


def date(date: str) -> datetime.date:
    return datetime.datetime.strptime(date, "%Y-%m-%d").date()


def parse_form(form, convertors):
    """
    Checks for fields in form and converts them using convertors dict

    Convertors E.x.: {"name":str, "weight":int, "birthday":date}
    """
    result = {}

    for key, convertor in convertors.items():
        value = form.get(key)
        if value is None:
            # TODO handle error input
            print(f"did not find {key}")
            print(form)
            return None
        result[key] = convertor(value)

    return result


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
    return flask.render_template('animal_detail.html', animal=db.get_animal(id))
    # return flask.render_template('404.html')


@app.route('/about')
def about():
    return flask.render_template('about.html')


@app.route('/walks', methods=['GET', 'POST', 'DELETE'])
@flask_login.login_required
def walks():
    if flask.request.method == 'DELETE':
        db.remove_event(flask.request.form['id'])
        return flask.render_template(
            'walks.html',
            user_info=flask_login.current_user.get_info(),
            past_events=db.get_past_events(user=flask_login.current_user.id),
            future_events=db.get_future_events(user=flask_login.current_user.id)
        )

    return flask.render_template(
            'walks.html',
            user_info=flask_login.current_user.get_info(),
            past_events=db.get_past_events(user=flask_login.current_user.id),
            future_events=db.get_future_events(user=flask_login.current_user.id)
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
    convertors = {"name": str, "sex": str, "color": str, "weight": int, "height": int, "kind": str, "breed": str,
                  "chip_id": int, "birthday": date, "discovery_day": date, "discovery_place": str, "description": str}

    values = parse_form(flask.request.form, convertors)

    new_animal = db.Animal(**values)
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
