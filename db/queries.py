from .constants import db
from .animal import Animal
from .user import User
from .event import Event
from .event_type import EventType
from .schemas import *


def get_animals(filter: str = None):
    """
        returns serialized array of animals,
        filter not yet implemented
    """
    schema = AnimalSchema()
    if filter is None:
        result = db.session.query(Animal).all()
    else:
        result = []
    return schema.dump(result, many=True)


def get_past_events(user: User | int = None, animal: Animal = None, event_type: EventType = None):
    """
        returns serialized array of events,
        default returns all,
        if any of arguments is set (user, animal, event_type), filter events by them
    """

    query = db.session.query(Event)
    if isinstance(user, int):
        user = db.session.query(User).get(user)
        print(user)
    if isinstance(user, User):
        query = query.filter(Event.user == user)
    if animal is not None:
        query = query.filter(Event.animal == animal)
    if event_type is not None:
        query = query.filter(Event.event_type == event_type)

    schema = EventSchema(
        only=("start", "end", "description", "animal.name", "animal.id"))

    return schema.dump(query.all(), many=True)
