from ..main import db
from .constants import STRING_LEN
import sqlalchemy


class event_type(db.Model):
    __tablename__ = "event_type"
    id = sqlalchemy.Column(sqlalchemy.types.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.types.String(STRING_LEN))

    priority = sqlalchemy.Column(sqlalchemy.types.Integer)

    description = sqlalchemy.Column(sqlalchemy.types.Text)
