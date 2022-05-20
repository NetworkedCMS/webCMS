import os
from app.common.BaseModel import BaseModel
from sqlalchemy import Column, Boolean, String, Integer
from flask import url_for


class TemplateSetting(BaseModel):
    __tablename__ = "template_settings"
    id = Column(Integer, primary_key=True)
    template_name = Column(String(80), nullable=True)
    category = Column(String(80), nullable=True)
    choice = Column(Boolean, default=False, index=True)
    image = Column(String(256), nullable=True)
    

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

    

class TemplateChoice(BaseModel):
    __tablename__ = "template_choice"
    id = Column(Integer, primary_key=True)
    template_name = Column(String(80), nullable=True)
    choice = Column(Boolean, default=False, index=True)


def template_choice_serializer(template_choice):
    return {
        'id':template_choice.id,
        'template_name': template_choice.template_name ,
        'choice': template_choice.choice,
        }
