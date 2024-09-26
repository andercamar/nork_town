import pytest
from app import create_app,db
from models.personModel import Person
from models.carModel import Car
from flask_jwt_extended import create_access_token

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@localhost/test_db'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.drop_all()

def test_create_car(client):
    with client.application.app_context():
        access_token = create_access_token(identity="testuser")
        
    headers = {"Authorization": f"Bearer {access_token}"}
    
    response = client.post('/person', json={"name": "Testador"}, headers=headers)
    assert response.status_code == 201
    person_data = response.get_json()
    person_id = person_data["id"]
    
    for color, model in [('yellow', 'hatch'), ('blue', 'sedan'), ('gray', 'convertible')]:
        response = client.post('/cars', json={"color": color, "model": model, "person_id": person_id}, headers=headers)
        assert response.status_code == 201
    
    response = client.post('/cars', json={"color": "yellow", "model": "hatch", "person_id": person_id}, headers=headers)
    assert response.status_code == 400
    assert response.json['error'] == "The person already owns the maximum of cars allowed"

def test_secure_route(client):
    response = client.get('/cars')
    assert response.status_code == 401
    assert response.json['msg'] == "Missing Authorization Header"