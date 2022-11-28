from app import app
import db

from routes import *


def reset_db():
    with app.app_context():
        db.db.drop_all()
        db.db.create_all()
        import data
        data.add_data()


if __name__ == "__main__":
    # temporary reseting database data for debuging purposes
    app.run()
