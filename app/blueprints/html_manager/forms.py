from flask import url_for
from flask_uploads import UploadSet, IMAGES
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import ValidationError, validators
from wtforms.fields import BooleanField, PasswordField, StringField, SubmitField, IntegerField, SelectField, \
    TextAreaField, EmailField, DateField
from wtforms.validators import (
    Email,
    EqualTo,
    InputRequired,
    Length,
    DataRequired
)
from wtforms_alchemy import model_form_factory, ModelForm
from flask_wtf.file import FileAllowed, FileRequired


images = UploadSet('images', IMAGES)
docs = UploadSet('docs', ('rtf', 'odf', 'ods', 'gnumeric', 'abw', 'doc', 'docx', 'xls', 'xlsx', 'pdf', 'css'))

BaseModelForm = model_form_factory(FlaskForm)




class CssForm(FlaskForm):
    css = FileField('dot css file', validators=[FileRequired(), FileAllowed(docs, '.css file only!')])
    submit = SubmitField('Submit')


class FooterHtmlForm(BaseModelForm):
    html = TextAreaField("Footer Html Code")
    submit = SubmitField('Submit')

class HeaderHtmlForm(BaseModelForm):
    html = TextAreaField("Header Html Code")
    submit = SubmitField('Submit')
    
class NavbarHtmlForm(BaseModelForm):
    html = TextAreaField("Navbar Html Code")
    submit = SubmitField('Submit')

class FooterScriptForm(BaseModelForm):
    js = TextAreaField("Footer JavaScript Code")
    submit = SubmitField('Submit')

class HeaderScriptForm(BaseModelForm):
    js = TextAreaField("Header JavaScript Code")
    submit = SubmitField('Submit')

class CarouselHtmlForm(BaseModelForm):
    html = TextAreaField("Carousel Html Code Only!")
    submit = SubmitField('Submit')

class AlbumHtmlForm(BaseModelForm):
    html = TextAreaField("Album Html Code Only!")
    submit = SubmitField('Submit')

class BlankHtmlForm(BaseModelForm):
    html = TextAreaField("Blank Html Code Only!")
    submit = SubmitField('Submit')

class JumbotronHtmlForm(BaseModelForm):
    html = TextAreaField("Jumbotron Html Code Only!")
    submit = SubmitField('Submit')

class FormHtmlForm(BaseModelForm):
    html = TextAreaField("Form Html Code")
    form_name = StringField("Name", validators=[DataRequired(), Length(min=2, max=80)])
    submit = SubmitField('Submit')

class FeaturesHtmlForm(BaseModelForm):
    html = TextAreaField("Features Html Code Only!")
    submit = SubmitField('Submit')

class PricingHtmlForm(BaseModelForm):
    html = TextAreaField("Pricing Html Code Only!")
    submit = SubmitField('Submit')

class ContactHtmlForm(BaseModelForm):
    html = TextAreaField("Contact Html Code Only!")
    submit = SubmitField('Submit')

class TestimonialsHtmlForm(BaseModelForm):
    html = TextAreaField("Testimonials Html Code Only!")
    submit = SubmitField('Submit')

class MetatagsHtmlForm(BaseModelForm):
    html = TextAreaField("Meta Tags Html Code Only!")
    submit = SubmitField('Submit')

class LinkHtmlForm(BaseModelForm):
    html = TextAreaField("Link Tags Html Code Only!")
    submit = SubmitField('Submit')

class TitleHtmlForm(BaseModelForm):
    html = TextAreaField("Title Tag Html Code Only!")
    submit = SubmitField('Submit')
