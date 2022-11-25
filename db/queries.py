from .constants import db
from .animal import Animal
from .user import User
from .event import Event
from .record_type import RecordType
from .user_role import UserRole
from .walk import Walk
from .medical import MedicalRecord

import flask_login
from datetime import datetime
import typing


# ====================================================================================================
# ANIMALS


def get_animal(id: int):
    """
        returns animal with id, or None if not found
    """
    return db.session.query(Animal).get(id)


def get_animals():
    """
        returns serialized array of all animals,
    """
    result = db.session.query(Animal).all()

    return result


# ====================================================================================================
# USERS


def get_user(id):
    """
        returns user with id, or None if not found
    """
# ====================================================================================================
# EVENTS

    return db.session.query(User).get(id)


def get_users(login: str = None, email: str = None, name: str = None, surname: str = None, role: typing.Union[str, UserRole] = None) -> list[User]:
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

    if isinstance(role, str):
        role = db.session.query(UserRole).filter(UserRole.name == role).first()

    if isinstance(role, UserRole):
        query = query.filter(User.user_role == role)

    return query.all()


# ====================================================================================================
# USERS ROLES


def get_user_role(name: str):
    return db.session.query(UserRole).filter(UserRole.name == name).first()


def get_user_roles():
    return db.session.query(UserRole).all()


# ====================================================================================================
# EVENTS


def get_event(id):
    """
        returns user with id, or None if not found
    """
    return db.session.query(Event).get(id)


def get_events_query(user=None, animal=None):
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

    return query


def get_past_events(user=None, animal=None):
    """
        returns serialized array of events that will end in future,
        default returns all,
        if any of arguments is set (user, animal, event_type), filter events by them
    """

    query = get_events_query(user, animal)
    return query.filter(Event.end < datetime.now()).all()


def get_future_events(user=None, animal=None):
    """
        returns serialized array of events that already ended,
        default returns all,
        if any of arguments is set (user, animal, event_type), filter events by them
    """

    query = get_events_query(user, animal)
    return query.filter(Event.end > datetime.now()).all()


# ====================================================================================================
# WALKS


def get_walks_query(user=None, animal=None):
    """
        returns query for events
    """

    query = db.session.query(Walk)

    if isinstance(user, int):
        user = db.session.query(User).get(user)
    if isinstance(user, User):
        query = query.filter(Walk.user == user)

    if isinstance(animal, int):
        animal = db.session.query(Animal).get(animal)
    if isinstance(animal, Animal):
        query = query.filter(Walk.animal == animal)

    return query


def get_walks(user=None, animal=None):
    query = get_walks_query(user, animal)
    return query.all()


def get_future_walks(user=None, animal=None):
    query = get_walks_query(user, animal)
    return query.filter(Walk.end > datetime.now()).all()


def get_past_walks(user=None, animal=None):
    query = get_walks_query(user, animal)
    return query.filter(Walk.end < datetime.now()).all()


# ====================================================================================================
# MY WALKS


def get_my_walks(animal=None):
    return get_walks(flask_login.current_user, animal)


def get_future_my_walks(animal=None):
    return get_future_walks(flask_login.current_user, animal)


def get_past_my_walks(animal=None):
    return get_past_walks(flask_login.current_user, animal)


# ====================================================================================================
# RECORD TYPES


def get_record_types():
    return db.session.query(RecordType).all()


def get_record_tpye(id: typing.Union[int, str]):
    if isinstance(id, int):
        return db.session.query(RecordType).get(id)
    if isinstance(id, str):
        return db.session.query(RecordType).filter(RecordType.name == id)

    # ====================================================================================================
    # MEDICAL RECORDS


def get_medical_records(user=None, animal=None, record_type=None):
    query = db.session.query(MedicalRecord)

    if isinstance(user, int):
        user = db.session.query(User).get(user)
    if isinstance(user, User):
        query = query.filter(MedicalRecord.user == user)

    if isinstance(animal, int):
        animal = db.session.query(Animal).get(animal)
    if isinstance(animal, Animal):
        query = query.filter(MedicalRecord.animal == animal)

    if isinstance(record_type, int) or isinstance(record_type, str):
        record_type = get_record_tpye(record_type)
    if isinstance(record_type, RecordType):
        query = query.filter(MedicalRecord.record_type == record_type)

    return query.all()
