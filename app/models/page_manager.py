import os

from flask import url_for
from .. import db


class Page(db.Model):
    __tablename__ = "page"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=True)
    #seo_title = db.Column(db.String(180), nullable=True)
    #seo_description = db.Column(db.String(250), nullable=True)
    content = db.Column(db.Text)
