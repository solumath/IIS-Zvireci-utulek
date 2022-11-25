from datetime import date, datetime
import db

admin_role = db.UserRole(name="administrator", czech_name="administrátor", description="""
            - has highest permissions""")

caretaker_role = db.UserRole(name="caretaker", czech_name="pečovatel", description="""
            - manages animals
            - creates walking timetables
            - verifies volunteers
            - approves animal bookings
            - creates veterinarian requests""")

vet_role = db.UserRole(name="veterinarian", czech_name="veterinář", description="""
            - has access to medical records, 
            - performs medical procedures""")

volunteer_role = db.UserRole(name="volunteer", czech_name="dobrovolník", description="""
            - can book animal for a walk 
            - can see his history""")

unverified_role = db.UserRole(name="unverified", czech_name="neověřený uživatel", description="""
            - unverified volunteer
            - awaits verification""")


admin_permissions = [
    db.PERMISSION_ANIMALS_SHOW,
    db.PERMISSION_ANIMALS_DELETE,
    db.PERMISSION_ANIMALS_EDIT,
    db.PERMISSION_ANIMALS_ADD,

    db.PERMISSION_USERS_SHOW,
    db.PERMISSION_USERS_EDIT,
    db.PERMISSION_USERS_VERIFY,
    db.PERMISSION_USERS_ADD,
    db.PERMISSION_USERS_DELETE,

    db.PERMISSION_EVENTS_SHOW,
    db.PERMISSION_EVENTS_DELETE,
    db.PERMISSION_EVENTS_EDIT,
    db.PERMISSION_EVENTS_ADD,

    db.PERMISSION_WALKS_SHOW,
    db.PERMISSION_WALKS_ADD,
    db.PERMISSION_WALKS_DELETE,
    db.PERMISSION_WALKS_CONFIRM,

    db.PERMISSION_MY_WALKS_SHOW,
    db.PERMISSION_MY_WALKS_ADD,
    db.PERMISSION_MY_WALKS_DELETE,

    db.PERMISSION_EXAMINATIONS_SHOW,
    db.PERMISSION_EXAMINATIONS_ADD,
    db.PERMISSION_EXAMINATIONS_EDIT,
    db.PERMISSION_EXAMINATIONS_DELETE,
]

caretaker_permissions = [
    db.PERMISSION_ANIMALS_SHOW,
    db.PERMISSION_ANIMALS_DELETE,
    db.PERMISSION_ANIMALS_EDIT,
    db.PERMISSION_ANIMALS_ADD,

    db.PERMISSION_USERS_SHOW,
    db.PERMISSION_USERS_VERIFY,

    db.PERMISSION_EVENTS_SHOW,
    db.PERMISSION_EVENTS_DELETE,
    db.PERMISSION_EVENTS_EDIT,
    db.PERMISSION_EVENTS_ADD,

    db.PERMISSION_WALKS_SHOW,
    db.PERMISSION_WALKS_ADD,
    db.PERMISSION_WALKS_DELETE,
    db.PERMISSION_WALKS_CONFIRM,

    db.PERMISSION_MY_WALKS_SHOW,
    db.PERMISSION_MY_WALKS_ADD,
    db.PERMISSION_MY_WALKS_DELETE,

    db.PERMISSION_EXAMINATIONS_SHOW,
    db.PERMISSION_EXAMINATIONS_ADD,
    db.PERMISSION_EXAMINATIONS_EDIT,
    db.PERMISSION_EXAMINATIONS_DELETE,
]

volunteer_permissions = [
    db.PERMISSION_ANIMALS_SHOW,

    db.PERMISSION_MY_WALKS_SHOW,
    db.PERMISSION_MY_WALKS_ADD,
    db.PERMISSION_MY_WALKS_DELETE,
]

vet_permissions = [
    db.PERMISSION_ANIMALS_SHOW,

    db.PERMISSION_MY_WALKS_SHOW,
    db.PERMISSION_MY_WALKS_ADD,
    db.PERMISSION_MY_WALKS_DELETE,

    db.PERMISSION_EXAMINATIONS_SHOW,
    db.PERMISSION_EXAMINATIONS_ADD,
    db.PERMISSION_EXAMINATIONS_EDIT,
    db.PERMISSION_EXAMINATIONS_DELETE,
]

unverified_permissions = [
    db.PERMISSION_ANIMALS_SHOW,
]

