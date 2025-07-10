from flask import jsonify,request,render_template

from config import app,db
from models import Contact

@app.route("/contacts",methods=["GET"])
def getcontacts():
    Contacts=Contact.query.all()
    json_contacts=list(map(lambda x:x.to_json(),Contacts))
    return jsonify({"Contacts":json_contacts})

@app.route("/addcontact",methods=["POST"])
def add_contact():
    data = request.json
    first_name = data.get("FirstName")
    last_name = data.get("LastName")
    email = data.get("Email")

    if not first_name or not last_name or not email:
        return jsonify({"error":"Please fill all Fields"}),400

    new_contact=Contact(first_name=first_name,last_name=last_name,email=email)
    try:
        db.session.add(new_contact)
        db.session.commit()
    except Exception as e:
        return jsonify({"error":str(e)}),400
    return jsonify({"message":"User added successfully"}),201

@app.route("/contacts/<int:user_id>",methods=["DELETE"])
def deleteContact(user_id):
    contact=Contact.query.get(user_id)
    if not contact:
        return jsonify({"error":"User not Found"}),404
    db.session.delete(contact)
    db.session.commit()

    return jsonify({"message":"user deleted succesfully"}),201

@app.route("/contacts/<int:user_id>",methods=["PUT"])
def updateContact(user_id):

    contact=Contact.query.get(user_id)
    if not contact:
        return jsonify({"error":"User not Found"}),404
    data=request.json
    contact.first_name=data.get("FirstName",contact.first_name)
    contact.last_name=data.get("LastName",contact.last_name)
    contact.email=data.get("Email",contact.email)

    db.session.commit()
    return jsonify({"message":"user updated succesfully"}),201

if __name__=="__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
