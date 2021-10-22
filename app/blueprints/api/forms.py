from flask import url_for
from flask_wtf import FlaskForm
from wtforms import ValidationError
from wtforms.fields import (
    BooleanField,
    PasswordField,
    StringField,
    SubmitField,
)
from wtforms.fields.html5 import EmailField
from wtforms.validators import Email, EqualTo, InputRequired, Length

from app.models import ApiKey


class AccessKeyForm(FlaskForm):
    user_input = StringField(
        'Access Token', validators=[InputRequired(),
                             Length(1, 64)])
    submit = SubmitField('Submit')
