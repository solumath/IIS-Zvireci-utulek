from .user_role import UserRole
from .user import User
from .permission import Permission
from .event import Event
from .event_type import EventType
from .animal import Animal
from .session import Session

import marshmallow as ma


class AnimalSchema(ma.Schema):
    id = ma.fields.Int()
    name = ma.fields.Str()
    sex = ma.fields.Str()
    color = ma.fields.Str()
    weight = ma.fields.Int()
    height = ma.fields.Int()
    kind = ma.fields.Str()
    breed = ma.fields.Str()
    chip_id = ma.fields.Int()
    birthday = ma.fields.DateTime()
    discovery_day = ma.fields.DateTime()
    discovery_place = ma.fields.Str()
    description = ma.fields.Str()


class EventTypeSchema(ma.Schema):
    id = ma.fields.Int()
    name = ma.fields.Str()
    priority = ma.fields.Int()
    description = ma.fields.Str()


class EventSchema(ma.Schema):
    id = ma.fields.Int()
    start = ma.fields.DateTime()
    end = ma.fields.DateTime()
    description = ma.fields.Str()
    animal = ma.fields.Nested(AnimalSchema)
    event_type = ma.fields.Nested(EventTypeSchema(only=("name",)))
    # user = ma.fields.Nested()
