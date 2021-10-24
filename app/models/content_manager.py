import os

from flask import url_for
from .. import db


class SlideShowImage(db.Model):
    __tablename__ = "slide_show_images"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=True)
    image_filename = db.Column(db.String(256), nullable=True)

    @property
    def image_url(self):
        return url_for('_uploads.uploaded_file', setname='images',filename=self.image_filename, external=True)


    @property
    def image_path(self):
        from flask import current_app
        return os.path.join(current_app.config['UPLOADED_IMAGES_DEST'], self.image_filename)

def slide_show_images_serializer(slide_show_images):
    return {
        'id':slide_show_images.id,
        'title': slide_show_images.title ,
        'image_filename': slide_show_images.image_filename,
        }

class Seo(db.Model):
    __tablename__ = "seo"
    id = db.Column(db.Integer, primary_key=True)
    meta_tag = db.Column(db.String(80), nullable=True)
    title = db.Column(db.String(80), nullable=True)
    content = db.Column(db.String(256), nullable=True)

def seo_serializer(seo):
    return {
        'id':seo.id,
        'meta_tag': seo.meta_tag ,
        'title': seo.content,
        }


class Setting(db.Model):
    __tablename__ = "settings"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=True)
    display_name = db.Column(db.String(80), nullable=True)
    value = db.Column(db.String(512), nullable=True)


def settings_serializer(settings):
    return {
        'id':settings.id,
        'name': settings.name ,
        'display_name': settings.display_name,
        'value': settings.value,
        }

#####################################################

class Counter(db.Model):
    __tablename__ = "counter"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=True)
    count = db.Column(db.String(25), nullable=True)

def counter_serializer(counter):
    return {
        'id':counter.id,
        'title': counter.title ,
        }


class HomeText(db.Model):
    __tablename__ = "hometext"
    id = db.Column(db.Integer, primary_key=True)
    firstext = db.Column(db.String(80), nullable=True)
    secondtext = db.Column(db.Text)

def hometext_serializer(hometext):
    return {
        'id':hometext.id,
        'firstext': hometext.firstext ,
        'secondtext': hometext.secondtext,
        }


class TrackingScript(db.Model):
    __tablename__ = "tracking_script"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=True)
    script = db.Column(db.String(150), nullable=True)

def tracking_script_serializer(tracking_script):
    return {
        'id':tracking_script.id,
        'name': tracking_script.name ,
        'script': tracking_script.script,
        }

class TechnologiesText(db.Model):
    __tablename__ = "technologies_text"
    id = db.Column(db.Integer, primary_key=True)
    firstext = db.Column(db.String(80), nullable=True)
    secondtext = db.Column(db.String(80), nullable=True)

def technologies_text_serializer(technologies_text):
    return {
        'id':technologies_text.id,
        'firstext': technologies_text.firstext ,
        'secondtext': technologies_text.secondtext,
        }

class Service(db.Model):
    __tablename__ = "services"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=True)
    description = db.Column(db.String(80), nullable=True)
    icon = db.Column(db.String(50), nullable=True)

def services_serializer(services):
    return {
        'id':services.id,
        'title': services.title ,
        'description': services.description,
        'icon': services.icon,
        }

class About(db.Model):
    __tablename__ = "about"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(180), nullable=True)
    description = db.Column(db.Text)

def about_serializer(about):
    return {
        'id':about.id,
        'title': about.title ,
        'description': about.description,
        }

class Team(db.Model):
    __tablename__ = "members"
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(80), nullable=True)
    job_title = db.Column(db.String(80), nullable=True)
    image = db.Column(db.String(256), nullable=True)

    @property
    def image_url(self):
        return url_for('_uploads.uploaded_file', setname='images',filename=self.image, external=True)

    @property
    def image_path(self):
        from flask import current_app
        return os.path.join(current_app.config['UPLOADED_IMAGES_DEST'], self.image)

def members_serializer(members):
    return {
        'id':members.id,
        'full_name': members.full_name ,
        'job_title': members.job_title,
        'image': members.image,
        }
    
class Video(db.Model):
    __tablename__ = "video"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=True)
    url = db.Column(db.String(80), nullable=True)
    description = db.Column(db.Text)
    image = db.Column(db.String(256), nullable=True)

    @property
    def image_url(self):
        return url_for('_uploads.uploaded_file', setname='images',filename=self.image, external=True)

    @property
    def image_path(self):
        from flask import current_app
        return os.path.join(current_app.config['UPLOADED_IMAGES_DEST'], self.image)

def video_serializer(video):
    return {
        'id':video.id,
        'title':video.title ,
        'url': video.url,
        'description': video.description,
        }

