import os

from flask import url_for
from .. import db


class ContactMessage(db.Model):
    __tablename__ = 'contact_messages'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    read = db.Column(db.Boolean, default=False)
    spam = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete="CASCADE"), nullable=True)
    name = db.Column(db.String(), default=None, nullable=True)
    email = db.Column(db.String(64), default=None, nullable=True)
    text = db.Column(db.Text)
    user = db.relationship("User")
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())

def contact_messages_serializer(contact_messages):
    return {
        'id':contact_messages.id,
        'read': contact_messages.read ,
        'name': contact_messages.name,
        'email': contact_messages.email,
        'text': contact_messages.text,
        'created_at': contact_messages.created_at,
        }