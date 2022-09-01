
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
import os


app = Flask(__name__)
login_manager = LoginManager(app)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data_base.db'
app.config['SECRET_KEY'] = '6be575743c714c0250e548de'

login_manager.login_view = 'login_page'
login_manager.login_message_category = 'info'

from pro import routes 
