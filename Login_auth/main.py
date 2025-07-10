# from flask import jsonify,request,render_template,redirect,session
# from werkzeug.security import generate_password_hash,check_password_hash
# from models import Users,Session
# from config import app,db
# import jwt,secrets
# from datetime import datetime,timezone,timedelta
# import random
# SECRET_KEY="This is secret key"



# @app.route("/")
# def dashboard():
#     return render_template("/index.html")

# @app.route("/signup")
# def signup_page():
#     return render_template("/signup.html")

# @app.route("/login")
# def signnup_page():
#     return render_template("/login.html")

# @app.route("/api/signup",methods=["POST"])
# def signup():
#     try:
#         data=request.get_json()
#         email=data.get("email")
#         username=data.get("username")
#         password=data.get("password")
        
    
#         if not all([username,password,email]):
#             return jsonify({"error":"All fields are mandatory"}),400
    
#         hashed_pass=generate_password_hash(password)

#         existing_user=Users.query.filter_by(email=email).first()
#         if existing_user:
#             return jsonify({"error":"User already exists,Please Login!"}),400
    
#         new_user=Users(email=email,username=username,password=hashed_pass)

#         db.session.add(new_user)
#         db.session.commit()

#         return jsonify({"message":"User successfully created"}),201
#     except Exception as e:
#         return jsonify({"error":str(e)}),400
        
# @app.route("/api/users",methods=["GET"])
# def fetch_users():
#     allowed=['106.215.196.32','192.168.1.25 ',"127.0.0.1"]
#     if request.remote_addr not in allowed:
#         return render_template("/badreq.html")
#     users=Users.query.all()
#     user=list(map(lambda x:x.to_json(),users))
#     return jsonify(user)

# @app.route("/api/login",methods=["POST"])
# def login():
#     data=request.get_json()
#     email=data.get("email")
#     password=data.get("password")

#     user=Users.query.filter_by(email=email).first()

#     if not user:
#         return jsonify({"error": "Invalid credentials"}), 401
    
#     check_pass_hash=check_password_hash(user.password,password)
#     if not check_pass_hash:
#         return jsonify({"error":"Invalid credentials"}),401
    
#     session_id=secrets.token_hex(64)

#     new_session=Session(session_id=session_id,user_id=user.Id)
#     db.session.add(new_session)
#     db.session.commit()
#     response=jsonify({"message":"Login successfull"})

#     response.set_cookie(
#     key="token",
#     value=str(session_id),
#     httponly=True,
#     secure=True,
#     samesite="Strict"
#     )

#     return response,200




# @app.route("/api/logout",methods=["POST"])
# def logout():
#     session_id=request.cookies.get("token")
#     response = jsonify({"message": "Logged out successfully"})
#     session=Session.query.filter_by(session_id=session_id).first()
#     if session:
#         db.session.delete(session)
#         db.session.commit()
    
#     response.set_cookie(
#         key="token",
#         value="",
#         httponly=True,
#         secure=False,   
#         samesite="Strict",
#         max_age=0
#     )
    
#     return response, 200

# @app.route("/api/user",methods=["GET"])
# def fetch_current_user():
#     session_id=request.cookies.get("token")
#     if not session_id:
#         return jsonify({"error": "Unauthorized"}), 401
    
#     session = Session.query.filter_by(session_id=session_id).first()
#     if not session:
#         return jsonify({"error": "Invalid session"}), 401

#     current_user=Users.query.get(session.user_id)
#     return jsonify({
#         "Id": current_user.Id,
#         "email": current_user.email,
#         "username": current_user.username
#     }), 200




# if __name__ == "__main__":
#     with app.app_context():
#         db.create_all()
#     app.run(host="0.0.0.0",port=5000,debug=True,ssl_context=("cert.pem","key.pem"))
