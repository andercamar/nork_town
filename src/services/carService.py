from models.carModel import Car,db
from sqlalchemy.exc import SQLAlchemyError

class CarService:
    
    @classmethod
    def get(self):
        return Car.query.all()
    
    @classmethod
    def create(self,data):
        try:
            if 'color' not in data or 'model' not in data or 'person_id' not in data:
                raise Exception("Please fill in all fields")
            car = Car(color=data['color'],model=data['model'],person_id=data['person_id'])
            db.session.add(car)
            db.session.commit()
            return car
        except SQLAlchemyError as e:
            db.session.rollback()
            raise Exception("Database error: %s" % (e))
    
    @classmethod    
    def show(self,car_id):
        car = Car.query.get(car_id)
        if not car:
            raise Exception("Car not Found")
        return car

    @classmethod
    def update(self,data,car_id):
        car = Car.query.get(car_id)
        if not car:
            raise Exception("Car not Found")
        if 'color' in data:
            car.color = data['color']
        if 'model' in data:
            car.model = data['model']
        try:
            updatedCar = db.session.commit()
            return updatedCar
        except SQLAlchemyError as e:
            db.session.rollback()
            raise Exception("Update error: %s" % (e))
        
    @classmethod
    def delete(self,car_id):
        car = Car.query.get(car_id)
        if not car:
            raise Exception("Car not Found")
        try:
            db.session.delete(car)
            db.session.commit()
            return True
        except SQLAlchemyError as e:
            db.session.rollback()
            raise Exception("Delete error: %s" % (e))
        
    @classmethod
    def qtd_person_car(self,person_id):
        qtd = Car.query.filter_by(person_id=person_id).count()
        return qtd