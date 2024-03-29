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
    BooleanField,EmailField)
from wtforms.validators import (
    Email,
    EqualTo,
    InputRequired,
    Length,
    DataRequired
)


from app.models import *
from wtforms_alchemy import Unique, ModelForm, model_form_factory
from app.utils.flask_uploads import UploadSet, IMAGES

images = UploadSet('images', IMAGES)
docs = UploadSet('docs', ('rtf', 'odf', 'ods', 'gnumeric', 'abw', 'doc', 'docx', 'xls', 'xlsx', 'pdf', 'css'))

BaseModelForm = model_form_factory(FlaskForm)


class PricingForm(FlaskForm):
    title = StringField(" Title e.g 'Free' or 'Premium'")
    description = StringField(" Description (Max 250 characters) ")
    submit = SubmitField('Submit')

class PricingAttributeForm(FlaskForm):
    description = StringField(" Description (Max 120 characters) ")
    submit = SubmitField('Submit')

class CostForm(FlaskForm):
    figure = FloatField(" 99.9 ")
    currency = StringField(" GBP or USD etc (Max 120 characters) ")
    currency_icon = StringField(" Currency Icons e.g '£' or '$' or '元' ")
    submit = SubmitField('Submit')


class SlideShowCrudForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired(), Length(min=2, max=80)])
    image = FileField('SlideShow Image (928x413)', validators=[FileRequired(), FileAllowed(images, 'Images only allowed!')])
    submit = SubmitField('Submit')

class SeoForm(FlaskForm):
    #meta_tag = SelectField(u'Meta Tag',choices=[('name','name'),('property','property')] ,validators=[DataRequired()])
    title = StringField("Title", validators=[DataRequired(), Length(min=5, max=80)])
    content = StringField("Meta Description, 180 words maximum", validators=[DataRequired(), Length(min=5, max=181)])
    submit = SubmitField('Submit')

#############################################################
class HomeTextForm(BaseModelForm):
    firstext = StringField("First Title", validators=[DataRequired(), Length(min=5, max=80)])
    secondtext = TextAreaField("Second Title")
    submit = SubmitField('Submit')

class AboutForm(BaseModelForm):
    title = StringField("First Title", validators=[DataRequired(), Length(min=5, max=180)])
    description = CKEditorField("Description")
    submit = SubmitField('Submit')

class CounterForm(BaseModelForm):
    title = StringField("Count Title e.g Projects", validators=[DataRequired(), Length(min=2, max=80)])
    count = StringField("Integers only e.g 1000", validators=[DataRequired(), Length(min=1, max=25)])
    submit = SubmitField('Submit')

class TeamForm(BaseModelForm):
    full_name = StringField("Full Name", validators=[DataRequired(), Length(min=2, max=80)])
    job_title = StringField("Job Title", validators=[DataRequired(), Length(min=2, max=80)])
    image = FileField('Team Member Portrait (255x255)', validators=[FileRequired(), FileAllowed(images, 'Images only allowed!')])
    submit = SubmitField('Submit')

class VideoForm(BaseModelForm):
    title = StringField("Video Title", validators=[DataRequired(), Length(min=2, max=80)])
    url = StringField("url e.g https://www.youtube.com/watch?v=jDDaplaOz7Q", validators=[DataRequired(), Length(min=2, max=80)])
    image = FileField('Video background image (1024 × 760 px)', validators=[FileRequired(), FileAllowed(images, 'Images only allowed!')])
    description = TextAreaField("Description")
    submit = SubmitField('Submit')

class PortfolioForm(BaseModelForm):
    title = StringField("Image Title", validators=[DataRequired(), Length(min=2, max=80)])
    image = FileField('Image size (873 × 885 px)', validators=[FileRequired(), FileAllowed(images, 'Images only allowed!')])
    description = StringField("Description")
    submit = SubmitField('Submit')

class TestimonialForm(BaseModelForm):
    full_name = StringField("Full Name", validators=[DataRequired(), Length(min=2, max=80)])
    job_title = StringField("Job Title ", validators=[DataRequired(), Length(min=2, max=80)])
    comment = StringField("Comment. 140 words max", validators=[DataRequired(), Length(min=2, max=180)])
    image = FileField('Image size (400 × 400 px)', validators=[FileRequired(), FileAllowed(images, 'Images only allowed!')])
    submit = SubmitField('Submit')

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
    
