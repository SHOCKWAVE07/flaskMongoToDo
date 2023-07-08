from flask import Flask
from flask_pymongo import PyMongo

application = Flask(__name__)
application.config["SECRET_KEY"] = 'a8bbb89011cc826c2bccb6fc1f53d779c1e59814'
application.config["MONGO_URI"]='mongodb+srv://varunraskar22:Shockwave07@cluster0.4tcbg1f.mongodb.net/todo'

mongodb_client = PyMongo(application)
db = mongodb_client.db

from main import routes