animals = [
    db.Animal("Gutenberg", "samec", "hnědá", 15, 40, "pes", "Kříženec", 15000,
              date(2015, 12, 2), date(2019, 1, 2), "Božetechova 2", "Hravý a přátelský pes nalezen uvázaný na přednášce IIS, doživotní trauma."),

    db.Animal("Salátek", "samec", "černá", 40, 80, "pes", "Dobrman", 15001,
              date(2020, 12, 6), date(2022, 1, 2), "Kolejní 2", "Velký černý pes, který má rád dlouhé procházky."),

    db.Animal("Mrkvička", "samice", "bílá", 5, 30, "kočka", "Ragdoll", 15002,
              date(2021, 2, 2), date(2022, 1, 2), "Purkyňova 93", "Agresivní malá kočka s alergií na ryby."),

    db.Animal("Nemo", "samec", "oranžová, bílá", 0.01, 5, "ryba", "Klaun očkatý", 15003,
              date(2022, 2, 8), date(2022, 10, 2), "Mánesova 2524/12", "Rybka menšího vzrůstu. Hledá tátu."),

    db.Animal("Rozárka", "samice", "barevná", 3, 35, "kočka", "Kříženec", 15004,
              date(2015, 12, 2), date(2019, 1, 2), "Kounicova 46/48", "Mourovaté koťátko nalezené v odpadcích."),

    db.Animal("Jurko", "samec", "růžová", 20, 65, "prase", "miniaturní prasátko", 15005,
              date(2021, 12, 2), date(2022, 10, 2), "Božetěchova 2", "Malé smradlavé prasátko, nemá rádo koupel."),

    db.Animal("Alex", "samec", "šedá", 50, 90, "pes", "Doga", 15006,
              date(2020, 12, 2), date(2022, 1, 2), "Božetechova 2", "Milý pes většího vzrůstu, vhodný k dětem."),

    db.Animal("Punťa", "samec", "hnědá", 5, 20, "pes", "Čivava", 15007,
              date(2010, 12, 2), date(2019, 1, 2), "Božetechova 2", "Psí důchodce, který by rád dožil svůj život v milující rodině."),

    db.Animal("Arnik", "samec", "hnědá", 5, 20, "pes", "Srnčí ratlík", 15008,
              date(2010, 12, 2), date(2019, 1, 2), "Sportovní 9, Ivančice", "Pejsek, kterému nedávno umřela maminka a potřeboval by se v klidu dožít někde u rodiny s velkou zahrádkou."),

    db.Animal("Marlin", "samec", "oranžová, bílá", 0.01, 5, "ryba", "Klaun očkatý", 15009,
              date(2022, 2, 8), date(2022, 10, 2), "Mánesova 2524/12", "Marlin je opuštěná rybka, která hledá svého syna Nema."),

    db.Animal("Rex", "samec", "zlatá", 25, 60, "pes", "Zlatý retrívr", 15010,
              date(2022, 9, 2), date(2022, 10, 30), "Božetechova 2", "Štěně bez základního výcviku, které potřebuje pravidelný kontakt s lidmi.")
]

admin_user = db.User("admin", "tryhards",  "Martin", "Kneslik", "Berkova 54",
                     "m.kneslik@utulek.cz", "+420603334197")

vet_user = db.User("vet", "treehards",  "Martin", "Kneslík", "Berkova 54",
                   "asdds@utulek.cz", "+420603334197")

caretaker_user = db.User("caretaker", "1234",  "Ahmed", "Prdík", "Revoluční 1820",
                         "ahm.prd@utulek.cz", "+420721059221")

volunteer_user = db.User("volunteer", "abcd",  "Jolanda", "Veliká", "Breberkova 1420",
                         "jolis.velis@utulek.cz", "+420603674100")

unverified_user = db.User("unverified", "poop",  "Juraj", "Prdelkový", "Vysoké Tatry 4",
                          "jurik.prdelka@utulek.cz", "+421913677100")

record_types = [
    db.RecordType("examination", "vyšetření", 9,
                  "Vyšetrení zvířete odborným pracovníkem (veterinářem)."),
    db.RecordType("requested examination", "vyžádané vyšetření", 9,
                  "Vyšetření zvířete odborným pracovníkem (veterinářem) na žádost pečovatele."),
    db.RecordType("booster_shot", "očkování", 9,
                  "Očkování."),
    db.RecordType("medicine", "předepsaný lék", 9,
                  "Předpis léku předepsaný odborným pracovníkem (veterinářem)."),
]

walks = [
    db.Walk(datetime(2025, 1, 1), datetime(2025, 1, 1, 23)),
    db.Walk(datetime(2020, 1, 1), datetime(2020, 1, 1, 23)),
    db.Walk(datetime(2022, 11, 21, 15), datetime(2022, 11, 21, 17)),
    db.Walk(datetime(2022, 11, 20, 15), datetime(2022, 11, 21, 17)),
]

medical_records = [
    db.MedicalRecord(datetime(2025, 1, 1), datetime(
        2025, 1, 1, 23), "Bezna prohlidka"),
    db.MedicalRecord(datetime(2025, 1, 1), datetime(
        2025, 1, 1, 23), "request"),
    db.MedicalRecord(datetime(2025, 1, 1), datetime(
        2025, 1, 1, 23), "booster"),
    db.MedicalRecord(datetime(2025, 1, 1), datetime(
        2025, 1, 1, 23), "medicine"),
]


def add_role(role, permissions):
    db.db.session.add(role)
    for perm_code in permissions:
        permission = db.Permission(perm_code)
        permission.user_role = role
        db.db.session.add(permission)


def add_data():
    add_role(admin_role, admin_permissions)
    add_role(caretaker_role, caretaker_permissions)
    add_role(vet_role, vet_permissions)
    add_role(volunteer_role, volunteer_permissions)
    add_role(unverified_role, unverified_permissions)

    admin_user.user_role = admin_role
    db.db.session.add(admin_user)

    vet_user.user_role = vet_role
    db.db.session.add(vet_user)

    caretaker_user.user_role = caretaker_role
    db.db.session.add(caretaker_user)

    volunteer_user.user_role = volunteer_role
    db.db.session.add(volunteer_user)

    unverified_user.user_role = unverified_role
    db.db.session.add(unverified_user)

    for animal in animals:
        db.db.session.add(animal)

    for record_type in record_types:
        db.db.session.add(record_type)

    for i, record in enumerate(medical_records):
        record.animal = animals[i]
        record.user = vet_user
        record.record_type = record_types[i]
        db.db.session.add(record)

    for i, walk in enumerate(walks):
        walk.animal = animals[i]
        walk.user = volunteer_user
        db.db.session.add(walk)

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
