from flask_wtf import FlaskForm
from wtforms import StringField, validators, TextAreaField

class CommentForm(FlaskForm):
    comment = TextAreaField("Add comment", [validators.Length(min=1)])
  
    class Meta:
        csrf = False