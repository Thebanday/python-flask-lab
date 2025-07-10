from config import db

class Tasks(db.Model):
   __tablename__ = 'tasks'
   id=db.Column(db.Integer,primary_key=True)
   title=db.Column(db.String(50),nullable=False)
   description=db.Column(db.String(200),nullable=False)
   status=db.Column(db.Boolean,default=False)
   user_id=db.Column(db.Integer,db.ForeignKey("users.id"),nullable=False)

   def to_json(self):
      return{
         "Id":self.id,
         "Title":self.title,
         "Description":self.description,
         "status":self.status,
         "user_id":self.user_id
      }


class Users(db.Model):
   __tablename__= 'users'
   id=db.Column(db.Integer,primary_key=True)
   username=db.Column(db.String(50),unique=True,nullable=False)
   password=db.Column(db.String(100),nullable=False)

   def to_jsonn(self):
      return{
         "Id":self.id,
         "Username":self.username,
         "Password":self.password
      }

