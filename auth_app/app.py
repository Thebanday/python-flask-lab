from flask import Flask,jsonify,render_template,request,send_from_directory,session
import requests,os,json

app=Flask(__name__)
USER_FILE="users.json"
app.secret_key= "supersecretkey"  # needed


# utility

def load_users():
    if not os.path.exists(USER_FILE):
        with open(USER_FILE,"w") as f:
            json.dump([],f)
        return []
    try:
        with open(USER_FILE,"r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def save_users(username,email,password):
    users=load_users()
    users.append({"username":username,"email":email,"password":password})
    with open (USER_FILE,"w") as f:
        return json.dump(users,f)
    

def authentication(username,password):
    users=load_users()
    for u in users:
        if u["username"]==username and u["password"]==password:
            return True
    return False
@app.route("/")
def root():
    return send_from_directory("templates","signup.html")

@app.route("/login.html")
def login():
    return send_from_directory("templates","login.html")

@app.route("/dashboard.html")
def dashboard():
    if "username" in session:
        return send_from_directory("templates","dashboard.html")
    return jsonify({"error":"unauthorized"}),401


@app.route("/api/signup",methods=["POST"])
def signup():
    data=request.json
    username=data.get("username")
    email=data.get("email")
    password=data.get("password")
    cpassword=data.get("cpassword")
    if (password!=cpassword):
        return jsonify({"error":"Password and confirm password are not same"}),400
    if(len(password)< 8 or len(username)< 8):
        return jsonify({"error":"Username and password should be atleat 8 digits long"}),400
    if not username or not password:
        return jsonify({"error":"Missinng credentialas"}),400
    if user_exists(username):
        return jsonify({"error":"User Already Exist"}),400
    save_users(username,email,password)    
    return jsonify({"message":"Signup Successful!"}),200

@app.route("/api/login",methods=["POST"])
def login_api():
    data=request.json
    username=data.get("username")
    password=data.get("password")
    if authentication(username,password):
        session["username"]=username
        return jsonify({"message":"Login Succesfull"})
    return jsonify({"error":"Invalid credentials"})

@app.route("/api/logout",methods=["POST"])
def logout():
    session.pop("username",None)
    return jsonify({"message":"Logged out"})

@app.route("/api/user")
def getuser():
    if "username" in session:
        return jsonify({"username":session["username"]})
    return jsonify({"error":"Not logged in"})
    
def user_exists(username):
    users = load_users()
    for user in users:
        if user["username"] == username:
            return True
    return False
 
if __name__=="__main__":
    app.run(debug=True)