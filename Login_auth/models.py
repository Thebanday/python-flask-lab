from config import db
from datetime import datetime,timezone


class Users(db.Model):
    Id=db.Column(db.Integer,primary_key=True)
    email=db.Column(db.String(80),nullable=False,unique=True)
    username=db.Column(db.String(50),nullable=False)
    password=db.Column(db.String(80),nullable=True)
   

    def to_json(self):
        return {
            "Id":self.Id,
            "email":self.email,
            "username":self.username
            
        }
    
class Session(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.Integer, unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.Id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())



