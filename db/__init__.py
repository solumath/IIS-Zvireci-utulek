"""
Database :ez:
"""

from .constants import db

from .user_role import UserRole
from .user import User
from .permission import Permission
from .event import Event
from .event_type import EventType
from .animal import Animal
from .session import Session

from .queries import get_animals, get_past_events, get_future_events, get_animal, get_user, get_users
