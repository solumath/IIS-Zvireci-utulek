from .constants import STRING_LEN, db
from sqlalchemy.orm import relation


class UserRole(db.Model):
    __tablename__ = "user_role"
    id = db.Column(db.Integer,
                   primary_key=True, autoincrement=True)

    name = db.Column(db.String(STRING_LEN), unique=True)
    czech_name = db.Column(db.String(STRING_LEN), unique=True)

    description = db.Column(db.Text)

    users = relation("User", back_populates="user_role")
    permissions = relation("Permission", back_populates="user_role")

    def __init__(self, name: str, czech_name: str, description: str = ""):
        self.name = name
        self.description = description

    def __repr__(self):
        return self.name
