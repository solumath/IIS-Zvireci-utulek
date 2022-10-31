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
    db.Animal("Gutenberg", "male", "brown", 15, 40, "dog", "dog with 4 legs", 15000,
              date(2015, 12, 2), date(2019, 1, 2), "Bozetechova 2", "Je to pes."),

    db.Animal("Salatek", "male", "black", 40, 80, "dog", "dobrman", 15001,
              date(2020, 12, 6), date(2022, 1, 2), "Bozetechova 2", "Velky cerny pes."),

    db.Animal("Mrkvicka", "female", "white", 5, 30, "cat", "ragdoll", 15002,
              date(2021, 2, 2), date(2022, 1, 2), "Bozetechova 2", "Agresivni mala kocka."),
    
    db.Animal("Oscar", "male", "blue", 0.01, 5, "fish", "bojovka", 15003,
              date(2022, 2, 8), date(2022, 10, 2), "Bozetechova 2", "Divna velka rybka."),

    db.Animal("Rozarka", "female", "tabby", 3, 35, "cat", "unknown", 15004,
              date(2015, 12, 2), date(2019, 1, 2), "Bozetechova 2", "Kotatko nalezene v odpadcich."),

    db.Animal("Jurko", "male", "pink", 20, 65, "pig", "miniature pig", 15005,
              date(2021, 12, 2), date(2022, 10, 2), "Bozetechova 2", "Male smradlave prasatko.")
    # TODO add animals
]

admin_user = db.User("admin", "tryhards", "martin", "kneslik", "Berkova 54",
                     "m.kneslik@utulek.cz", "+420603334197", 10, True)

vet_user = db.User("vet", "treehards", "martin", "kneslik", "Berkova 54",
                   "m.kneslik@utulek.cz", "+420603334197", 10, True)

caretaker_user = db.User("caretaker", "1234", "Ahmed", "Prdik", "Revolucni 1820",
                    "ahm.prd@utulek.cz", "+420721059221", 10, True)

volunteer_user = db.User("volunteer", "abcd", "Jolanda", "Velika", "Breberkova 1420",
                   "jolis.velis@utulek.cz", "+420603674100", 9, True)

unverified_user = db.User("unverified", "poop", "Juraj", "Prdelkovy", "Vysoke Tatry 4",
                   "jurik.prdelka@utulek.cz", "+421913677100", 8, False)


# TODO add more users

event_types = [
    db.event_type("prochazka", 1, "Vziti zvirete mimo utulek s povinnosti navraceni."),
    db.event_type("vysetreni", 9, "Vysetreni zvirete odbornym pracovnikem.")
    # TODO more add event_types
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

    caretaker_user.user_role = role_caretaker
    db.db.session.add(caretaker_user)

    volunteer_user.user_role = role_volunteer
    db.db.session.add(volunteer_user)

    # TODO add users to db
    # TODO add event types to db
    # TODO add events to db (event.event_type = event_type)

    # must be last, commits all changes to database
    db.db.session.commit()


if __name__ == "__main__":
    import app
    with app.app.app_context():
        db.db.drop_all()
        db.db.create_all()

        add_data()
