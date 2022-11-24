from .constants import STRING_LEN, db
from sqlalchemy.orm import relation


class RecordType(db.Model):
    __tablename__ = "record_type"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(STRING_LEN), unique=True)
    czech_name = db.Column(db.String(STRING_LEN))

    priority = db.Column(db.Integer)

    description = db.Column(db.Text)

    records = relation("MedicalRecord", back_populates="record_type")

    def __init__(self, name: str, priority: int = 0, description: str = ""):
        self.name = name
        self.priority = priority
        self.description = description
