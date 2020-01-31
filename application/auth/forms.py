from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators
  
class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")
  
    class Meta:
        csrf = False

class RegistrationForm(FlaskForm):
    username = StringField("Username", [validators.Length(min=6, message="Username must be at least 6 characters long.")])
    password = PasswordField('Password', [validators.equal_to('confirm', message="Passwordfields don't match")])
    confirm = PasswordField('Repeat Password', [validators.Length(min=8, message="Make sure your password is atleast 8 characters long.")])

    class Meta:
        csrf = False