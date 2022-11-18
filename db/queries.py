from .constants import db
from .animal import Animal
from .user import User
from .event import Event
from .event_type import EventType
from datetime import datetime


# ====================================================================================================
# ANIMALS


def get_animal(id: int) -> Animal | None:
    """
        returns animal with id, or None if not found
    """
    return db.session.query(Animal).get(id)


def get_animals() -> list[Animal]:
    """
        returns serialized array of all animals,
    """
    result = db.session.query(Animal).all()

    return result


# ====================================================================================================
# USERS


def get_user(id) -> User | None:
    """
        returns user with id, or None if not found
    """
    return db.session.query(User).get(id)


def get_users(login: str = None, email: str = None, name: str = None, surname: str = None) -> list[User]:
    """
        return array of users,
        if some of the arguments are set, filter by them
    """
    query = db.session.query(User)

    if isinstance(login, str):
        query = query.filter(User.login == login)

    if isinstance(email, str):
        query = query.filter(User.email == email)

    if isinstance(name, str):
        query = query.filter(User.name == name)

    if isinstance(surname, str):
        query = query.filter(User.surname == surname)

    return query.all()


# ====================================================================================================
# EVENTS


def get_events_query(user: User | int = None, animal: Animal | int = None, event_type: EventType | int = None):
    """
        returns query for events
    """

    query = db.session.query(Event)

    if isinstance(user, int):
        user = db.session.query(User).get(user)
    if isinstance(user, User):
        query = query.filter(Event.user == user)

    if isinstance(animal, int):
        animal = db.session.query(Animal).get(animal)
    if isinstance(animal, Animal):
        query = query.filter(Event.animal == animal)

    if isinstance(event_type, int):
        event_type = db.session.query(EventType).get(event_type)
    if isinstance(event_type, Animal):
        query = query.filter(Event.animal == event_type)

    return query


def get_past_events(user: User | int = None, animal: Animal | int = None, event_type: EventType | int = None) -> list[Event]:
    """
        returns serialized array of events that will end in future,
        default returns all,
        if any of arguments is set (user, animal, event_type), filter events by them
    """

    query = get_events_query(user, animal, event_type)
    return query.filter(Event.end < datetime.now()).all()


def get_future_events(user: User | int = None, animal: Animal | int = None, event_type: EventType | int = None) -> list[Event]:
    """
        returns serialized array of events that already ended,
        default returns all,
        if any of arguments is set (user, animal, event_type), filter events by them
    """

    query = get_events_query(user, animal, event_type)
    return query.filter(Event.end < datetime.now()).all()
