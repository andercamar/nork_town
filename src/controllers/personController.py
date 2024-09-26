from flask import jsonify,request
from services.personService import PersonService

class PersonController:
    @classmethod
    def index(self):
        try:
            persons = PersonService.get_persons()
            return jsonify([person.serialize() for person in persons]), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 400
    @classmethod
    def store(self):
        try:
            data = request.get_json()
            person = PersonService.create(data)
            return jsonify(person.serialize()), 201
        except Exception as e:
            return jsonify({'error': str(e)}), 400
    
    @classmethod   
    def show(self,person_id):
        try:
            person = PersonService.show(person_id)
            return jsonify(person.serialize()), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 404

    @classmethod 
    def update(self,person_id):
        try:
            data = request.get_json()
            PersonService.update(data, person_id)
            return jsonify({"message" : 'Person updated successfully'}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 400
        
    @classmethod
    def destroy(self,person_id):
        try:
            PersonService.delete(person_id)
            return jsonify({'message': 'Person deleted successfully'}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 400