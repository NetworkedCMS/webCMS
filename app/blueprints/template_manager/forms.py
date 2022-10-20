from flask_wtf import FlaskForm
from flask_ckeditor import CKEditorField
from flask_wtf.file import FileAllowed, FileRequired
from wtforms import ValidationError
from wtforms_alchemy import QuerySelectField, QuerySelectMultipleField
from wtforms.fields import (
    PasswordField,
    StringField,
    SubmitField,
    FloatField,
    MultipleFileField,
    FileField,
    SelectField,
    DateField, 
    TextAreaField,
    IntegerField,
    BooleanField, EmailField)
from wtforms.validators import (
    Email,
    EqualTo,
    InputRequired,
    Length,
    DataRequired
)

from app.models import Role, User, TemplateSetting, TemplateChoice
from wtforms_alchemy import Unique, ModelForm, model_form_factory
from app.utils.flask_uploads import UploadSet, IMAGES

images = UploadSet('images', IMAGES)
docs = UploadSet('docs', ('rtf', 'odf', 'ods', 'gnumeric', 'abw', 'doc', 'docx', 'xls', 'xlsx', 'pdf', 'css'))

BaseModelForm = model_form_factory(FlaskForm)

class TemplateSettingForm(BaseModelForm):
    template_name = StringField("Name of template", validators=[DataRequired(), Length(min=2, max=80)])
    category = SelectField(u'Category', choices=[('business','business'),('event','event'),('restaurant','restaurant'),
                                                 ('real estate','real estate'), ('portfolio','portfolio'),
                                                 ('launching soon','launching soon'), ('bare template','bare template')] ,validators=[DataRequired()])
    choice = BooleanField("Is Default Template?")
    image = FileField('Image size (400 × 400 px)', validators=[FileRequired(), FileAllowed(images, 'Images only allowed!')])
    submit = SubmitField('Submit')

class TemplateChoiceForm(BaseModelForm):
    template_name = StringField("Name of template", validators=[DataRequired(), Length(min=2, max=80)])
    choice = BooleanField("Is Default Template?")
    submit = SubmitField('Submit')
