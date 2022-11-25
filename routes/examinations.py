import db
import flask
import flask_login
from app import app
import utility


@app.route('/examinations/add', methods=['GET', 'POST'])
@flask_login.login_required
@utility.role_required(['administrator', 'caretaker', 'vet'])
def examinations_add():
    pass


@app.route('/examinations/edit', methods=['GET', 'POST'])
@flask_login.login_required
@utility.role_required(['administrator', 'caretaker', 'vet'])
def examinations_edit():
    pass


@app.route('/examinations/delete', methods=['GET', 'POST'])
@flask_login.login_required
@utility.role_required(['administrator', 'caretaker', 'vet'])
def examinations_delete():
    pass


@app.route('/examinations', methods=['GET', 'POST'])
@flask_login.login_required
@utility.role_required(['administrator', 'caretaker', 'vet'])
def examinations():
    return utility.render_with_permissions('events.html', records=db.get_medical_records())
