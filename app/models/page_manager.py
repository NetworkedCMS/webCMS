from app.common.BaseModel import BaseModel
from sqlalchemy import Column, String,Text, Integer


class Page(BaseModel):
    __tablename__ = "page"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=True)
    #seo_title = Column(String(180), nullable=True)
    #seo_description = Column(String(250), nullable=True)
    content = Column(Text)

def page_serializer(page):
    return {
        'id':page.id,
        'name': page.name ,
        'content': page.content,
        }

