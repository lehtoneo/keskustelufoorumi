from flask_wtf import FlaskForm
from wtforms import StringField, validators, TextAreaField, RadioField


class DateForm(FlaskForm):
    radios = RadioField('Label', choices=[('newest','Newest first'),('oldest','Oldest first')], default='oldest')
    
    
    
    class Meta:
        csrf = False

