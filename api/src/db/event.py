from ..main import db
from .constants import STRING_LEN
import sqlalchemy


class event(db.Model):
    __tablename__ = "event"
    id = sqlalchemy.Column(sqlalchemy.types.Integer, primary_key=True)
    animal_id = sqlalchemy.Column(
        sqlalchemy.types.Integer, sqlalchemy.ForeignKey("animal.id"))
    type_id = sqlalchemy.Column(
        sqlalchemy.types.Integer, sqlalchemy.ForeignKey("event_type.id"))

    start = sqlalchemy.Column(sqlalchemy.types.DateTime)
    end = sqlalchemy.Column(sqlalchemy.types.DateTime)

    description = sqlalchemy.Column(sqlalchemy.types.Text)

    # TODO animal
    # TODO type
    # TODO author
    # TODO performer
