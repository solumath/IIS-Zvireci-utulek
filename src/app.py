import flask
from db import db
from flask_cors import CORS


app = flask.Flask(__name__)
app.config["DEBUG"] = False
app.config['SECRET_KEY'] = '5ee1418c2eadbdd70a8f681d719628970de4c927177b47a7'       # Security ++
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://iis:iispass@localhost/iis'
CORS(app, supports_credentials=True)
db.init_app(app)
