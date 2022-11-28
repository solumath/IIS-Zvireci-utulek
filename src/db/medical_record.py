from .event import Event
from sqlalchemy.orm import relation
from .constants import STRING_LEN, db

from datetime import datetime


class MedicalRecord(Event):
    __tablename__ = "medical_record"

    record_type = relation("RecordType", back_populates="records")

    record_type_id = db.Column(
        db.Integer, db.ForeignKey("record_type.id"))

    description = db.Column(db.Text)

    __mapper_args__ = {
        'polymorphic_identity': 'MedicalRecord'
    }

    def __init__(self, start: datetime, end: datetime, description: str = ""):
        super().__init__(start, end)
        self.description = description
