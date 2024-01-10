from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField,BooleanField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from app.auth.models import User


def email_exists(form, field):
    email = User.query.filter_by(user_email=field.data).first()
    if email:
        raise ValidationError('Email already exists. !!!')




class ResgistrationForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), Length(4, 16, message="Between 4 to 16 characters")])
    email =StringField("E-mail", validators=[DataRequired(), Email(), email_exists])
    passwor = PasswordField("Password", validators=[DataRequired(), EqualTo("confirm", message="Password mus match!!!")])
    confirm =PasswordField("Confirm", validators=[DataRequired()])
    submit = SubmitField("Register")

class LoginForm(FlaskForm):
    email = StringField("E-mail", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    stay_loggedin = BooleanField("Remember me!")
    submit = SubmitField("Login")

class Scraping(FlaskForm):
    search_article = StringField("Article", validators=[DataRequired()])
    search = SubmitField("Search")
