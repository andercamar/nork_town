from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token, jwt_required

auth_routes = Blueprint('auth', __name__)

@auth_routes.route('/login',methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    
    if username == 'test' and password == 'test':
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token),200
      
    return jsonify({"message": "Username or password wrong"}), 401

@auth_routes.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    return jsonify(msg="This is a protected route"), 200