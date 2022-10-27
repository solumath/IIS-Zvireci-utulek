from ..main import db
from .constants import STRING_LEN
import sqlalchemy


class animal(db.Model):
    """
    Table for animal, 
    contains basic info about animal
    connects to Event table for history of animal
    """
    __tablename__ = "animal"
    id = sqlalchemy.Column(sqlalchemy.types.Integer, primary_key=True)

    name = sqlalchemy.Column(sqlalchemy.types.String(STRING_LEN))
    sex = sqlalchemy.Column(sqlalchemy.types.String(STRING_LEN))
    color = sqlalchemy.Column(sqlalchemy.types.String(STRING_LEN))
    weight = sqlalchemy.Column(sqlalchemy.types.Integer)
    height = sqlalchemy.Column(sqlalchemy.types.Integer)
    kind = sqlalchemy.Column(sqlalchemy.types.String(STRING_LEN))
    breed = sqlalchemy.Column(sqlalchemy.types.String(STRING_LEN))
    chip_id = sqlalchemy.Column(sqlalchemy.types.Integer)

    birthday = sqlalchemy.Column(sqlalchemy.types.Date)
    discovery_day = sqlalchemy.Column(sqlalchemy.types.Date)
    discovery_place = sqlalchemy.Column(sqlalchemy.types.String(STRING_LEN))

    description = sqlalchemy.Column(sqlalchemy.types.Text)

    # TODO events
