from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    
    app.config.from_object('config.Config')

    db.init_app(app)
    jwt.init_app(app)
    
    from routes.authRoute import auth_routes
    from routes.personRoute import person_routes
    from routes.carRoute import car_routes
    
    app.register_blueprint(auth_routes)
    app.register_blueprint(person_routes)
    app.register_blueprint(car_routes)
    
    return app
