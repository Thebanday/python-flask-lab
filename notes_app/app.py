from flask import Flask,jsonify,render_template,request

app=Flask(__name__)

notes = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/notes",methods=["GET"])
def getnotes():
    return jsonify(notes)

@app.route("/api/notes",methods=["POST"])
def addnote():
    data=request.get_json()
    note={
        "id":len(notes)+1,
        "content":data.get("content","")

    }
    notes.append(note)
    return jsonify(note),201

@app.route("/api/notes/<int:note_id>",methods=["DELETE"])
def deletenotes(note_id):
    global notes
    notes=[n for n in notes if n["id"] != note_id]
    return jsonify({"Message":"Note Deleted"}),200
    

if __name__=="__main__":
    app.run(debug=True)
