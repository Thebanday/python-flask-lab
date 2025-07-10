from flask import Flask,jsonify,request,render_template

app=Flask(__name__)


tasks=[]
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/tasks",methods=["GET"])
def getTasks():
    return jsonify(tasks)

@app.route("/api/tasks",methods=["POST"])
def addTask():
    data=request.get_json()
    task={
        "id":len(tasks)+1,
        "text":data.get("text",""),
        "done":False

    }
    tasks.append(task)
    return jsonify(task),201


@app.route("/api/tasks/<int:task_id>",methods=["DELETE"])
def deleteTask(task_id):
    global tasks
    tasks=[t for t in tasks if t["id"]!=task_id]
    return jsonify({"Message":"Task Deleted"})


@app.route("/api/tasks/<int:task_id>/toggle",methods=["PUT"])
def toggleTask(task_id):
    for task in tasks:
        if task["id"]==task_id:
            task["done"]=not task["done"]
            return jsonify(tasks)
    return jsonify({"Error":"No Task Found"})

if __name__=="__main__":
    app.run(debug=True)