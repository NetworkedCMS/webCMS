from flask import url_for
from flask_wtf import FlaskForm
from wtforms import ValidationError
from wtforms.fields import (
    StringField,
    SubmitField,
    FileField,
    TextAreaField, EmailField)
from wtforms.validators import Email, EqualTo, InputRequired, Length



class UploadForm(FlaskForm):
    image = FileField('image')
    submit = SubmitField('Save')



class ContactForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired()])
    email = EmailField('Email', validators=[InputRequired(), Length(1, 64), Email()])
    text = TextAreaField('Message', validators=[InputRequired()])
    submit = SubmitField('Send')