class Portfolio(db.Model):
    __tablename__ = "portfolio"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=True)
    description = db.Column(db.String(80), nullable=True)
    image = db.Column(db.String(256), nullable=True)

    @property
    def image_url(self):
        return url_for('_uploads.uploaded_file', setname='images',filename=self.image, external=True)

    @property
    def image_path(self):
        from flask import current_app
        return os.path.join(current_app.config['UPLOADED_IMAGES_DEST'], self.image)

def portfolio_serializer(portfolio):
    return {
        'id':portfolio.id,
        'title':portfolio.title ,
        'image': portfolio.image,
        'description': portfolio.description,
        }

class Testimonial(db.Model):
    __tablename__ = "testimonial"
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(80), nullable=True)
    job_title = db.Column(db.String(80), nullable=True)
    comment = db.Column(db.String(140), nullable=True)
    image = db.Column(db.String(256), nullable=True)

    @property
    def image_url(self):
        return url_for('_uploads.uploaded_file', setname='images',filename=self.image, external=True)

    @property
    def image_path(self):
        from flask import current_app
        return os.path.join(current_app.config['UPLOADED_IMAGES_DEST'], self.image)
    
def testimonial_serializer(testimonial):
    return {
        'id':testimonial.id,
        'full_name':testimonial.full_name ,
        'job_title':testimonial.job_title ,
        'image': testimonial.image,
        'comment': testimonial.comment,
        }

class CallToAction(db.Model):
    __tablename__ = "call_to_action"
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(80), nullable=True)
    url = db.Column(db.String(80), nullable=True)

def call_to_action_serializer(call_to_action):
    return {
        'id':call_to_action.id,
        'text':call_to_action.text ,
        'url':testimonial.url ,
        }

class NavMenu(db.Model):
    __tablename__ = "nav_menu"
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(80), nullable=True)
    url = db.Column(db.String(80), nullable=True)

def nav_menu_serializer(nav_menu):
    return {
        'id':nav_menu.id,
        'text':nav_menu.text ,
        'url':nav_menu.url ,
        }

class TechnologiesImage(db.Model):
    __tablename__ = "technologies_images"
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String(256), nullable=True)

    @property
    def image_url(self):
        return url_for('_uploads.uploaded_file', setname='images',filename=self.image, external=True)

    @property
    def image_path(self):
        from flask import current_app
        return os.path.join(current_app.config['UPLOADED_IMAGES_DEST'], self.image)

def technologies_images_serializer(technologies_images):
    return {
        'id':technologies_images.id,
        'image':technologies_images.image ,
        }

class Client(db.Model):
    __tablename__ = "client"
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String(256), nullable=True)

    @property
    def image_url(self):
        return url_for('_uploads.uploaded_file', setname='images',filename=self.image, external=True)

    @property
    def image_path(self):
        from flask import current_app
        return os.path.join(current_app.config['UPLOADED_IMAGES_DEST'], self.image)

def client_serializer(client):
    return {
        'id':client.id,
        'image':client.image ,
        }


class AppleTouchIcon(db.Model):
    __tablename__ = "apple_touch_icon"
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String(256), nullable=True)

    @property
    def image_url(self):
        return url_for('_uploads.uploaded_file', setname='images',filename=self.image, external=True)

    @property
    def image_path(self):
        from flask import current_app
        return os.path.join(current_app.config['UPLOADED_IMAGES_DEST'], self.image)

def apple_touch_icon_serializer(apple_touch_icon):
    return {
        'id':apple_touch_icon.id,
        'image':apple_touch_icon.image ,
        }

    
class Logo(db.Model):
    _tablename_ = "logo"
    id = db.Column(db.Integer, primary_key=True)
    logo_image = db.Column(db.String(256), nullable=True)

    @property
    def image_url(self):
        return url_for('_uploads.uploaded_file', setname='images', filename=self.logo_image, external=True)

    @property
    def image_path(self):
        from flask import current_app
        return os.path.join(current_app.config['UPLOADED_IMAGES_DEST'], self.logo_image)

def logo_serializer(logo):
    return {
        'id':logo.id,
        'image':logo.image ,
        }



class BackgroundImage(db.Model):
    _tablename_ = "background_image"
    id = db.Column(db.Integer, primary_key=True)
    background_image = db.Column(db.String(256), nullable=True)

    @property
    def image_url(self):
        return url_for('_uploads.uploaded_file', setname='images', filename=self.background_image, external=True)

    @property
    def image_path(self):
        from flask import current_app
        return os.path.join(current_app.config['UPLOADED_IMAGES_DEST'], self.background_image)

def background_image_serializer(background_image):
    return {
        'id':background_image.id,
        'image':background_image.image ,
        }


# Favicon Image Model 
class FaviconImage(db.Model):
    __tablename__ = "favicon_image"
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String(256), nullable=True)

    @property
    def image_url(self):
        return url_for('_uploads.uploaded_file', setname='images', filename=self.image, external=True)

    @property
    def image_path(self):
        from flask import current_app
        return os.path.join(current_app.config['UPLOADED_IMAGES_DEST'], self.image)
    
