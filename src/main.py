from app import app
import db

from routes import *


if __name__ == "__main__":
    # temporary reseting database data for debuging purposes
    # with app.app_context():
    #     db.db.drop_all()
    #     db.db.create_all()
    #     import data
    #     data.add_data()
    app.run(host="194.146.12.40",port = 9566)
