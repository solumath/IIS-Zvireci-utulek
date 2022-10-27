import db
import main

roles = [
    db.user_role(id=0,name="admimnistrator", description="""
            - has highest permissions"""),

    db.user_role(id=1,name="caretaker", description="""
            - manages animals
            - creates walking timetables
            - verifies volunteers
            - approves animal bookings
            - creates veterinarian requests"""),

    db.user_role(id=2,name="veterinarian", description="""
            - has access to medical records, 
            - performs medical procedures"""),

    db.user_role(id=3,name="volunteer", description="""
            - can book animal for a walk 
            - can see his history"""),
]


def add_data():
    for role in roles:
        main.db.session.add(role)

    main.db.session.commit()


if __name__ == "__main__":
    with main.app.app_context():
        main.db.drop_all()
        main.db.create_all()
        
        add_data()
