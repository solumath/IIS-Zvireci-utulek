from .login import login, logout
from .routes import about, index, not_enough_perms, page_not_found
from .animals import animals, animals_add, animals_detail, animals_edit, animals_medical_record, request_walk
from .users import users, users_edit, users_delete
from .walks import walks, walks_delete
from .my_walks import my_walks, my_walks_delete
from .medical_records import medical_records, medical_records_add, medical_records_delete, medical_records_edit
from .profile import profile, profile_edit, profile_password
from .examination_requests import examination_requests, examination_requests_accept, examination_requests_decline, \
    examination_requests_delete, examination_requests_perform
