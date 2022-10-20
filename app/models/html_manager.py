import os

from flask import url_for
from app.common.BaseModel import BaseModel
from sqlalchemy import Column, Text, String,Integer


class Css(BaseModel):
    __tablename__ = "css"
    id = Column(Integer, primary_key=True)
    css_filename = Column(String(256), nullable=True)

    @property
    def css_url(self):
        return url_for('_uploads.uploaded_file', setname='docs',filename=self.css_filename, external=True)

    @property
    def css_path(self):
        from flask import current_app
        return os.path.join(current_app.config['UPLOADED_DOCS_DEST'], self.css_filename)


class FooterHtml(BaseModel):
    __tablename__ = "footer_html"
    id = Column(Integer, primary_key=True)
    html = Column(Text)

class HeaderHtml(BaseModel):
    __tablename__ = "header_html"
    id = Column(Integer, primary_key=True)
    html = Column(Text)

class NavbarHtml(BaseModel):
    __tablename__ = "navbar_html"
    id = Column(Integer, primary_key=True)
    html = Column(Text)

class FooterScript(BaseModel):
    __tablename__ = "footer_script"
    id = Column(Integer, primary_key=True)
    js = Column(Text)

class HeaderScript(BaseModel):
    __tablename__ = "header_script"
    id = Column(Integer, primary_key=True)
    js = Column(Text)

class CarouselHtml(BaseModel):
    __tablename__ = "carousel_html"
    id = Column(Integer, primary_key=True)
    html = Column(Text)

class AlbumHtml(BaseModel):
    __tablename__ = "album_html"
    id = Column(Integer, primary_key=True)
    html = Column(Text)

class BlankHtml(BaseModel):
    __tablename__ = "blank_html"
    id = Column(Integer, primary_key=True)
    html = Column(Text)

class FormHtml(BaseModel):
    __tablename__ = "form_html"
    id = Column(Integer, primary_key=True)
    form_name = Column(String(80), nullable=True)
    html = Column(Text)

class JumbotronHtml(BaseModel):
    __tablename__ = "jumbotron_html"
    id = Column(Integer, primary_key=True)
    html = Column(Text)

class FeaturesHtml(BaseModel):
    __tablename__ = "features_html"
    id = Column(Integer, primary_key=True)
    html = Column(Text)

class PricingHtml(BaseModel):
    __tablename__ = "pricing_html"
    id = Column(Integer, primary_key=True)
    html = Column(Text)

class TestimonialsHtml(BaseModel):
    __tablename__ = "testimonials_html"
    id = Column(Integer, primary_key=True)
    html = Column(Text)

class ContactHtml(BaseModel):
    __tablename__ = "contact_html"
    id = Column(Integer, primary_key=True)
    html = Column(Text)
    
class MetatagsHtml(BaseModel):
    __tablename__ = "metatags_html"
    id = Column(Integer, primary_key=True)
    html = Column(Text)

class LinkHtml(BaseModel):
    __tablename__ = "link_html"
    id = Column(Integer, primary_key=True)
    html = Column(Text)

class TitleHtml(BaseModel):
    __tablename__ = "title_html"
    id = Column(Integer, primary_key=True)
    html = Column(Text)

