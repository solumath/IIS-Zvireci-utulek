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
    db.Animal("Gutenberg", "samec", "hnědá", 15, 40, "pes", "Kříženec", 15000,
              date(2015, 12, 2), date(2019, 1, 2), "Božetechova 2", "Hravý a přátelský pes nalezen uvázaný na přednášce IIS, doživotní trauma."),

    db.Animal("Salátek", "samec", "černá", 40, 80, "pes", "Dobrman", 15001,
              date(2020, 12, 6), date(2022, 1, 2), "Kolejní 2", "Velký černý pes, který má rád dlouhé procházky."),

    db.Animal("Mrkvička", "samice", "bílá", 5, 30, "kočka", "Ragdoll", 15002,
              date(2021, 2, 2), date(2022, 1, 2), "Purkyňova 93", "Agresivní malá kočka s alergií na ryby."),

    db.Animal("Oscar", "samec", "modrá", 0.01, 5, "ryba", "Bojovka", 15003,
              date(2022, 2, 8), date(2022, 10, 2), "Mánesova 2524/12", "Rybka většího vzrůstu, musí být v akvárku sama."),

    db.Animal("Rozárka", "samice", "barevná", 3, 35, "kočka", "Kříženec", 15004,
              date(2015, 12, 2), date(2019, 1, 2), "Kounicova 46/48", "Mourovaté koťátko nalezené v odpadcích."),

    db.Animal("Jurko", "samec", "růžová", 20, 65, "prase", "miniaturní prasátko", 15005,
              date(2021, 12, 2), date(2022, 10, 2), "Božetěchova 2", "Malé smradlavé prasátko, nemá rádo koupel."),

    db.Animal("Alex", "samec", "šedá", 50, 90, "pes", "Doga", 15006,
              date(2020, 12, 2), date(2022, 1, 2), "Božetechova 2", "Milý pes většího vzrůstu, vhodný k dětem."),

    db.Animal("Punťa", "samec", "hnědá", 5, 20, "pes", "Čivava", 15007,
              date(2010, 12, 2), date(2019, 1, 2), "Božetechova 2", "Psí důchodce, který by rád dožil svůj život v milující rodině."),

    db.Animal("Rex", "samec", "zlatá", 25, 60, "pes", "Zlatý retrívr", 15008,
              date(2022, 9, 2), date(2022, 10, 30), "Božetechova 2", "Štěně bez základního výcviku, které potřebuje pravidelný kontakt s lidmi.")
]

admin_user = db.User("admin", "tryhards",  "Martin", "Kneslik", "Berkova 54",
                     "m.kneslik@utulek.cz", "+420603334197", 11)

vet_user = db.User("vet", "treehards",  "Martin", "Kneslík", "Berkova 54",
                   "asdds@utulek.cz", "+420603334197", 10)

caretaker_user = db.User("caretaker", "1234",  "Ahmed", "Prdík", "Revoluční 1820",
                         "ahm.prd@utulek.cz", "+420721059221", 10)

volunteer_user = db.User("volunteer", "abcd",  "Jolanda", "Veliká", "Breberkova 1420",
                         "jolis.velis@utulek.cz", "+420603674100", 9)

unverified_user = db.User("unverified", "poop",  "Juraj", "Prdelkový", "Vysoké Tatry 4",
                          "jurik.prdelka@utulek.cz", "+421913677100", 8)

event_types = [
    db.Event_type(
        "procházka", 1, "Vzití zviřete mimo útulek s povinnosti navrácení v předem určený čas."),
    db.Event_type("vyšetření", 9,
                  "Vyšetrení zvířete odborným pracovníkem (veterinářem)."),
    db.Event_type(
        "salón", 5, "Návštěva psího salónu s cílem vylepšení vzhledu zvířete (koupel, stříhání srsti, stříhání drápků).")
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

    for animal in animals:
        db.db.session.add(animal)

    for event_type in event_types:
        db.db.session.add(event_type)

    for event in events:
        db.db.session.add(event)

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
