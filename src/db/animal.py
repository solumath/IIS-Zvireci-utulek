from datetime import date
from .constants import STRING_LEN, db
from sqlalchemy.orm import relation


class Animal(db.Model):
    """
    Table for animal, 
    contains basic info about animal
    connects to Event table for history of animal
    """
    __tablename__ = "animal"
    id = db.Column(db.Integer,
                   primary_key=True, autoincrement=True)

    name = db.Column(db.String(STRING_LEN))
    sex = db.Column(db.String(STRING_LEN))
    color = db.Column(db.String(STRING_LEN))
    weight = db.Column(db.Integer)
    height = db.Column(db.Integer)
    kind = db.Column(db.String(STRING_LEN))
    breed = db.Column(db.String(STRING_LEN))
    chip_id = db.Column(db.Integer)

    birthday = db.Column(db.Date)
    discovery_day = db.Column(db.Date)
    discovery_place = db.Column(db.String(STRING_LEN))

    description = db.Column(db.Text)

    image = db.Column(db.String(STRING_LEN * 4))

    events = relation("Event", back_populates="animal")

    def __init__(self, name: str, sex: str, color: str,
                 weight: int, height: int, kind: str, breed: str,
                 chip_id: int, birthday: date, discovery_day: date,
                 discovery_place: str, description: str, image: str = ""):
        """initializes row for table animal"""
        self.name = name
        self.sex = sex
        self.color = color
        self.weight = weight
        self.height = height
        self.kind = kind
        self.breed = breed
        self.chip_id = chip_id
        self.birthday = birthday
        self.discovery_day = discovery_day
        self.discovery_place = discovery_place
        self.description = description
        self.image = image
