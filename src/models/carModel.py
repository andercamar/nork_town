from sqlalchemy.orm import validates
from app import db

class Car(db.Model):
    __tablename__ = 'car'
    
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    color = db.Column(db.String(10),primary_key=False)
    model = db.Column(db.String(15),primary_key=False)
    
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'),nullable=False)
    
    @validates('color')
    def validate_color(self,key,color):
        assert color in ['yellow','blue','gray'], "Invalid Color"
        return color
    
    @validates('model')
    def validate_model(self,key,model):
        assert model in ['hatch','sedan','convertible'], "Invalid Model"
        return model
    
    def serialize(self):
        return{
            'id': self.id,
            'color': self.color,
            'model': self.model,
            'person_id': self.person_id
        }