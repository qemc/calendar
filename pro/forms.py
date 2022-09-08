from tokenize import String
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField, TimeField, TextAreaField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from pro.models import User


class RegisterForm(FlaskForm):

    def validate_user_name(self, user_name_to_check):
        user_name = User.query.filter_by(
            user_name=user_name_to_check.data).first()
        if user_name:
            raise ValidationError('user_name already exists')

    def validate_email_address(self, email_address_to_check):
        email_address = User.query.filter_by(
            email_address=email_address_to_check.data).first()
        if email_address:
            raise ValidationError('Email_addres already exists')

    user_name = StringField(label='User Name: ', validators=[
                            Length(min=3, max=30), DataRequired()])
    email_address = StringField(label='Email Address: ', validators=[
                                Email(), DataRequired()])
    password_1 = PasswordField(label='Password: ', validators=[
                               Length(min=6), DataRequired()])
    password_2 = PasswordField(label='Confirm Password: ', validators=[
                               EqualTo('password_1'), DataRequired()])
    submit = SubmitField(label='Create Your Account')


class LoginForm(FlaskForm):

    user_name = StringField(label='User Name', validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    submit = SubmitField(label='Login')


class EventForm(FlaskForm):

    date = DateField(label='Date', validators=[DataRequired()])
    time = TimeField(label='Time', validators=[DataRequired()])
    name = TextAreaField(label='Description', validators=[
                         Length(min=2, max=300), DataRequired()])
    submit = SubmitField(label='Add')


class DeleteEventForm(FlaskForm):
    delete = SubmitField(label='Delete')
    
class EditEventForm(FlaskForm):

    date = DateField(label='Date', validators=[DataRequired()])
    time = TimeField(label='Time', validators=[DataRequired()])
    name = TextAreaField(label='Description', validators=[
                            Length(min=2, max=300), DataRequired()])
    edit = SubmitField(label='Save')
    
class EditForm(FlaskForm):
    submit = SubmitField(label='Edit')


    