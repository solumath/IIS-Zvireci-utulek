import db
import flask
import flask_login
from app import app
import utility


@app.route('/walks/delete', methods=['GET', 'POST'])
@flask_login.login_required
@utility.role_required(['administrator'])
def walks_delete():
    if flask.request.method == 'POST':
        animal = db.get_event(flask.request.form['id'])
        db.db.session.delete(animal)
        db.db.session.commit()
        return flask.redirect(flask.url_for('walks'))

    return flask.redirect(flask.url_for('walks'))


@app.route('/walks', methods=['GET', 'POST'])
@flask_login.login_required
@utility.role_required(['administrator', 'vet'])
def walks():
    return utility.render_with_permissions(
        'walks.html',
        past_events=db.get_past_events(),
        future_events=db.get_future_events()
    )
