# -*- coding: utf-8 -*-
"""Public forms."""

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, EmailField
from wtforms.validators import InputRequired, Length, Email


class PublicContactForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired()])
    email = EmailField('Email', validators=[InputRequired(), Length(1, 64), Email()])
    text = TextAreaField('Message', validators=[InputRequired()])
    submit = SubmitField('Send')



class ContactForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired()])
    email = EmailField('Email', validators=[InputRequired(), Length(1, 64), Email()])
    text = TextAreaField('Message', validators=[InputRequired()])
    submit = SubmitField('Send')
