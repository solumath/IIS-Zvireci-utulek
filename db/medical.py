from .event import Event
from sqlalchemy.orm import relation
from .constants import db

from .constants import STRING_LEN


class MedicalRecord(Event):
    __tablename__ = "medical_record"

    record_type = relation("RecordType", back_populates="records")

    record_type_id = db.Column(
        db.Integer, db.ForeignKey("record_type.id"))

    description = db.Column(db.Text)

    __mapper_args__ = {
        'polymorphic_identity': 'MedicalRecord'
    }
