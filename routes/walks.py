import db
import flask
import datetime
import flask_login
import response as r
from app import app
import utility


@app.route('/walks', methods=['GET', 'POST'])
@flask_login.login_required
@utility.role_required(['administrator', 'vet'])
def walks():
    if flask.request.method == 'POST':
        if 'DELETE' in flask.request.form['action']:
            # todo admin může mazat všechny eventy
            if utility.date_from_datetime(flask.request.form['start']) == datetime.datetime.today().date():
                flask.flash(r.DELETE_PRESENT_WALK, r.ERROR)
                return utility.render_with_permissions(
                    'walks.html',
                    past_events=db.get_past_events(),
                    future_events=db.get_future_events()
                )

            event = db.get_event(flask.request.form['id'])
            db.db.session.delete(event)
            db.db.session.commit()
            return utility.render_with_permissions(
                'walks.html',
                past_events=db.get_past_events(),
                future_events=db.get_future_events()
            )

    return utility.render_with_permissions(
        'walks.html',
        past_events=db.get_past_events(),
        future_events=db.get_future_events()
    )
