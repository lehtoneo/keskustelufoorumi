from flask_wtf import FlaskForm
from wtforms import StringField, validators
from wtforms.widgets import TextArea

class CommentForm(FlaskForm):
    comment = StringField("Add comment")
  
    class Meta:
        csrf = False