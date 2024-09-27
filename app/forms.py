from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError, Length
from app import db
import sqlalchemy as sa
from app.models import User

class LoginForm(FlaskForm):
    username    = StringField('Username', validators=[DataRequired()])
    password    = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit      = SubmitField('Sign In')

class RegisterForm(FlaskForm):
    username    = StringField('Username', validators=[DataRequired()])
    email       = StringField('Email', validators=[DataRequired(), Email()])
    password    = PasswordField('Password', validators=[DataRequired()])
    password2   = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')]) 
    submit      = SubmitField('Sign Up')

    def validate_username(self, username):
        statement = sa.select(User).where(User.username == username.data)
        if db.session.scalar(statement):
            raise ValidationError("username already exist!")

    def validate_email(self, email):
        statement = sa.select(User).where(User.email == email.data)
        if db.session.scalar(statement):
            raise ValidationError("email already exist!")

class EditForm(FlaskForm):
    username    = StringField('Username', validators=[DataRequired()])
    about_me    = TextAreaField('About me', validators=[Length(min=0, max=140)])
    submit      = SubmitField('Submit')

    def __init__(self, original_username, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.original_username = original_username
    
    def validate_username(self, username):
        if username.data != self.original_username:
            statement = sa.select(User).where(User.username == username.data) 
            user      = db.session.scalar(statement)
            if user is not None:
                raise ValidationError("Please use a different username.")