from ..main import db
from .constants import STRING_LEN
import sqlalchemy


class user(db.Model):
    __tablename__ = "user"
    id = sqlalchemy.Column(sqlalchemy.types.String(
        STRING_LEN), primary_key=True)
    login = sqlalchemy.Column(sqlalchemy.types.String(STRING_LEN))
    password = sqlalchemy.Column(sqlalchemy.types.String(STRING_LEN))

    name = sqlalchemy.Column(sqlalchemy.types.String(STRING_LEN))
    surname = sqlalchemy.Column(sqlalchemy.types.String(STRING_LEN))
    address = sqlalchemy.Column(sqlalchemy.types.String(STRING_LEN))
    email = sqlalchemy.Column(sqlalchemy.types.String(STRING_LEN))
    tel_number = sqlalchemy.Column(sqlalchemy.types.String(STRING_LEN))

    rating = sqlalchemy.Column(sqlalchemy.types.Integer)

    verified = sqlalchemy.Column(sqlalchemy.types.Boolean)
