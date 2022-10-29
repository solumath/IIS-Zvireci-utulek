from .constants import STRING_LEN, db
from sqlalchemy.orm import relation


class Permission(db.Model):
    __tablename__ = "permission"
    user_role_id = db.Column(db.String(STRING_LEN), db.ForeignKey(
        "user_role.id"), primary_key=True)
    event_type_id = db.Column(db.String(STRING_LEN), db.ForeignKey(
        "event_type.id"), primary_key=True)
    action = db.Column(db.Integer)

    user_role = relation("User_role", back_populates="permissions")
    event_type = relation("Event_type", back_populates="permissions")

    def __init__(self, actions: int):
        self.action = actions

    def has_permision(self, action):
        return True if action ^ self.action else False
