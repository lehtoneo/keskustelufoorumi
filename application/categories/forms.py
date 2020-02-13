from flask_wtf import FlaskForm
from wtforms import StringField, validators, SelectField
from application.categories.models import Category

class CategoryForm(FlaskForm):
    
    categories = SelectField(u'Select Category', choices=Category.findChoices())
    othercategory = StringField("If you selected 'other' from the preceding list, type new category here. Otherwise, leave this empty", [validators.Length(min=5, max=30)])
    

    

    
    class Meta:
        csrf = False