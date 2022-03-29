import os

from flask import url_for
from .. import db


class HtmlContent(db.Model):
    __tablename__ = 'html_content'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    #user = db.relationship("User", back_populates="html_contents")

    ''' html_content is the parent of the following '''

    csses = db.relationship("Css", backref="html_content")
    footer_html = db.relationship("FooterHtml", backref="html_content")
    header_html = db.relationship("HeaderHtml", backref="html_content")
    navbar_html = db.relationship("NavbarHtml", backref="html_content")
    
class Css(db.Model):
    __tablename__ = "css"
    id = db.Column(db.Integer, primary_key=True)
    css_filename = db.Column(db.String(256), nullable=True)
    html_content_id = db.Column(db.Integer, db.ForeignKey('html_content.id'))
    #html_content = db.relationship("HtmlContent", back_populates="csses")

    @property
    def css_url(self):
        return url_for('_uploads.uploaded_file', setname='docs',filename=self.css_filename, external=True)

    @property
    def css_path(self):
        from flask import current_app
        return os.path.join(current_app.config['UPLOADED_DOCS_DEST'], self.css_filename)


class FooterHtml(db.Model):
    __tablename__ = "footer_html"
    id = db.Column(db.Integer, primary_key=True)
    html = db.Column(db.Text)
    html_content_id = db.Column(db.Integer, db.ForeignKey('html_content.id'))
    #html_content = db.relationship("HtmlContent", back_populates="footer_html")

class HeaderHtml(db.Model):
    __tablename__ = "header_html"
    id = db.Column(db.Integer, primary_key=True)
    html = db.Column(db.Text)
    html_content_id = db.Column(db.Integer, db.ForeignKey('html_content.id'))
    #html_content = db.relationship("HtmlContent", back_populates="header_html")

class NavbarHtml(db.Model):
    __tablename__ = "navbar_html"
    id = db.Column(db.Integer, primary_key=True)
    html = db.Column(db.Text)
    html_content_id = db.Column(db.Integer, db.ForeignKey('html_content.id'))
    #html_content = db.relationship("HtmlContent", back_populates="navbar_html")

class FooterScript(db.Model):
    __tablename__ = "footer_script"
    id = db.Column(db.Integer, primary_key=True)
    js = db.Column(db.Text)

class HeaderScript(db.Model):
    __tablename__ = "header_script"
    id = db.Column(db.Integer, primary_key=True)
    js = db.Column(db.Text)

class CarouselHtml(db.Model):
    __tablename__ = "carousel_html"
    id = db.Column(db.Integer, primary_key=True)
    html = db.Column(db.Text)

class AlbumHtml(db.Model):
    __tablename__ = "album_html"
    id = db.Column(db.Integer, primary_key=True)
    html = db.Column(db.Text)

class BlankHtml(db.Model):
    __tablename__ = "blank_html"
    id = db.Column(db.Integer, primary_key=True)
    html = db.Column(db.Text)

class FormHtml(db.Model):
    __tablename__ = "form_html"
    id = db.Column(db.Integer, primary_key=True)
    form_name = db.Column(db.String(80), nullable=True)
    html = db.Column(db.Text)

class JumbotronHtml(db.Model):
    __tablename__ = "jumbotron_html"
    id = db.Column(db.Integer, primary_key=True)
    html = db.Column(db.Text)

class FeaturesHtml(db.Model):
    __tablename__ = "features_html"
    id = db.Column(db.Integer, primary_key=True)
    html = db.Column(db.Text)

class PricingHtml(db.Model):
    __tablename__ = "pricing_html"
    id = db.Column(db.Integer, primary_key=True)
    html = db.Column(db.Text)

class TestimonialsHtml(db.Model):
    __tablename__ = "testimonials_html"
    id = db.Column(db.Integer, primary_key=True)
    html = db.Column(db.Text)

class ContactHtml(db.Model):
    __tablename__ = "contact_html"
    id = db.Column(db.Integer, primary_key=True)
    html = db.Column(db.Text)
    
class MetatagsHtml(db.Model):
    __tablename__ = "metatags_html"
    id = db.Column(db.Integer, primary_key=True)
    html = db.Column(db.Text)

class LinkHtml(db.Model):
    __tablename__ = "link_html"
    id = db.Column(db.Integer, primary_key=True)
    html = db.Column(db.Text)

class TitleHtml(db.Model):
    __tablename__ = "title_html"
    id = db.Column(db.Integer, primary_key=True)
    html = db.Column(db.Text)

