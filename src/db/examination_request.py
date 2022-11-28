from .event import Event
from .constants import db
from datetime import datetime


class ExaminationRequest(Event):
    __tablename__ = "examination_request"
    accepted = db.Column(db.Boolean, default=False)

    request = db.Column(db.Text)

    __mapper_args__ = {
        'polymorphic_identity': 'ExaminationRequest'
    }

    def __init__(self, start: datetime, end: datetime, request: str = ""):
        super().__init__(start, end)
        self.request = request
