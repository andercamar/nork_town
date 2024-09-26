from flask.cli import FlaskGroup
from models.personModel import Person
from models.carModel import Car

from app import create_app,db

app = create_app()

cli = FlaskGroup(app)

@cli.command("init_db")
def init_db():
    db.drop_all()
    db.create_all()
    
    db.session.add(Person(name="Joaquim"))
    db.session.add(Person(name="Fernanda"))
    db.session.commit()
    
    
    db.session.add(Car(model="hatch",color="gray",person_id=1))
    db.session.add(Car(model="convertible",color="blue",person_id=2))
    db.session.commit()

    print("Database initialized")

   
if __name__ == '__main__':
    cli()