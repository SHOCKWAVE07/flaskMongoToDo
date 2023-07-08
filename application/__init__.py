from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["SECRET_KEY"] = 'a8bbb89011cc826c2bccb6fc1f53d779c1e59814'
app.config["MONGO_URI"]='mongodb+srv://varunraskar22:Shockwave07@cluster0.4tcbg1f.mongodb.net/'

mongodb_client = PyMongo(app)
db = mongodb_client.db

from application import routes