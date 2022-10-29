from user_session import *
from app import app
import db

# cross origin resource sharing
from flask_cors import cross_origin


@cross_origin
@app.route('/')
def hello_world():
    return 'Hello world!'


if __name__ == "__main__":
    # temporary reseting database data for debuging purposes
    with app.app_context():
        db.db.drop_all()
        db.db.create_all()
        import data
        data.add_data()
    app.run()
