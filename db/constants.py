import flask_sqlalchemy
import sqlalchemy_imageattach.stores.fs

store = sqlalchemy_imageattach.stores.fs.HttpExposedFileSystemStore(
    path='images'
)


STRING_LEN = 128

db = flask_sqlalchemy.SQLAlchemy()

# ANIMALS
PERMISSION_ANIMALS_SHOW = 1
PERMISSION_ANIMALS_DELETE = 2
PERMISSION_ANIMALS_EDIT = 3
PERMISSION_ANIMALS_ADD = 4


# USERS
PERMISSION_USERS_SHOW = 11
PERMISSION_USERS_EDIT = 12
PERMISSION_USERS_VERIFY = 13  # ok
PERMISSION_USERS_ADD = 14
PERMISSION_USERS_DELETE = 15

# EVENTS
PERMISSION_EVENTS_SHOW = 21
PERMISSION_EVENTS_DELETE = 22
PERMISSION_EVENTS_EDIT = 23
PERMISSION_EVENTS_ADD = 24

# WALKS
PERMISSION_WALKS_SHOW = 31
PERMISSION_WALKS_ADD = 32
PERMISSION_WALKS_DELETE = 33
PERMISSION_WALKS_CONFIRM = 34

# EXAMINATIOS
PERMISSION_EXAMINATIONS_SHOW = 41
