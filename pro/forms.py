from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from pro.models import User



class RegisterForm(FlaskForm):

    def validate_user_name(self, user_name_to_check):
        user_name = User.query.filter_by(user_name = user_name_to_check.data).first()
        if user_name:
            raise ValidationError('user_name already exists') 

    def validate_email_address(self, email_address_to_check):
        email_address = User.query.filter_by(email_address = email_address_to_check.data).first()
        if email_address:
            raise ValidationError('Email_addres already exists') 

    user_name = StringField(label='User Name: ', validators=[Length(min=3, max=30), DataRequired()])
    email_address = StringField(label='Email Address: ', validators=[Email(), DataRequired()])
    password_1 = PasswordField(label='Password: ', validators=[Length(min=6), DataRequired()])
    password_2 = PasswordField(label='Confirm Password: ', validators=[EqualTo('password_1'), DataRequired()])
    submit = SubmitField(label='Create Your Account')

