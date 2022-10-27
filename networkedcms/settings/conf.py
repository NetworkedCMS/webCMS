from pydantic import BaseModel


class SiteSettings(BaseModel):
    """NetworkedCMS Global site settings"""
    MONGO_CONN_URI:str = None

    MONGO_DATABASE:str = None

    # Data pagination
    PER_PAGE:int = 10

    # Sqlalchemy database
    SQLALCHEMY_DB:str = None
    SQLALCHEMY_URI:str = None

    # File Upload path
    DOC_UPLOAD_PATH:str
    IMAGE_UPLOAD_PATH:str
    



settings = SiteSettings()
