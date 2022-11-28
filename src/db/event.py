from datetime import date, datetime
from .constants import db
from sqlalchemy.orm import relation
from .constants import STRING_LEN


class Event(db.Model):
    __tablename__ = "event"
    id = db.Column(db.Integer,
                   primary_key=True, autoincrement=True)

    # FOREIGN KEYS
    animal_id = db.Column(
        db.Integer, db.ForeignKey("animal.id"))
    user_id = db.Column(
        db.Integer, db.ForeignKey("user.id"))

    # ATTRIBUTES
    start = db.Column(db.DateTime)
    end = db.Column(db.DateTime)

    # RELATIONS
    animal = relation("Animal", back_populates="events")
    user = relation("User", back_populates="events")

    # MAPPER PARAMS
    table_type = db.Column(db.String(STRING_LEN))
    __mapper_args__ = {
        'polymorphic_on': table_type,
        'polymorphic_identity': 'Event'
    }

    def __init__(self, start: datetime, end: datetime):
        self.start = start
        self.end = end
