from app import db

class Person(db.Model):
    __tablename__ = 'person'
    
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
       
    def serialize(self):
        return{
            'id': self.id,
            'name': self.name
        }