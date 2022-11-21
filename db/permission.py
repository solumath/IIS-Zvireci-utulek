from .constants import STRING_LEN, db
from sqlalchemy.orm import relation


class Permission(db.Model):
    __tablename__ = "permission"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_role_id = db.Column(db.Integer, db.ForeignKey(
        "user_role.id"))
    action = db.Column(db.Integer)

    user_role = relation("UserRole", back_populates="permissions")

    def __init__(self, action: int):
        self.action = action
