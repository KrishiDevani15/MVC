from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField

from wtforms.validators import DataRequired, Length

class RegisterForm(FlaskForm):
    username = StringField("Username",validators=[DataRequired(),Length(min=4, max=25)])
    email = StringField("Email",validators=[DataRequired()])
    password = PasswordField("Password",validators=[DataRequired(),Length(min=8)])
    submit = SubmitField("Register")

class LoginForm(FlaskForm):
    email = StringField("Email",validators=[DataRequired()])
    password = PasswordField("Password",validators=[DataRequired()])
    submit = SubmitField("Login")