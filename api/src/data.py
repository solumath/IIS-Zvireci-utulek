from datetime import date
import db
from db.user_role import role_admin, role_volunteer, role_caretaker, role_unverified, role_vet


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
]

admin_users = [
    db.User("admin", "tryhards", "martin", "kneslik", "Berkova 54",
            "m.kneslik@utulek.cz", "+420603334197", 10, True),
]


def add_data():
    for role in user_roles:
        db.db.session.add(role)

    for admin in admin_users:
        admin.user_role = role_admin
        db.db.session.add(admin)

    # must be last, commits all changes to database
    db.db.session.commit()


if __name__ == "__main__":
    import app
    with app.app.app_context():
        db.db.drop_all()
        db.db.create_all()

        add_data()
