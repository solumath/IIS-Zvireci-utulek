import db
import flask
import datetime
import flask_login
import response as r
from app import app
import utility


@app.route('/my_walks', methods=['GET', 'POST'])
@flask_login.login_required
def my_walks():
    if flask.request.method == 'POST':
        if 'DELETE' in flask.request.form['action']:
            # todo admin může mazat všechny eventy
            if utility.date_from_datetime(flask.request.form['start']) == datetime.datetime.today().date():
                flask.flash(r.DELETE_PRESENT_WALK, r.ERROR)
                return utility.render_with_permissions(
                    'walks.html',
                    past_events=db.get_past_events(
                        user=flask_login.current_user.id),
                    future_events=db.get_future_events(
                        user=flask_login.current_user.id)
                )

            event = db.get_event(flask.request.form['id'])
            db.db.session.delete(event)
            db.db.session.commit()
            return utility.render_with_permissions(
                'walks.html',
                past_events=db.get_past_events(
                    user=flask_login.current_user.id),
                future_events=db.get_future_events(
                    user=flask_login.current_user.id)
            )

    return utility.render_with_permissions(
        'walks.html',
        past_events=db.get_past_events(user=flask_login.current_user.id),
        future_events=db.get_future_events(
            user=flask_login.current_user.id)
    )
