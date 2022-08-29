from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired



class RegisterForm(FlaskForm):

    user_name = StringField(label='User Name: ', validators=[Length(min=3, max=30), DataRequired()])
    email_address = StringField(label='Email Address: ', validators=[Email(), DataRequired()])
    password_1 = PasswordField(label='Password: ', validators=[Length(min=6), DataRequired()])
    password_1 = PasswordField(label='Confirm Password: ', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Create Account')

