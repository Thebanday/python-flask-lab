# from flask import Flask, jsonify,request
# from markupsafe import escape
# from flask import render_template_string
# app=Flask(__name__)

# # @app.route("/")
# # def greet():
# #     return "<p><h1>Hello world</h1></p>"

# # #xss protecctionn using jinja
# # # @app.route("/<name>")
# # # def new(name):
# # #     return render_template_string("hello, {{name}}",name=name)

# # html escaping
# # @app.route("/vuln/<vuln>")
# # def new1(vuln):
# #     return f"Hello {escape(vuln)}"

# @app.route("/helllo")
# def hello():
#     return jsonify({"Message":"hello world"})






# tasks=[
#     {"id":1,"title":"Buy books"},
#     {"id":2,"title":"sleep"}

# ]

# @app.route("/tasks")
# def taks():
#     return jsonify(tasks)


# # tasks=[]

    
# # @app.route("/addtask",methods=["POST"])
# # def addd_tasks():
# #     data=request.get_json()
# #     if "title" not in data:
# #         return jsonify({"Error":"No title Found"})
    
# #     task={"id":len(tasks)+1,"title":data["title"]}
# #     tasks.append(task)
# #     return jsonify(task),201


# tasks = [
#     {"id": 1, "title": "Learn Flask"},
#     {"id": 2, "title": "Build API"},
# ]

# @app.route("/gettasks",methods=["GET"])
# def gettask():
#     return jsonify(tasks)

# @app.route("/tasks/<int:task_id>",methods=["DELETE"])
# def delete(task_id):
#     global tasks
    
    
    
    


# if __name__=="__main__":
#     app.run(debug=True)







































from flask import Flask,jsonify,request




app=Flask(__name__)


@app.route("/")
def greet():
    return "hello world"

@app.route("/api/info",methods=["POST"])
def return_json():
    return jsonify({"name":"majid","age":25})


tasks=[]

@app.route("/tasks",methods=["GET"])
def get_tasks():
    return jsonify(tasks)

@app.route("/tasks",methods=["POST"])
def add_task():
    data=request.get_json()
    tasks.append(data)
    return "Task is sucesfully added"

@app.route("/tasks/<int:index>",methods=["DELETE"])
def del_tasks(index):
    if 0 <= index < len(tasks):
        removed=tasks.pop(index)
        return jsonify({"removed":removed}),200
    return jsonify({"error": "no task found"}),404


if __name__=="__main__":
    app.run(debug=True)