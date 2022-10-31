from .constants import STRING_LEN, db
from sqlalchemy.orm import relation


class User_role(db.Model):
    __tablename__ = "user_role"
    id = db.Column(db.Integer,
                   primary_key=True, autoincrement=True)

    name = db.Column(db.String(STRING_LEN), unique=True)
    description = db.Column(db.Text)

    users = relation("User", back_populates="user_role")
    permissions = relation("Permission", back_populates="user_role")

    def __init__(self, name: str, description: str = ""):
        self.name = name
        self.description = description

    def __repr__(self):
        return self.name


role_admin = User_role(name="administrator", description="""
            - has highest permissions""")

role_caretaker = User_role(name="caretaker", description="""
            - manages animals
            - creates walking timetables
            - verifies volunteers
            - approves animal bookings
            - creates veterinarian requests""")

role_vet = User_role(name="veterinarian", description="""
            - has access to medical records, 
            - performs medical procedures""")

role_volunteer = User_role(name="volunteer", description="""
            - can book animal for a walk 
            - can see his history""")

role_unverified = User_role(name="unverified", description="""
            - unverified volunteer
            - awaits verification""")
