import db
import flask
import flask_login
from app import app
import utility
import response as r


@app.route('/walks/confirm', methods=['GET', 'POST'])
@flask_login.login_required
@utility.role_required(['administrator', 'caretaker'])
def walks_confirm():
    if flask.request.method == 'POST':
        walk = db.get_event(flask.request.form.get('id'))
        if walk is None:
            flask.flash(r.WALK_NOT_FOUND, r.ERROR)
            return flask.redirect(flask.url_for('walks'))
        walk.confirmed = True
        db.db.session.commit()
        return flask.redirect(flask.url_for('walks'))

    return flask.redirect(flask.url_for('walks'))


@app.route('/walks/unconfirm', methods=['GET', 'POST'])
@flask_login.login_required
@utility.role_required(['administrator', 'caretaker'])
def walks_unconfirm():
    if flask.request.method == 'POST':
        walk = db.get_event(flask.request.form.get('id'))
        if walk is None:
            flask.flash(r.WALK_NOT_FOUND, r.ERROR)
            return flask.redirect(flask.url_for('walks'))
        walk.confirmed = False
        db.db.session.commit()
        return flask.redirect(flask.url_for('walks'))

    return flask.redirect(flask.url_for('walks'))


@app.route('/walks/delete', methods=['GET', 'POST'])
@flask_login.login_required
@utility.role_required(['administrator', 'caretaker'])
def walks_delete():
    if flask.request.method == 'POST':
        animal = db.get_event(flask.request.form.get('id'))
        if animal is None:
            flask.flash(r.ANIMAL_NOT_FOUND, r.ERROR)
            return flask.redirect(flask.url_for('walks'))

        db.db.session.delete(animal)
        db.db.session.commit()
        return flask.redirect(flask.url_for('walks'))


    return flask.redirect(flask.url_for('walks'))


@app.route('/walks', methods=['GET', 'POST'])
@flask_login.login_required
@utility.role_required(['administrator', 'caretaker'])
def walks():
    return utility.render_with_permissions(
        'walks.html',
        past_events=db.get_past_walks(),
        future_events=db.get_future_walks()
    )