class NavMenuForm(FlaskForm):
    text = StringField("Text etc Contact", validators=[DataRequired(), Length(min=1, max=80)])
    url = StringField("Url e.g /account/login ", validators=[DataRequired(), Length(min=1, max=80)])
    submit = SubmitField('Submit')
    
class CallToActionForm(FlaskForm):
    text = StringField("Call to action text")
    url = StringField("Call to action url e.g /account/login ")
    submit = SubmitField('Submit')

class TechnologiesForm(FlaskForm):
    firstext = StringField("First Title", validators=[DataRequired(), Length(min=5, max=80)])
    secondtext = StringField("Second Title", validators=[DataRequired(), Length(min=10, max=80)])
    submit = SubmitField('Submit')

class ServiceForm(FlaskForm):
    title = StringField("Service Name", validators=[DataRequired(), Length(min=5, max=80)])
    description = StringField("Service Description", validators=[DataRequired(), Length(min=10, max=180)])
    submit = SubmitField('Submit')

class TrackingScriptForm(FlaskForm):
    name = StringField("Script Name e.g Hotjar or Google Analytics", validators=[DataRequired(), Length(min=2, max=25)])
    script = TextAreaField("Paste the raw script")
    submit = SubmitField('Submit')
    
class ImageTechnologyForm(FlaskForm):
    image = FileField('Technology Image (128x128)', validators=[FileRequired(), FileAllowed(images, 'Images only allowed!')])
    submit = SubmitField('Submit')

class ClientForm(FlaskForm):
    image = FileField('Client Image Max. (400x219)', validators=[FileRequired(), FileAllowed(images, 'Images only allowed!')])
    submit = SubmitField('Submit')
    
class WebsiteLogoForm(BaseModelForm):
    logo_image = FileField('Logo Image (182x33). A transparent logo is better', validators=[FileRequired(), FileAllowed(images, 'Logo Only allowed!')])
    submit = SubmitField('Submit')
    
class BackgroundImageForm(FlaskForm):
    background_image = FileField('Background (1920x1081)', validators=[FileRequired(), FileAllowed(images, 'Images Only allowed!')])
    submit = SubmitField('Submit')

class FaviconImageForm(FlaskForm):
    image = FileField('Favicon (32x32)', validators=[FileRequired(), FileAllowed(images, 'Images Only allowed!')])
    submit = SubmitField('Submit')

class AppleTouchIconForm(FlaskForm):
    favicon_image = FileField('Apple Touch Icon (180x180)', validators=[FileRequired(), FileAllowed(images, 'Images Only allowed!')])
    submit = SubmitField('Submit')
    
# Footer Text Form
class FooterTextForm(BaseModelForm):
    title = TextAreaField("Long Description", validators=[DataRequired(), Length(min=5)])
    submit = SubmitField('Submit')

# Footer Text Form
class FaqForm(BaseModelForm):
    question = StringField("Question Title", validators=[DataRequired(), Length(min=5)])
    answer = CKEditorField("Answer", validators=[DataRequired(), Length(min=5)])
    submit = SubmitField('Submit')

# Social Media Form 
class SocialMediaIconForm(FlaskForm):
    # image = FileField('Logo Image (128x128)', validators=[FileRequired(), FileAllowed(images, 'Social Iocn Image Only!')])
    icon = StringField("Icon Html Code(fab fa-facebook-f)", validators=[DataRequired()])
    url_link = StringField("Icon Link, e.g https://www.facebook.com/PastorChrisLive ", validators=[DataRequired()])
    submit = SubmitField('Submit')
    
# Brand Name Form Model
class BrandNameForm(FlaskForm):
    text = StringField("Brand Name E.g Nokia ", validators=[DataRequired(), Length(min=2, max=15)])
    submit = SubmitField('Submit')

# Copyright Form Model
class CopyRightForm(FlaskForm):
    text = StringField("Copyright Footer Text", validators=[DataRequired(), Length(min=6, max=60)])
    submit = SubmitField('Submit')

# Footer Image Model Form
class FooterImageForm(BaseModelForm):
    image = FileField('Footer Image', validators=[FileRequired(), FileAllowed(images, "Image Allowed Only !")])


# Resource Title Role Model Form
class ResourcesForm(BaseModelForm):
    role_title = StringField("Role Add ...", validators=[DataRequired(), Length(min=3, max=20)])




