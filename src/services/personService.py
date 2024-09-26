from models.personModel import Person,db
from sqlalchemy.exc import SQLAlchemyError
class PersonService:
    @classmethod
    def get_persons(self):
        return Person.query.all()

    @classmethod
    def create(self,data):
        try:
            if 'name' not in data:
                raise Exception("Name is required")
            person = Person(name=data.get('name'))
            db.session.add(person)
            db.session.commit()
            return person
        except SQLAlchemyError as e:
            db.session.rollback()
            raise Exception("Database error: %s" % (e))
        
    @classmethod
    def show(self,person_id):
        person = Person.query.get(person_id)
        if not person:
            raise Exception("Person not Found")
        return person

    @classmethod
    def update(self,data,person_id):
        person = Person.query.get(person_id)
        if not person:
            raise Exception("Person not Found")
        if 'name' in data:
            person.name = data['name']
        try:
            updatedPerson = db.session.commit()
            return updatedPerson
        except SQLAlchemyError as e:
            db.session.rollback()
            raise Exception("Update error: %s" % (e))
        
    @classmethod
    def delete(self,person_id):
        person = Person.query.get(person_id)
        if not person:
            raise Exception("Car not Found")
        try:
            db.session.delete(person)
            db.session.commit()
            return True
        except SQLAlchemyError as e:
            db.session.rollback()
            raise Exception("Delete error: %s" % (e))
