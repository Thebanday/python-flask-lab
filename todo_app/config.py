from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
app=Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///project.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
app.config["SECRET_KEY"]="this_is_local_app"
CORS(app)
db=SQLAlchemy(app)
