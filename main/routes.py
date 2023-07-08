

from main import application,db
from flask import render_template,flash,request,redirect,url_for
from .forms import TodoForm
from datetime import datetime
from bson import ObjectId

@application.route("/")
def get_todos():
    todos = []
    for todo in db.todos_flask.find().sort("date_created",-1):
        todo["_id"] = str(todo["_id"])
        todo["data_created"] = todo["date_created"].strftime("%b %d %Y %H:%M:%S")
        todos.append(todo)
    return render_template("views_todo.html",title="Layout page", todos=todos)

@application.route("/add_todo", methods = ['POST', 'GET'])
def add_todo():
    if request.method == "POST":
        form = TodoForm(request.form)
        todo_name = form.name.data
        todo_description = form.description.data
        completed = form.completed.data

        db.todos_flask.insert_one({
            "name": todo_name,
            "description": todo_description,
            "completed": completed,
            "date_created": datetime.utcnow()
        })
        flash("Todo successfully added", "success")
        return redirect("/")
    else:
        form = TodoForm()
    return render_template("add_todo.html", form = form)

@application.route("/update_todo/<id>", methods=["POST","GET"])
def update_todo(id):
    if request.method== "POST":
        form = TodoForm(request.form)
        todo_name = form.name.data
        todo_description = form.description.data
        completed = form.completed.data

        db.todos_flask.find_one_and_update({"_id":ObjectId(id)}, 
                                           {"$set":{"name":todo_name,
                                                    "description": todo_description,
                                                    "completed": completed,
                                                    "date_created": datetime.utcnow()
                                            }})
        flash("Todo successfully updated", "success")
        return redirect("/")
    
    else:
        form = TodoForm()
        todo = db.todos_flask.find_one_or_404({"_id":ObjectId(id)})
        form.name.data = todo.get("name",None)
        form.description.data = todo.get("description", None)
        form.completed.data = todo.get("completed",None)

    return render_template("add_todo.html",form=form)

@application.route("/delete_todo/<id>")
def delete_todo(id):
    db.todos_flask.find_one_and_delete({"_id":ObjectId(id)})
    flash("Todo deleted successfully" , "success")
    return redirect("/")

# @application.route("/")
# def home():
#     return render_template("u.html")