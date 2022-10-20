import os

from flask import url_for
from app.common.BaseModel import BaseModel
from sqlalchemy import Column, Text, String,ForeignKey, Integer, Float
from sqlalchemy.orm import relationship


class SlideShowImage(BaseModel):
    __tablename__ = "slide_show_images"
    id = Column(Integer, primary_key=True)
    title = Column(String(80), nullable=True)
    image_filename = Column(String(256), nullable=True)

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

class Seo(BaseModel):
    __tablename__ = "seo"
    id = Column(Integer, primary_key=True)
    meta_tag = Column(String(80), nullable=True)
    title = Column(String(80), nullable=True)
    content = Column(String(256), nullable=True)

def seo_serializer(seo):
    return {
        'id':seo.id,
        'meta_tag': seo.meta_tag ,
        'title': seo.content,
        }


class Setting(BaseModel):
    __tablename__ = "settings"
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=True)
    display_name = Column(String(80), nullable=True)
    value = Column(String(512), nullable=True)


def settings_serializer(settings):
    return {
        'id':settings.id,
        'name': settings.name ,
        'display_name': settings.display_name,
        'value': settings.value,
        }

#####################################################

class Counter(BaseModel):
    __tablename__ = "counter"
    id = Column(Integer, primary_key=True)
    title = Column(String(80), nullable=True)
    count = Column(String(25), nullable=True)

def counter_serializer(counter):
    return {
        'id':counter.id,
        'title': counter.title ,
        }


class HomeText(BaseModel):
    __tablename__ = "hometext"
    id = Column(Integer, primary_key=True)
    firstext = Column(String(80), nullable=True)
    secondtext = Column(Text)

def hometext_serializer(hometext):
    return {
        'id':hometext.id,
        'firstext': hometext.firstext ,
        'secondtext': hometext.secondtext,
        }


class TrackingScript(BaseModel):
    __tablename__ = "tracking_script"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=True)
    script = Column(String(150), nullable=True)

def tracking_script_serializer(tracking_script):
    return {
        'id':tracking_script.id,
        'name': tracking_script.name ,
        'script': tracking_script.script,
        }

class TechnologiesText(BaseModel):
    __tablename__ = "technologies_text"
    id = Column(Integer, primary_key=True)
    firstext = Column(String(80), nullable=True)
    secondtext = Column(String(80), nullable=True)

def technologies_text_serializer(technologies_text):
    return {
        'id':technologies_text.id,
        'firstext': technologies_text.firstext ,
        'secondtext': technologies_text.secondtext,
        }

class Service(BaseModel):
    __tablename__ = "services"
    id = Column(Integer, primary_key=True)
    title = Column(String(80), nullable=True)
    description = Column(String(80), nullable=True)
    icon = Column(String(50), nullable=True)

def services_serializer(services):
    return {
        'id':services.id,
        'title': services.title ,
        'description': services.description,
        'icon': services.icon,
        }

class About(BaseModel):
    __tablename__ = "about"
    id = Column(Integer, primary_key=True)
    title = Column(String(180), nullable=True)
    description = Column(Text)

def about_serializer(about):
    return {
        'id':about.id,
        'title': about.title ,
        'description': about.description,
        }

class Team(BaseModel):
    __tablename__ = "members"
    id = Column(Integer, primary_key=True)
    full_name = Column(String(80), nullable=True)
    job_title = Column(String(80), nullable=True)
    image = Column(String(256), nullable=True)

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
    
class Video(BaseModel):
    __tablename__ = "video"
    id = Column(Integer, primary_key=True)
    title = Column(String(80), nullable=True)
    url = Column(String(80), nullable=True)
    description = Column(Text)
    image = Column(String(256), nullable=True)

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

class Portfolio(BaseModel):
    __tablename__ = "portfolio"
    id = Column(Integer, primary_key=True)
    title = Column(String(80), nullable=True)
    description = Column(String(80), nullable=True)
    image = Column(String(256), nullable=True)

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

class Testimonial(BaseModel):
    __tablename__ = "testimonial"
    id = Column(Integer, primary_key=True)
    full_name = Column(String(80), nullable=True)
    job_title = Column(String(80), nullable=True)
    comment = Column(String(140), nullable=True)
    image = Column(String(256), nullable=True)

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

class CallToAction(BaseModel):
    __tablename__ = "call_to_action"
    id = Column(Integer, primary_key=True)
    text = Column(String(80), nullable=True)
    url = Column(String(80), nullable=True)

def call_to_action_serializer(call_to_action):
    return {
        'id':call_to_action.id,
        'text':call_to_action.text ,
        'url':call_to_action.url ,
        }

class NavMenu(BaseModel):
    __tablename__ = "nav_menu"
    id = Column(Integer, primary_key=True)
    text = Column(String(80), nullable=True)
    url = Column(String(80), nullable=True)

def nav_menu_serializer(nav_menu):
    return {
        'id':nav_menu.id,
        'text':nav_menu.text ,
        'url':nav_menu.url ,
        }

class TechnologiesImage(BaseModel):
    __tablename__ = "technologies_images"
    id = Column(Integer, primary_key=True)
    image = Column(String(256), nullable=True)

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

class Client(BaseModel):
    __tablename__ = "client"
    id = Column(Integer, primary_key=True)
    image = Column(String(256), nullable=True)

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


