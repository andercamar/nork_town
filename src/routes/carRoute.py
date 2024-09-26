from flask import Blueprint
from flask_jwt_extended import jwt_required
from controllers.carController import CarController


car_routes = Blueprint('car', __name__)
  
@car_routes.route('/cars',methods=['GET'])
@jwt_required()
def get_cars():
    return CarController.index()
    
@car_routes.route('/cars',methods=['POST'])
@jwt_required()
def create_car():
    return CarController.store()
    
@car_routes.route('/cars/<int:car_id>',methods=['GET'])
@jwt_required()
def get_car(car_id):
    return CarController.show(car_id)
    
@car_routes.route('/cars/<int:car_id>',methods=['PUT'])
@jwt_required()
def update_car(car_id):
    return CarController.update(car_id)
    
@car_routes.route('/cars/<int:car_id>',methods=['DELETE'])
@jwt_required()
def delete_car(car_id):
    return CarController.destroy(car_id)
    