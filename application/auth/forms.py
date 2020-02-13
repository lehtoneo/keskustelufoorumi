from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators
  
class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")
  
    class Meta:
        csrf = False

class RegistrationForm(FlaskForm):
    username = StringField("Username", [validators.Length(min=6, max=25, message="Username length has to be between 6 and 25 characters.")])
    password = PasswordField('Password', [validators.equal_to('confirm', message="Passwordfields don't match")])
    confirm = PasswordField('Repeat Password', [validators.Length(min=8, max=30, message="Make sure your password length is between 8 and 30 characters")])

    class Meta:
        csrf = False