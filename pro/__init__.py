
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os




app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data_base.db'
app.config['SECRET_KEY'] = '6be575743c714c0250e548de'
from pro import routes 