class AppleTouchIcon(BaseModel):
    __tablename__ = "apple_touch_icon"
    id = Column(Integer, primary_key=True)
    image = Column(String(256), nullable=True)

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

    
class Logo(BaseModel):
    _tablename_ = "logo"
    id = Column(Integer, primary_key=True)
    logo_image = Column(String(256), nullable=True)

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



class BackgroundImage(BaseModel):
    _tablename_ = "background_image"
    id = Column(Integer, primary_key=True)
    background_image = Column(String(256), nullable=True)

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
class FaviconImage(BaseModel):
    __tablename__ = "favicon_image"
    id = Column(Integer, primary_key=True)
    image = Column(String(256), nullable=True)

    @property
    def image_url(self):
        return url_for('_uploads.uploaded_file', setname='images', filename=self.image, external=True)

    @property
    def image_path(self):
        from flask import current_app
        return os.path.join(current_app.config['UPLOADED_IMAGES_DEST'], self.image)
    
def favicon_image_serializer(favicon_image):
    return {
        'id':favicon_image.id,
        'image':favicon_image.image ,
        }


# Footer Image Model 
class FooterImage(BaseModel):
    __tablename__ = "footerimage"
    id = Column(Integer, primary_key=True)
    image = Column(String(256), nullable=True)

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
class FooterText(BaseModel):
    __tablename__ = "footertext"
    id = Column(Integer, primary_key=True)
    title = Column(String(256), nullable=True)

def footertext_serializer(footertext):
    return {
        'id':footertext.id,
        'title':footertext.title,
        }



# Footer Social Media Icon with link Model
class SocialMediaIcon(BaseModel):
    __tablename__ = "socialmediaicon"
    id = Column(Integer, primary_key=True)
    icon = Column(String(50), nullable=True)
    url_link = Column(String(300), nullable=True)

def socialmediaicon_serializer(socialmediaicon):
    return {
        'id':socialmediaicon.id,
        'icon':socialmediaicon.icon,
        'url_link':socialmediaicon.url_link,
        }


# Faq text here
class Faq(BaseModel):
    __tablename__ = "faq"
    id = Column(Integer, primary_key=True)
    question = Column(String(50), nullable=True)
    answer = Column(Text)

def faq_serializer(faq):
    return {
        'id':faq.id,
        'question':faq.question,
        'answer':faq.answer,
        }

# Faq text here
class Location(BaseModel):
    __tablename__ = "location"
    id = Column(Integer, primary_key=True)
    locality = Column(String(50), nullable=True)
    town = Column(String(50), nullable=True)

def location_serializer(location):
    return {
        'id':location.id,
        'location':location.locality,
        'town':location.town,
        }
    
# BrandName text here
class BrandName(BaseModel):
    __tablename__ = "brandname"
    id = Column(Integer, primary_key=True)
    text = Column(String(15), nullable=True)

def brandname_serializer(brandname):
    return {
        'id':brandname.id,
        'text':brandname.text,
        }

# Copyright text here
class CopyRight(BaseModel):
    __tablename__ = "copyright"
    id = Column(Integer, primary_key=True)
    text = Column(String(256), nullable=True)

def copyright_serializer(copyright):
    return {
        'id':copyright.id,
        'text':copyright.text,
        }


# Resources List 
class Resource(BaseModel):
    __tablename__ = "resource"
    id = Column(Integer, primary_key=True)
    role_title = Column(String(100), nullable=True)
    resourcedetails = relationship('ResourceDetail', backref='resource', uselist=False)

def resource_serializer(resource):
    return {
        'id':resource.id,
        'text':resource.text,
        }



# Resources Details Models
class ResourceDetail(BaseModel):
    __tablename__ = "resource_detail"
    id = Column(Integer, primary_key=True)
    title = Column(String(150), nullable=True)
    description = Column(String(1000), nullable=True)
    resource_id = Column(Integer, ForeignKey('resource.id'))

def resource_detail_serializer(resource_detail):
    return {
        'id':resource_detail.id,
        'title':resource_detail.title,
        'description':resource_detail.description,
        'resource_id':resource_detail.resource_id,
        }



class Pricing(BaseModel):
    __tablename__ = "pricing"
    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=True)
    description = Column(String(250), nullable=True)
    pricing_attributes = relationship('PricingAttribute', backref='pricing', lazy=True)
    costs = relationship('Cost', backref='pricing', lazy=True)

def pricing_serializer(pricing):
    return {
        'id':pricing.id,
        'title':pricing.title,
        'description':pricing.description,
        'pricing_attributes':pricing.pricing_attributes,
        'costs':pricing.costs,
        }


class PricingAttribute(BaseModel):
    __tablename__ = "pricing_attribute"
    id = Column(Integer, primary_key=True)
    description = Column(String(120), nullable=True)
    pricing_id = Column(Integer, ForeignKey('pricing.id'),
        nullable=True)

def pricing_attribute_serializer(pricing_attribute):
    return {
        'id':pricing_attribute.id,
        'description':pricing_attribute.description,
        'pricing_id':pricing_attribute.pricing_id,
        }


class Cost(BaseModel):
    __tablename__ = "cost"
    id = Column(Integer, primary_key=True)
    figure = Column(Float, nullable=True)
    currency = Column(String(120), nullable=True)
    currency_icon = Column(String(10), nullable=True)
    pricing_id = Column(Integer, ForeignKey('pricing.id'),
        nullable=True)


def cost_serializer(cost):
    return {
        'id':cost.id,
        'figure':cost.figure,
        'currency':cost.currency,
        'currency_icon':cost.currency_icon,
        'pricing_id':cost.pricing_id,
        }
