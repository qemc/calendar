from python import app
from flask import render_template
from python.models import User


@app.route('/')
def home_page():
    user = User()
    return render_template('home.html', user = user)