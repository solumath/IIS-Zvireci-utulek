from datetime import date, datetime
from .constants import db
from sqlalchemy.orm import relation


class Event(db.Model):
    __tablename__ = "event"
    id = db.Column(db.Integer,
                   primary_key=True, autoincrement=True)

    animal_id = db.Column(
        db.Integer, db.ForeignKey("animal.id"))
    event_type_id = db.Column(
        db.Integer, db.ForeignKey("event_type.id"))
    user_id = db.Column(
        db.Integer, db.ForeignKey("user.id"))

    start = db.Column(db.DateTime)
    end = db.Column(db.DateTime)

    description = db.Column(db.Text)

    animal = relation("Animal", back_populates="events")
    event_type = relation("Event_type", back_populates="events")
    user = relation("User", back_populates="events")

    def __init__(self, start: datetime, end: datetime, description: str = ""):
        self.start = start
        self.end = end
        self.description = description
