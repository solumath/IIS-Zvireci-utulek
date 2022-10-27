import flask
import flask_sqlalchemy


app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://login:password@localhost/iis'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://login:@localhost/iis'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = flask_sqlalchemy.SQLAlchemy(app)


@app.route('/')
def hello_world():
    return 'Hello world!'


if __name__ == "__main__":
    app.run()
