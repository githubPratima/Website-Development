from wtforms import Form, StringField, PasswordField, validators

class UpdateUserForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=25), validators.DataRequired() ])
    email = StringField('Email Address', [validators.Length(min=6, max=35), validators.Email(), validators.DataRequired() ])
    new_pwd = PasswordField('New Password')
    password = PasswordField('Confirm with existing Password', [validators.DataRequired()])

class UpdatePwdForm(Form):
    new_pwd = PasswordField('New Password', [validators.DataRequired()]) 
    password = PasswordField('Confirm with existing Password', [validators.DataRequired()])
