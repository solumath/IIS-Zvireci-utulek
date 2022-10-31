from datetime import date
import db

role_admin = db.User_role(name="administrator", description="""
            - has highest permissions""")

role_caretaker = db.User_role(name="caretaker", description="""
            - manages animals
            - creates walking timetables
            - verifies volunteers
            - approves animal bookings
            - creates veterinarian requests""")

role_vet = db.User_role(name="veterinarian", description="""
            - has access to medical records, 
            - performs medical procedures""")

role_volunteer = db.User_role(name="volunteer", description="""
            - can book animal for a walk 
            - can see his history""")

role_unverified = db.User_role(name="unverified", description="""
            - unverified volunteer
            - awaits verification""")

user_roles = [
    role_admin,
    role_caretaker,
    role_vet,
    role_volunteer,
    role_unverified,
]

animals = [
    db.Animal("Gutenberg", "male", "brown", 15, 40, "dog ?", "dog with 4 legs", 15,
              date(2015, 12, 2), date(2019, 1, 2), "Bozetechova 2", "It is a dog."),
    # TODO add animals
]

admin_user = db.User("admin", "tryhards", "martin", "kneslik", "Berkova 54",
                     "m.kneslik@utulek.cz", "+420603334197", 10, True)

vet_user = db.User("vet", "treehards", "martin", "kneslik", "Berkova 54",
                   "m.kneslik@utulek.cz", "+420603334197", 10, True)
# TODO add users (caretaker, volunteer, unverified)

event_types = [
    # TODO add event_types (2-3)
]

events = [
    # TODO add events (2-3)
]


def add_data():
    for role in user_roles:
        db.db.session.add(role)

    admin_user.user_role = role_admin
    db.db.session.add(admin_user)

    vet_user.user_role = role_vet
    db.db.session.add(vet_user)

    # TODO add users to db
    # TODO add event types to db
    # TODO add events to db (event.event_type = evetn_type)

    # must be last, commits all changes to database
    db.db.session.commit()


if __name__ == "__main__":
    import app
    with app.app.app_context():
        db.db.drop_all()
        db.db.create_all()

        add_data()
