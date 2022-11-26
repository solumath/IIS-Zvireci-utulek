"""
Database :ez:
"""

from .constants import db

from .user_role import UserRole
from .user import User
from .permission import Permission
from .event import Event
from .record_type import RecordType
from .animal import Animal
from .session import Session
from .walk import Walk
from .medical import MedicalRecord


from .queries import \
    get_animal, \
    get_animals, \
    get_event, \
    get_events_query, \
    get_past_events, \
    get_future_events, \
    get_user, \
    get_users, \
    get_user_role, \
    get_user_roles, \
    get_future_my_walks, \
    get_future_walks, \
    get_my_walks, \
    get_past_my_walks, \
    get_past_walks, \
    get_walks, \
    get_walks_query, \
    get_record_type, \
    get_record_types, \
    get_medical_record, \
    get_medical_records, \
    get_medical_records_query, \
    get_future_medical_records, \
    get_past_medical_records


from .constants import \
    PERMISSION_ANIMALS_SHOW, \
    PERMISSION_ANIMALS_DELETE, \
    PERMISSION_ANIMALS_EDIT, \
    PERMISSION_ANIMALS_ADD, \
    PERMISSION_USERS_SHOW, \
    PERMISSION_USERS_EDIT, \
    PERMISSION_USERS_VERIFY, \
    PERMISSION_USERS_ADD, \
    PERMISSION_USERS_DELETE, \
    PERMISSION_EVENTS_SHOW, \
    PERMISSION_EVENTS_DELETE, \
    PERMISSION_EVENTS_EDIT, \
    PERMISSION_EVENTS_ADD, \
    PERMISSION_WALKS_SHOW, \
    PERMISSION_WALKS_ADD, \
    PERMISSION_WALKS_DELETE, \
    PERMISSION_WALKS_CONFIRM, \
    PERMISSION_MY_WALKS_SHOW, \
    PERMISSION_MY_WALKS_ADD, \
    PERMISSION_MY_WALKS_DELETE, \
    PERMISSION_EXAMINATIONS_SHOW, \
    PERMISSION_EXAMINATIONS_ADD, \
    PERMISSION_EXAMINATIONS_EDIT, \
    PERMISSION_EXAMINATIONS_DELETE
