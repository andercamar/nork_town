from flask import Blueprint
from flask_jwt_extended import jwt_required
from controllers.personController import PersonController

person_routes = Blueprint('person', __name__)
    
@person_routes.route('/person',methods=['GET'])
@jwt_required()
def get_persons():
    return PersonController.index()
    
@person_routes.route('/person',methods=['POST'])
@jwt_required()
def create_person():
    return PersonController.store()
    
@person_routes.route('/person/<int:person_id>',methods=['GET'])
@jwt_required()
def get_person(person_id):
    return PersonController.show(person_id)
    
@person_routes.route('/person/<int:person_id>',methods=['PUT'])
@jwt_required()
def update_person(person_id):
    return PersonController.update(person_id)
    
@person_routes.route('/person/<int:person_id>',methods=['DELETE'])
@jwt_required()
def delete_person(person_id):
    return PersonController.destroy(person_id)
    