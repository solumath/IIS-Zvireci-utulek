import db
from app import app
import flask
from flask_cors import cross_origin
import response as r


@cross_origin
@app.route('/register', methods=['POST'])
def register():
    json = flask.request.json

    # check if needed data was sent
    needed_fields = {"login", "password", "name",
                     "surname", "address", "email", "tel_number"}
    if set(json.keys()) != needed_fields:
        return r.generate_response(r.STAUTS_BAD_REQUEST, r.MISSING_FIELD)

    # user lookup
    login = json["login"]
    user = db.db.session.query(db.User).filter(
        db.User.login == login).first()

    # login conflict
    if user is not None:
        return r.generate_response(r.STAUTS_BAD_REQUEST, r.USER_ALREADY_EXISTS)

    # create user and insert to db
    new_user = db.User(**json)
    db.db.session.add(new_user)
    db.db.session.commit()

    return r.generate_OK()
