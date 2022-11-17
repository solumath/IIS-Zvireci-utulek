from .constants import STRING_LEN, db
from sqlalchemy.orm import relation
# import marshmallow as ma


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    login = db.Column(db.String(STRING_LEN), unique=True)
    password = db.Column(db.String(STRING_LEN))

    name = db.Column(db.String(STRING_LEN))
    surname = db.Column(db.String(STRING_LEN))
    address = db.Column(db.String(STRING_LEN))
    email = db.Column(db.String(STRING_LEN))
    tel_number = db.Column(db.String(STRING_LEN))

    rating = db.Column(db.Integer)

    role_id = db.Column(db.Integer, db.ForeignKey("user_role.id"))

    user_role = relation("User_role", back_populates="users")
    events = relation("Event", back_populates="user")
    session = relation("Session", back_populates="user", uselist=False)

    # created_at = db.Column(
    #     db.DateTime, default=db.func.now())
    # updated_at = db.Column(
    #     db.DateTime, default=db.func.now(), onupdate=db.func.now())

    def __init__(self, login, password, name, surname, address, email, tel_number, rating=0, verified=False):
        self.login = login
        self.password = password
        self.name = name
        self.surname = surname
        self.address = address
        self.email = email
        self.tel_number = tel_number
        self.rating = rating

    def __repr__(self) -> str:
        return "login: %10s, role %10r" % (self.login, self.user_role)


# class UserSchema(ma.Schema):
#     class Meta:
#         fields = ('id', 'login', 'password', 'name', 'surname', 'address', 'email', 'tel_number', 'rating', 'verified')

# user_schema = UserSchema()
# users_schema = UserSchema(many=True)
