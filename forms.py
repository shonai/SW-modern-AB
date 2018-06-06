from wtforms import Form, BooleanField, StringField, PasswordField, validators


class RegistrationForm(Form):
    login = StringField('UserName', [validators.DataRequired(), validators.Email()])
    password = PasswordField('New Password', [
        validators.DataRequired(), validators.equal_to('confirm', message='Passwords must match')])
    confirm = PasswordField('Repeat Password')
