import db
import flask
import datetime
import flask_login
import response as r
from app import app
import utility


@app.route('/my_walks/delete', methods=['GET', 'POST'])
@flask_login.login_required
def my_walks_delete():
    if flask.request.method == 'POST':
        if utility.date_from_datetime(flask.request.form['start']) == datetime.datetime.today().date():
            flask.flash(r.DELETE_PRESENT_WALK, r.ERROR)
            return flask.redirect(flask.url_for('my_walks'))

        animal = db.get_event(flask.request.form['id'])
        db.db.session.delete(animal)
        db.db.session.commit()
        return flask.redirect(flask.url_for('my_walks'))

    return flask.redirect(flask.url_for('my_walks'))

@app.route('/my_walks', methods=['GET', 'POST'])
@flask_login.login_required
def my_walks():
    return utility.render_with_permissions(
        'my_walks.html',
        past_events=db.get_past_events(user=flask_login.current_user.id),
        future_events=db.get_future_events(user=flask_login.current_user.id),
        today=datetime.datetime.today().date()
    )
