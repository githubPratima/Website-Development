from wtforms import Form, BooleanField, StringField, PasswordField, validators, SelectField

from shop.admin.models import Roles

class RegistrationForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=25), validators.DataRequired()])
    email = StringField('Email Address', [validators.Length(min=6, max=35), validators.Email(),validators.DataRequired() ])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')

class LoginForm(Form):
    email = StringField('Email', [validators.Length(min=6, max=35), validators.Email()]) 
    password = PasswordField('Password', [validators.DataRequired()])

class AddUserForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=25), validators.DataRequired()])
    email = StringField('Email Address', [validators.Length(min=6, max=35), validators.Email(),validators.DataRequired() ])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    role = SelectField(u'Roles', choices=[(Roles.generic_user, Roles.generic_user.value),
    (Roles.retail_user, Roles.retail_user.value), 
    (Roles.site_manager, Roles.site_manager.value)])
