from ..main import db
from .constants import STRING_LEN
import sqlalchemy


class user_role(db.Model):
    __tablename__ = "user_role"
    id = sqlalchemy.Column(sqlalchemy.types.String(
        STRING_LEN), primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.types.String(STRING_LEN))

    description = sqlalchemy.Column(sqlalchemy.types.Text)
