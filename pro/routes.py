from pro import app
from flask import render_template
from pro.models import User


@app.route('/')
def home_page():
    user = User()
    return render_template('home.html', user = user)


