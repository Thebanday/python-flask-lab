from flask import jsonify,request,render_template,redirect,session
from werkzeug.security import generate_password_hash,check_password_hash
from models import Users
from config import app,db
import jwt
from datetime import datetime,timezone,timedelta
from functools import wraps

def auth_req(f):
    @wraps(f)
    def decorated_func(*args,**kwargs):
        token=request.cookies.get("secret")
        if not token:
                return jsonify({"error":"NO token Found"})
        try:
            with open("signing.key.pub","r") as file:
                decode_key=file.read()
            payload=jwt.decode(token,decode_key,algorithms="RS256")
            current_user=payload.get("user_id")
        except jwt.ExpiredSignatureError:
            return jsonify({"error": "Token expired"}), 401

        except jwt.InvalidTokenError:
            return jsonify({"error": "Invalid token"}), 401
        except Exception as e:
            return jsonify({"error":str(e)})
        
        return f(current_user,*args,**kwargs)
    return decorated_func



@app.route("/")
def dashboard():
    return render_template("/index.html")

@app.route("/api/signup",methods=["POST"])
def signup():
    try:
        data=request.get_json()
        email=data.get("email")
        username=data.get("username")
        password=data.get("password")
        
    
        if not all([username,password,email]):
            return jsonify({"error":"All fields are mandatory"}),400
    
        hashed_pass=generate_password_hash(password)

        existing_user=Users.query.filter_by(email=email).first()
        if existing_user:
            return jsonify({"error":"User already exists,Please Login!"}),400
    
        new_user=Users(email=email,username=username,password=hashed_pass)

        db.session.add(new_user)
        db.session.commit()

        return jsonify({"message":"User successfully created"}),201
    except :
        return jsonify({"error":"Bad request"}),400
        
@app.route("/api/users",methods=["GET"])
def fetch_users():
    allowed=['106.215.196.32','192.168.1.25 ',"127.0.0.1"]
    if request.remote_addr not in allowed:
        return render_template("/badreq.html")
    users=Users.query.all()
    user=list(list(map(lambda x:x.to_json(),users)))
    return jsonify(user)

@app.route("/api/login",methods=["POST"])
def login():
    data=request.get_json()
    email=data.get("email")
    password=data.get("password")

    user=Users.query.filter_by(email=email).first()

    if not user:
        return jsonify({"message": "Invalid credentials"}), 401
    
    check_pass_hash=check_password_hash(user.password,password)
    if not check_pass_hash:
        return jsonify({"message":"Invalid credentials"}),401
    
    payload={
        "user_id":user.Id,
        "email":user.email,
        "exp":datetime.now(timezone.utc)+ timedelta(hours=1)
    }
    # Read private key for signing
    with open("signing.key", "r") as file:
        private_key = file.read()

    
    jwt_token = jwt.encode(payload, private_key, algorithm="RS256")

    response= jsonify({"message":"Login succesfull"})
    response.set_cookie(
        key="secret",
        value=jwt_token,
        httponly=True,
        secure=False,
        samesite="Strict"
    )
    return response,200


@app.route("/api/logout",methods=["POST"])
def logout():
    response = jsonify({"message": "Logged out successfully"})
    
    # Clear the cookie → set it to empty with -1 max_age
    response.set_cookie(
        key="secret",
        value="",
        httponly=True,
        secure=False,    # True in production
        samesite="Strict",
        max_age=-1
    )
    
    return response, 200


@app.route("/api/user",methods=["GET"])
@auth_req
def get_current_user(current_user):
    return jsonify({"Error":current_user})



if __name__=="__main__":
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0",port=5000,debug=True)

