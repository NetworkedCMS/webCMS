from app.common.BaseModel import BaseModel
from sqlalchemy import Column, Text, String, Integer
from sqlalchemy.ext.asyncio import AsyncSession


class EditableHTML(BaseModel):
    id = Column(Integer, primary_key=True)
    editor_name = Column(String(100), unique=True)
    value = Column(Text)

    @staticmethod
    async def get_editable_html(editor_name, session:AsyncSession):
        editable_html_obj = await EditableHTML.get_by_field(
            editor_name, 'editor_name' ,session)

        if editable_html_obj is None:
            editable_html_obj = EditableHTML(editor_name=editor_name, value='')
        return editable_html_obj
