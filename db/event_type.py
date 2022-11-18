from .constants import STRING_LEN, db
from sqlalchemy.orm import relation


class EventType(db.Model):
    __tablename__ = "event_type"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(STRING_LEN), unique=True)

    priority = db.Column(db.Integer)

    description = db.Column(db.Text)

    events = relation("Event", back_populates="event_type")
    permissions = relation("Permission", back_populates="event_type")

    def __init__(self, name: str, priority: int = 0, description: str = ""):
        self.name = name
        self.priority = priority
        self.description = description
