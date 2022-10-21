from app.common.BaseModel import BaseModel
from sqlalchemy import Column, Boolean, String,ForeignKey, Integer, Text
from sqlalchemy.orm import relationship

class ContactMessage(BaseModel):
    __tablename__ = 'contact_messages'
    id = Column(Integer, primary_key=True, autoincrement=True)
    read = Column(Boolean, default=False)
    spam = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey('users.id', ondelete="CASCADE"), nullable=True)
    name = Column(String(), default=None, nullable=True)
    email = Column(String(64), default=None, nullable=True)
    text = Column(Text)
    user = relationship("User")

def contact_messages_serializer(contact_messages):
    return {
        'id':contact_messages.id,
        'read': contact_messages.read ,
        'name': contact_messages.name,
        'email': contact_messages.email,
        'text': contact_messages.text,
        'created_at': contact_messages.created_at,
        }