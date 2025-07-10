# app.py
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/api/hello",methods=["GET"])
def home():
    return jsonify({"message": "Hello world!"})


@app.route("/api/user/<username>",methods=["GET"])
def second(username):
    return f"hello {username}"

@app.route("/api/add",methods=["POST"])
def third():
    data=request.get_json()
    a=data.get('a')
    b=data.get('b')
    result=a+b
    return jsonify({"sum":result})

contacts=[]
@app.route("/api/contacts",methods=["POST"])
def addcontact():
    data=request.get_json()
    name=data.get("name")
    phone=data.get("phone")
    new_contact={
        "name":name,
        "phone":phone
    }
    contacts.append(new_contact)
    return jsonify(new_contact),201

@app.route("/api/contacts",methods=["GET"])
def gettasks():
    return jsonify(contacts)


@app.route("/api/contacts/<name>",methods=["DELETE"])
def deltetask(name):
    global contacts
    
    contacts=[c for c in contacts if c["name"]!=name]
    



if __name__ == "__main__":
    app.run(debug=True)
