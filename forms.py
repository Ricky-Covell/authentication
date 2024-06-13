from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField 
from wtforms.validators import InputRequired, Length, Email




# # # # # # # # # # # # # # # # FORMS # # # # # # # # # # # # # # # # # # # # # # # # 
class RegistrationForm(FlaskForm):
    '''Registration Form'''

    username = StringField(
        'Username',
        validators=[InputRequired(), Length(min=1, max=20)],
    )

    password = PasswordField(
        'Password',
        validators=[InputRequired(), Length(min=6, max=55)],
    )

    email = StringField(
        'Email',
        validators=[InputRequired(), Email(), Length(min=1, max=55)],
    )

    first_name = StringField(
        "First Name",
        validators=[InputRequired(), Length(max=30)],
    )
    last_name = StringField(
        "Last Name",
        validators=[InputRequired(), Length(max=30)],
    )



class LoginForm(FlaskForm):
    '''Login Form'''

    username = StringField(
        "Username",
        validators=[InputRequired(), Length(min=1, max=20)],
    )
    password = PasswordField(
        "Password",
        validators=[InputRequired(), Length(min=6, max=55)],
    )


class FeedbackForm(FlaskForm):
    title = StringField(
        "Title",
        validators=[InputRequired(), Length(max=100)],
    )

    content = StringField(
        "Content",
        validators=[InputRequired()],
    )

