import os

from flask import url_for
from .. import db


class Template(db.Model):
    __tablename__ = 'template'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    #user = db.relationship("User", back_populates="templates")
    ''' template is the parent of template_settings '''

    template_settings = db.relationship("TemplateSetting", back_populates="template")

class TemplateSetting(db.Model):
    __tablename__ = "template_settings"
    id = db.Column(db.Integer, primary_key=True)
    template_name = db.Column(db.String(80), nullable=True)
    category = db.Column(db.String(80), nullable=True)
    choice = db.Column(db.Boolean, default=False, index=True)
    image = db.Column(db.String(256), nullable=True)
    ''' template_settings is a child of template. Template is the parent ''' 

    template_id = db.Column(db.Integer, db.ForeignKey('template.id'))
    template = db.relationship("Template", back_populates="template_settings")
    

    @property
    def image_url(self):
        return url_for('_uploads.uploaded_file', setname='images',filename=self.image, external=True)

    @property
    def image_path(self):
        from flask import current_app
        return os.path.join(current_app.config['UPLOADED_IMAGES_DEST'], self.image)

def template_settings_serializer(template_settings):
    return {
        'id':template_settings.id,
        'template_name': template_settings.template_name ,
        'category': template_settings.category,
        'choice': template_settings.choice,
        'image': template_settings.image,
        }

    

class TemplateChoice(db.Model):
    __tablename__ = "template_choice"
    id = db.Column(db.Integer, primary_key=True)
    template_name = db.Column(db.String(80), nullable=True)
    choice = db.Column(db.Boolean, default=False, index=True)


def template_choice_serializer(template_choice):
    return {
        'id':template_choice.id,
        'template_name': template_choice.template_name ,
        'choice': template_choice.choice,
        }
