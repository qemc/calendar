from pro import app
from flask import render_template, redirect, url_for, flash, request
from pro.models import User, Event
from pro.forms import RegisterForm, LoginForm, EventForm, DeleteEventForm, EditEventForm, EditForm
from pro import db
from flask_login import login_user, logout_user, current_user
import os



IMG_FOLDER = os.path.join('static', 'pics')
app.config['UPLOAD_FOLDER'] = IMG_FOLDER


@app.route('/', methods=['GET', 'POST'])
def home_page():

    form = EventForm()
    delete_item = DeleteEventForm()
    edit_event_form = EditEventForm()
    edit_form = EditForm()
        
    if form.validate_on_submit() and form.submit.data:
        new_event = Event(event_name=form.name.data,
                          event_date=form.date.data,
                          event_time=form.time.data,
                          event_creator_id=current_user._get_current_object().id)
        db.session.add(new_event)
        db.session.commit()
        flash(f'Event Added', category='success')
        return redirect(url_for('home_page'))
 
    if edit_event_form.validate_on_submit() and edit_event_form.edit.data:
        
        to_edit = request.form.get('to_edit')    
        
        flash(to_edit, category='success')
        
        update_event = Event.query.filter_by(event_id = to_edit).first()
        update_event.event_name = edit_event_form.name.data
        update_event.event_time = edit_event_form.time.data
        update_event.event_date = edit_event_form.date.data
        db.session.commit()
        
        return redirect(url_for('home_page'))
        
    if current_user.is_authenticated:
        
        events = Event.query.filter(Event.event_creator_id==current_user.id).order_by(Event.event_date.asc())
        events.order_by(Event.event_date.asc())
        
        if delete_item.validate_on_submit():
            to_delete = request.form.get('to_delete')
            Event.query.filter_by(event_id = to_delete).delete()
            db.session.commit()
            
        return render_template('home.html', form=form, events=events, delete_item = delete_item, edit_event_form = edit_event_form, edit_form = edit_form)
    else:
        return render_template('home.html', form=form,delete_item = delete_item, edit_event_form = edit_event_form, edit_form = edit_form)


    

@app.route('/register', methods=['GET', 'POST'])
def register_page():

    form = RegisterForm()
    logo = os.path.join(app.config['UPLOAD_FOLDER'], 'planer.png')

    if form.validate_on_submit():
        new_user = User(user_name=form.user_name.data,
                        email_address=form.email_address.data,
                        password=form.password_1.data)
        db.session.add(new_user)
        db.session.commit()
        # loging new created user
        login_user(new_user)
        # flashing positive message to announce that creation was succesful
        flash(
            f'Account created, you are now logged in as: {new_user.user_name}', category='success')
        return redirect(url_for('home_page'))

    if form.errors != {}:  # If there are not errors from the validations
        for err_msg in form.errors.values():
            # here will be flash instead of print
            flash(
                f'There was an error with creating a user: {err_msg}', category='danger')

    return render_template('register.html', form=form, logo=logo)


@app.route('/login', methods=['GET', 'POST'])
def login_page():

    form = LoginForm()
    logo = os.path.join(app.config['UPLOAD_FOLDER'], 'planer.png')

    if form.validate_on_submit():
        attempted_user = User.query.filter_by(
            user_name=form.user_name.data).first()

        if attempted_user and attempted_user.check_password_correction(atempted_password=form.password.data):
            login_user(attempted_user)
            flash(
                f'You are now logged in as {current_user.user_name}', category='success')
            return redirect(url_for('home_page'))

        else:
            flash(f'User Name or password are wrong, try again', category='danger')

    return render_template('login.html', form=form, logo=logo)


@app.route('/logout')
def logout_page():
    logout_user()
    flash(f'You have been logged out', category='info')
    return redirect(url_for('home_page'))

    

