from flask_wtf import FlaskForm
from wtforms import StringField, validators, TextAreaField

class NewThreadForm(FlaskForm):
    title = StringField("Thread title", [validators.Length(min=5)])
    description = TextAreaField("Description")
 
    class Meta:
        csrf = False

class EditThreadForm(FlaskForm):
    title = StringField("New title: ", [validators.Length(min=5)])
    description = TextAreaField("Description")
    
 
    class Meta:
        csrf = False