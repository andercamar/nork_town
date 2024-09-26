from flask import jsonify,request
from services.carService import CarService

class CarController:
    @classmethod
    def index(self):
        try:
            cars = CarService.get()
            return jsonify([car.serialize() for car in cars]), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 400

    @classmethod
    def store(self):
        try:
            data = request.get_json()
            qtdCar = CarService.qtd_person_car(data['person_id'])
            if qtdCar >=3:
                return jsonify({'error': 'The person already owns the maximum of cars allowed'}), 400
            car = CarService.create(data)
            return jsonify(car.serialize()), 201
        except Exception as e:
            return jsonify({'error': str(e)}), 400
        
    @classmethod
    def show(self,car_id):
        try:
            car = CarService.show(car_id)
            return jsonify(car.serialize()), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 404
        
    @classmethod
    def update(self,car_id):
        try:
            data = request.get_json()
            CarService.update(data, car_id)
            return jsonify({"message" : 'Car updated successfully'}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 400
        
    @classmethod
    def destroy(self,car_id):
        try:
            CarService.delete(car_id)
            return jsonify({'message': 'Car deleted successfully'}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 400