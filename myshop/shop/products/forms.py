
from flask_wtf.file import FileAllowed, FileField, FileRequired

from wtforms import Form, IntegerField, StringField, BooleanField, TextAreaField, validators


class AddProductsForm(Form):
    name = StringField('Name', [validators.DataRequired()])
    price = IntegerField('Price', [validators.DataRequired()])
    category = StringField('Category', [validators.DataRequired()])
    stock = IntegerField('stock', [validators.DataRequired()])
    visibility = BooleanField('Visibility')
    description = TextAreaField("Description", [validators.DataRequired()])
    image_1 = FileField('Image 1', validators=[  FileAllowed(['jpg', 'png', 'jpeg'])] )
    image_2 = FileField('Image 2', validators=[  FileAllowed(['jpg', 'png', 'jpeg'])] )
    image_3 = FileField('Image 3', validators=[  FileAllowed(['jpg', 'png', 'jpeg'])] )