def favicon_image_serializer(favicon_image):
    return {
        'id':favicon__image.id,
        'image':favicon__image.image ,
        }


# Footer Image Model 
class FooterImage(db.Model):
    __tablename__ = "footerimage"
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String(256), nullable=True)

    @property
    def image_url(self):
        return url_for('_uploads.uploaded_file', setname='images', filename=self.image, external=True)

    @property
    def image_path(self):
        from flask import current_app
        return os.path.join(current_app.config['UPLOADED_IMAGES_DEST'], self.image)

def footerimage_serializer(footerimage):
    return {
        'id':footerimage.id,
        'image':footerimage.image ,
        }



#Footer Text Model
class FooterText(db.Model):
    __tablename__ = "footertext"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256), nullable=True)

def footertext_serializer(footertext):
    return {
        'id':footertext.id,
        'title':footertext.title,
        }



# Footer Social Media Icon with link Model
class SocialMediaIcon(db.Model):
    __tablename__ = "socialmediaicon"
    id = db.Column(db.Integer, primary_key=True)
    icon = db.Column(db.String(50), nullable=True)
    url_link = db.Column(db.String(300), nullable=True)

def socialmediaicon_serializer(socialmediaicon):
    return {
        'id':socialmediaicon.id,
        'icon':socialmediaicon.icon,
        'url_link':socialmediaicon.url_link,
        }


# Faq text here
class Faq(db.Model):
    __tablename__ = "faq"
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(50), nullable=True)
    answer = db.Column(db.Text)

def faq_serializer(faq):
    return {
        'id':faq.id,
        'question':faq.question,
        'answer':faq.answer,
        }

# Faq text here
class Location(db.Model):
    __tablename__ = "location"
    id = db.Column(db.Integer, primary_key=True)
    locality = db.Column(db.String(50), nullable=True)
    town = db.Column(db.String(50), nullable=True)

def location_serializer(location):
    return {
        'id':location.id,
        'location':location.locality,
        'town':location.town,
        }
    
# BrandName text here
class BrandName(db.Model):
    __tablename__ = "brandname"
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(15), nullable=True)

def brandname_serializer(brandname):
    return {
        'id':brandname.id,
        'text':brandname.text,
        }

# Copyright text here
class CopyRight(db.Model):
    __tablename__ = "copyright"
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(256), nullable=True)

def copyright_serializer(copyright):
    return {
        'id':copyright.id,
        'text':copyright.text,
        }


# Resources List 
class Resource(db.Model):
    __tablename__ = "resource"
    id = db.Column(db.Integer, primary_key=True)
    role_title = db.Column(db.String(100), nullable=True)
    resourcedetails = db.relationship('ResourceDetail', backref='resource', uselist=False)

def resource_serializer(resource):
    return {
        'id':resource.id,
        'text':resource.text,
        }



# Resources Details Models
class ResourceDetail(db.Model):
    __tablename__ = "resource_detail"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=True)
    description = db.Column(db.String(1000), nullable=True)
    resource_id = db.Column(db.Integer, db.ForeignKey('resource.id'))

def resource_detail_serializer(resource_detail):
    return {
        'id':resource_detail.id,
        'title':resource_detail.title,
        'description':resource_detail.description,
        'resource_id':resource_detail.resource_id,
        }



class Pricing(db.Model):
    __tablename__ = "pricing"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=True)
    description = db.Column(db.String(250), nullable=True)
    pricing_attributes = db.relationship('PricingAttribute', backref='pricing', lazy=True)
    costs = db.relationship('Cost', backref='pricing', lazy=True)

def pricing_serializer(pricing):
    return {
        'id':pricing.id,
        'title':pricing.title,
        'description':pricing.description,
        'pricing_attributes':pricing.pricing_attributes,
        'costs':pricing.costs,
        }


class PricingAttribute(db.Model):
    __tablename__ = "pricing_attribute"
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(120), nullable=True)
    pricing_id = db.Column(db.Integer, db.ForeignKey('pricing.id'),
        nullable=True)

def pricing_attribute_serializer(pricing_attribute):
    return {
        'id':pricing_attribute.id,
        'description':pricing_attribute.description,
        'pricing_id':pricing_attribute.pricing_id,
        }


class Cost(db.Model):
    __tablename__ = "cost"
    id = db.Column(db.Integer, primary_key=True)
    figure = db.Column(db.Float, nullable=True)
    currency = db.Column(db.String(120), nullable=True)
    currency_icon = db.Column(db.String(10), nullable=True)
    pricing_id = db.Column(db.Integer, db.ForeignKey('pricing.id'),
        nullable=True)


def cost_serializer(cost):
    return {
        'id':cost.id,
        'figure':cost.figure,
        'currency':cost.currency,
        'currency_icon':cost.currency_icon,
        'pricing_id':cost.pricing_id,
        }