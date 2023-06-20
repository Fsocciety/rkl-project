from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import InputRequired, Length, Email, EqualTo

class LoginForm(FlaskForm):
    username = StringField('Username', 
                            validators=[InputRequired(), Length(min=2, max=20)])
    password = PasswordField('Password',
                            validators=[InputRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')