from application import app
from flask import render_template
from .forms import TodoForm

@app.route("/")
def index():
    return render_template("index.html",title="Layout page") 

@app.route("/todo")
def todo():
    return render_template("views_todo.html")

@app.route("/add_todo")
def add_doto():
    form = TodoForm()
    return render_template("add_todo.html",form=form)