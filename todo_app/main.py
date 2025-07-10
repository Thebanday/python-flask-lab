from flask import jsonify,request,render_template,send_from_directory
from config import db,app
from models import Tasks,Users
from datetime import datetime,timedelta,timezone
import jwt
from functools import wraps
from werkzeug.security import generate_password_hash,check_password_hash
#main routes
@app.route("/")
def home():
    return send_from_directory("templates", "index.html")

@app.route("/signup.html")
def signup_page():
    return send_from_directory("templates", "signup.html")

@app.route("/login.html")
def login_page():
    return send_from_directory("templates", "login.html")

@app.route("/index.html")
def dashboard_page():
    return send_from_directory("templates", "index.html")


def token_required(f):
    @wraps(f)
    def decorated(*args,**kwargs):
        token=request.cookies.get('jwt_token')
        if not token:
            return jsonify({"error":"Token is misssing"})
        try:
            data=jwt.decode(token,app.config["SECRET_KEY"],algorithms="H6256")
            current_user=Users.query.filter_by(user_id=data['Id']).first()
        except:
            return jsonify({"error":"Token is not valid"})
        return f(*args,**kwargs)
    return decorated

@app.route("/api/signup",methods=["POST"])
def signup():
    data=request.get_json()
    username=data.get("username")
    password=data.get("password")

    hashed_pasword=generate_password_hash(password,method="pbkdf2:sha512")

    if not username or not password:
        return jsonify({"error":"Username and Password are required"})
    
    existing_user=Users.query.filter_by(username=username).first()
    if existing_user:
        return jsonify({"error":"Username already exists"})
    
    new_user=Users(username=username,password=hashed_pasword)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message":"user succesfully added"})


@app.route("/api/login",methods=["POST"])
def login():
    data=request.get_json()
    username=data.get("username")
    password=data.get("password")

    user=Users.query.filter_by(username=username).first()
    decode_pass=check_password_hash(user.password,password)
    if not user or not decode_pass:
        return jsonify({"error":"Invalid Credentials"}),401
    
    
    token=jwt.encode(
        {'user_id':user.id,
        'exp':datetime.now(timezone.utc)+timedelta(hours=1)
        },
        app.config["SECRET_KEY"],
        algorithm="HS256"
    )
    
    resp = jsonify({"message": "Login successful"})
    resp.set_cookie('jwt_token', token, httponly=True)
    return resp

@app.route("/api/users",methods=["GET"])
def get_users():
    users = Users.query.all()
    users_json = [user.to_jsonn() for user in users]
    return jsonify(users_json), 200

@app.route("/api/user",methods=["GET"])
@token_required
def get_current_user(current_user):
    return jsonify(current_user.to_json()), 200

@app.route("/api/tasks",methods=["POST"])
def add_task():
    data=request.get_json()
    title=data.get("title")
    description=data.get("description")
    user_id=data.get("user_id")

    if not all([title,description,user_id]):
        return jsonify({"error":"All fiels required"}),401
    
    new_task=Tasks(title=title,description=description,user_id=user_id)
    db.session.add(new_task)
    db.session.commit()
    return jsonify({"message":"Task succesfully added"})

@app.route("/api/tasks/<int:user_id>",methods=["GET"])
def get_task(user_id):
    tasks=Tasks.query.filter_by(user_id=user_id).all()
    return jsonify([task.to_json() for task in tasks])


@app.route("/api/tasks/<int:task_id>",methods=["PUT"])
def updatetasks(task_id):
    task=Tasks.query.get(task_id)
    if not task:
        return jsonify({"error":"No such task found"})
    data=request.get_json()
    data = request.get_json()
    task.title = data.get("title", task.title)
    task.description = data.get("description", task.description)
    task.status = data.get("status",task.status)
    
    db.session.commit()
    return jsonify({"message":"Task updated","task":task.to_json()})


@app.route("/api/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    task = Tasks.query.get(task_id)
    if not task:
        return jsonify({"error": "Task not found"}), 404

    db.session.delete(task)
    db.session.commit()
    return jsonify({"message": "Task deleted"})




def token_required(f):
    @wraps(f)
    def decorated(*args,**kwargs):
        token=request.get('jwt_token')
        if not token:
            return jsonify({"error":"Token is misssing"})
        try:
            data=jwt.decode(token,app.config["SECRET_KEY"],algorithms="H6256")
            current_user=Users.query.filter_by(user_id=data['user_id']).first()
        except:
            return jsonify({"error":"Token is not valid"})
        return f(*args,**kwargs)
    return decorated


























































if __name__=="__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)

