from datetime import datetime, timedelta
import uuid
from .constants import STRING_LEN, db
from sqlalchemy.orm import relation


# time from last action until session is invalid
EXPIRE_TIME = timedelta(minutes=10)


def get_expire_time():
    """Calculates session expiration time"""
    return datetime.now() + EXPIRE_TIME


def get_token():
    """generates new random token"""

    token = uuid.uuid4().__str__()
    while db.session.query(Session).filter(Session.token == token).count() > 0:
        token = uuid.uuid4().__str__()

    return token


class Session(db.Model):
    __tablename__ = "session"
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    token = db.Column(db.String(STRING_LEN),
                      primary_key=True, default=get_token)
    expire = db.Column(db.DateTime, default=get_expire_time)

    user = relation("User", back_populates="session")

    def __init__(self, user):
        self.user = user

    def is_active(self):
        print("is_active call")
        return self.expire > datetime.now()

    def update(self):
        self.expire = get_expire_time()
        return
