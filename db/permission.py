from .constants import STRING_LEN, db
from sqlalchemy.orm import relation


class Permission(db.Model):
    __tablename__ = "permission"
    user_role_id = db.Column(db.String(STRING_LEN), db.ForeignKey(
        "user_role.id"), primary_key=True)
    action = db.Column(db.Integer)

    user_role = relation("UserRole", back_populates="permissions")

    def __init__(self, action: int):
        self.action = action
