
from pro import app
from flask import render_template
from pro.models import User
from pro.forms import RegisterForm
import os

IMG_FOLDER = os.path.join('static','pics')
app.config['UPLOAD_FOLDER'] =  IMG_FOLDER

@app.route('/')
def home_page():
    user = User()
    return render_template('home.html', user = user)

@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    logo = os.path.join(app.config['UPLOAD_FOLDER'],'planer.png')
    # here will be some sqlalchemy queries
    return render_template('register.html', form = form, logo = logo)



