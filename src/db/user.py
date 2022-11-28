from .constants import STRING_LEN, db
from sqlalchemy.orm import relation
from flask_login import UserMixin


class User(db.Model, UserMixin):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    login = db.Column(db.String(STRING_LEN), unique=True)
    password = db.Column(db.String(STRING_LEN))
    email = db.Column(db.String(STRING_LEN), unique=True)

    authenticated = db.Column(db.Boolean, default=False)

    name = db.Column(db.String(STRING_LEN))
    surname = db.Column(db.String(STRING_LEN))
    address = db.Column(db.String(STRING_LEN))
    tel_number = db.Column(db.String(STRING_LEN))

    role_id = db.Column(db.Integer, db.ForeignKey("user_role.id"))

    user_role = relation("UserRole", back_populates="users")
    events = relation("Event", back_populates="user")
    session = relation("Session", back_populates="user", uselist=False)

    @property
    def is_active(self):
        return True

    @property
    def is_authenticated(self):
        return self.authenticated

    @property
    def is_anonymous(self):
        return False

    @property
    def verified(self):
        return self.user_role.name != "unverified"
    
    @property
    def volunteer(self):
        return self.user_role.name == "volunteer"

    def __init__(self, login, password, name, surname, address, email, tel_number):
        self.login = login
        self.password = password
        self.name = name
        self.surname = surname
        self.address = address
        self.email = email
        self.tel_number = tel_number

    def __repr__(self) -> str:
        return f"login: {self.login}, role {self.user_role}"

    def get_info(self) -> dict:
        return {
            "Jméno": f"{self.name} {self.surname}",
            "Bydliště": self.address,
            "Email": self.email,
            "Telefon": self.tel_number,
            "Ověřen": "Ano" if not self.user_role.name == "unverified" else "Ne",
            "Role": self.user_role.czech_name
        }

    def get_id(self):
        return self.login

    def __eq__(self, other):
        """
        Checks the equality of two `UserMixin` objects using `get_id`.
        """
        if isinstance(other, UserMixin):
            return self.get_id() == other.get_id()
        return NotImplemented

    def __ne__(self, other):
        """
        Checks the inequality of two `UserMixin` objects using `get_id`.
        """
        equal = self.__eq__(other)
        if equal is NotImplemented:
            return NotImplemented
        return not equal
