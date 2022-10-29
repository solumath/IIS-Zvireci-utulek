import flask
from db import db


app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://login:password@localhost/iis'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://login:@localhost/iis'
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
