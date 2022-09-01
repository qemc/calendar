
from pro import app
from flask import render_template, redirect, url_for, flash
from pro.models import User
from pro.forms import RegisterForm
from pro import db
from flask_login import login_user
import os

IMG_FOLDER = os.path.join('static','pics')
app.config['UPLOAD_FOLDER'] =  IMG_FOLDER


@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register_page():

    form = RegisterForm()
    logo = os.path.join(app.config['UPLOAD_FOLDER'],'planer.png')
    
    if form.validate_on_submit():
        new_user = User(user_name = form.user_name.data, 
                        email_address = form.email_address.data,
                        password_hash = form.password_1.data)
        db.session.add(new_user)
        db.session.commit()
        #loging new created user
        login_user(new_user)
        #flashing positive message to announce that creation was succesful
        flash(f'Account created, you are now logged in as: {new_user.user_name}', category='success')
        return redirect(url_for('home_page'))

    if form.errors != {}: #If there are not errors from the validations
        for err_msg in form.errors.values():
            #here will be flash instead of print
            flash(f'There was an error with creating a user: {err_msg}', category='danger')

    return render_template('register.html', form = form, logo = logo)



