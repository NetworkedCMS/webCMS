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


class Seo(db.Model):
    __tablename__ = "seo"
    id = db.Column(db.Integer, primary_key=True)
    meta_tag = db.Column(db.String(80), nullable=True)
    title = db.Column(db.String(80), nullable=True)
    content = db.Column(db.String(256), nullable=True)


class Setting(db.Model):
    __tablename__ = "settings"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=True)
    display_name = db.Column(db.String(80), nullable=True)
    value = db.Column(db.String(512), nullable=True)

#####################################################

class Counter(db.Model):
    __tablename__ = "counter"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=True)
    count = db.Column(db.String(25), nullable=True)

class HomeText(db.Model):
    __tablename__ = "hometext"
    id = db.Column(db.Integer, primary_key=True)
    firstext = db.Column(db.String(80), nullable=True)
    secondtext = db.Column(db.Text)

class TrackingScript(db.Model):
    __tablename__ = "tracking_script"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=True)
    script = db.Column(db.String(150), nullable=True)

class TechnologiesText(db.Model):
    __tablename__ = "technologies_text"
    id = db.Column(db.Integer, primary_key=True)
    firstext = db.Column(db.String(80), nullable=True)
    secondtext = db.Column(db.String(80), nullable=True)

class Service(db.Model):
    __tablename__ = "services"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=True)
    description = db.Column(db.String(80), nullable=True)
    icon = db.Column(db.String(50), nullable=True)

class About(db.Model):
    __tablename__ = "about"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(180), nullable=True)
    description = db.Column(db.Text)

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

class CallToAction(db.Model):
    __tablename__ = "call_to_action"
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(80), nullable=True)
    url = db.Column(db.String(80), nullable=True)

class NavMenu(db.Model):
    __tablename__ = "nav_menu"
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(80), nullable=True)
    url = db.Column(db.String(80), nullable=True)

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


#Footer Text Model
class FooterText(db.Model):
    __tablename__ = "footertext"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256), nullable=True)


# Footer Social Media Icon with link Model
class SocialMediaIcon(db.Model):
    __tablename__ = "socialmediaicon"
    id = db.Column(db.Integer, primary_key=True)
    icon = db.Column(db.String(50), nullable=True)
    url_link = db.Column(db.String(300), nullable=True)



# Faq text here
class Faq(db.Model):
    __tablename__ = "faq"
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(50), nullable=True)
    answer = db.Column(db.Text)

# Faq text here
class Location(db.Model):
    __tablename__ = "location"
    id = db.Column(db.Integer, primary_key=True)
    locality = db.Column(db.String(50), nullable=True)
    town = db.Column(db.String(50), nullable=True)


    
# BrandName text here
class BrandName(db.Model):
    __tablename__ = "brandname"
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(15), nullable=True)

# Copyright text here
class CopyRight(db.Model):
    __tablename__ = "copyright"
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(256), nullable=True)


# Resources List 
class Resource(db.Model):
    __tablename__ = "resource"
    id = db.Column(db.Integer, primary_key=True)
    role_title = db.Column(db.String(100), nullable=True)
    resourcedetails = db.relationship('ResourceDetail', backref='resource', uselist=False)


# Resources Details Models
class ResourceDetail(db.Model):
    __tablename__ = "resource_detail"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=True)
    description = db.Column(db.String(1000), nullable=True)
    resource_id = db.Column(db.Integer, db.ForeignKey('resource.id'))

class Pricing(db.Model):
    __tablename__ = "pricing"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=True)
    description = db.Column(db.String(250), nullable=True)
    pricing_attributes = db.relationship('PricingAttribute', backref='pricing', lazy=True)
    costs = db.relationship('Cost', backref='pricing', lazy=True)


class PricingAttribute(db.Model):
    __tablename__ = "pricing_attribute"
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(120), nullable=True)
    pricing_id = db.Column(db.Integer, db.ForeignKey('pricing.id'),
        nullable=True)

class Cost(db.Model):
    __tablename__ = "cost"
    id = db.Column(db.Integer, primary_key=True)
    figure = db.Column(db.Float, nullable=True)
    currency = db.Column(db.String(120), nullable=True)
    currency_icon = db.Column(db.String(10), nullable=True)
    pricing_id = db.Column(db.Integer, db.ForeignKey('pricing.id'),
        nullable=True)


