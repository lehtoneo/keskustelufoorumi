from flask_wtf import FlaskForm
from wtforms import StringField, validators, TextAreaField, SelectField
from application.categories.models import Category


class NewThreadForm(FlaskForm):
    title = StringField("Thread title", [validators.Length(min=5, max=60)])
    description = TextAreaField("Description", [validators.Length(max=200)])
    categories = SelectField(u'Select Category', choices=Category.findChoices())
    class Meta:
        csrf = False

    


class EditThreadTitleForm(FlaskForm):
    title = StringField("New title: ", [validators.Length(min=5)])
    class Meta:
        csrf = False
class EditThreadDescriptionForm(FlaskForm):
    description = TextAreaField("New description: ", [validators.Length(max=200)])
    class Meta:
        csrf = False

