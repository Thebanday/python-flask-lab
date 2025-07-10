from config import db


class Contact(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    first_name=db.Column(db.String(80),unique=False,nullable=False)
    last_name=db.Column(db.String(80),unique=False,nullable=False)
    email=db.Column(db.String(100),unique=True,nullable=False)

    def to_json(self):
        return{
            "user_id":self.id,
            "First_name":self.first_name,
            "Last_name":self.last_name,
            "Email":self.email

        }
