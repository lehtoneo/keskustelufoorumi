from flask_wtf import FlaskForm
from wtforms import StringField, validators

class NewThreadForm(FlaskForm):
    title = StringField("Thread title", [validators.Length(min=5)])
 
    class Meta:
        csrf = False

class EditThreadForm(FlaskForm):
    title = StringField("New title: ", [validators.Length(min=5)])
    
 
    class Meta:
        csrf = False