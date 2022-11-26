from .event import Event
from .constants import db


class Walk(Event):
    __tablename__ = "walk"

    confirmed = db.Column(db.Boolean, default=False)
    returned = db.Column(db.Boolean, default=False)

    __mapper_args__ = {
        'polymorphic_identity': 'Walk'
    }
