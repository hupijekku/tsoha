from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators


class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")

    class Meta:
        csrf = False

class RegisterForm(FlaskForm):
    full_name = StringField("Full name", [validators.Length(min=5, max=144)])
    username = StringField("Username", [validators.Length(min=3, max=144)])
    password = PasswordField("Password", [validators.Length(min=6, max=144)])

    class Meta:
        csrf = False

class UpdateForm(FlaskForm):
    full_name = StringField("Full name", [validators.Length(min=5, max=144)])
    username = StringField("Username", [validators.Length(min=3, max=144)])
    password = PasswordField("New password", [validators.Length(min=6, max=144)])
    current_password = PasswordField("Current password", [validators.Length(min=6, max=144)])

    class Meta:
        csrf = False

class UpdateForm(FlaskForm):
    full_name = StringField("Full name", [validators.Length(min=5, max=144)])
    username = StringField("Username", [validators.Length(min=3, max=144)])
    password = PasswordField("New password", [validators.Length(min=6, max=144)])
    current_password = PasswordField("Current password", [validators.Length(min=6, max=144)])

    class Meta:
        csrf = False
