from .constants import STRING_LEN, db
from sqlalchemy.orm import relation
import marshmallow as ma
from flask_login import UserMixin


class User(db.Model):
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

    rating = db.Column(db.Integer)

    role_id = db.Column(db.Integer, db.ForeignKey("user_role.id"))

    user_role = relation("User_role", back_populates="users")
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

    # created_at = db.Column(
    #     db.DateTime, default=db.func.now())
    # updated_at = db.Column(
    #     db.DateTime, default=db.func.now(), onupdate=db.func.now())

    def __init__(self, login, password, name, surname, address, email, tel_number, rating=0):
        self.login = login
        self.password = password
        self.name = name
        self.surname = surname
        self.address = address
        self.email = email
        self.tel_number = tel_number
        self.rating = rating

    def __repr__(self) -> str:
        return f"login: {self.login}, role {self.user_role}"
    
    def get_info(self) -> dict:
        return {
            "Jméno": f"{self.name} {self.surname}",
            "Bydliště": self.address,
            "email": self.email,
            "Telefon": self.tel_number,
            "Hodnocení": self.rating
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


class User_Schema(ma.Schema):
    pass

# class UserSchema(ma.Schema):
#     class Meta:
#         fields = ('id', 'login', 'password', 'name', 'surname', 'address', 'email', 'tel_number', 'rating', 'verified')

# user_schema = UserSchema()
# users_schema = UserSchema(many=True)
