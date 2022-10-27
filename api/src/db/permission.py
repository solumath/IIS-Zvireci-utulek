from ..main import db
from .constants import STRING_LEN
import sqlalchemy


class permission(db.Model):
    __tablename__ = "permission"
    user_role_id = sqlalchemy.Column(sqlalchemy.types.String(STRING_LEN), sqlalchemy.ForeignKey(
        "user_role.id"), primary_key=True)
    event_type_id = sqlalchemy.Column(sqlalchemy.types.String(STRING_LEN), sqlalchemy.ForeignKey(
        "event_type.id"), primary_key=True)
    action = sqlalchemy.Column(sqlalchemy.types.Integer)

    def has_permision(self, action):
        return True if action ^ self.action else False
