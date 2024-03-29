import aiofiles
from flask import url_for
from wtforms.fields import Field
from wtforms.widgets import HiddenInput
from aioflask.patched.flask_login import LoginManager

from redis import Redis
from rq import Queue
from config import Config


redis_conn = Redis(host=Config.RQ_DEFAULT_HOST, 
    port=Config.RQ_DEFAULT_PORT, db=0, 
    password=Config.RQ_DEFAULT_PASSWORD)

redis_q = Queue('high', connection=redis_conn)


# Set up Flask-Login
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'account.login'



def register_template_utils(app):
    """Register Jinja 2 helpers (called from __init__.py)."""

    @app.template_test()
    def equalto(value, other):
        return value == other

    @app.template_global()
    def is_hidden_field(field):
        from wtforms.fields import HiddenField
        return isinstance(field, HiddenField)

    app.add_template_global(index_for_role)



def index_for_role(role):
    return url_for(role.index)


class CustomSelectField(Field):
    widget = HiddenInput()

    def __init__(self, label='', validators=None, multiple=False,
                 choices=[], allow_custom=True, **kwargs):
        super(CustomSelectField, self).__init__(label, validators, **kwargs)
        self.multiple = multiple
        self.choices = choices
        self.allow_custom = allow_custom

    def _value(self):
        return str(self.data) if self.data is not None else ''

    def process_formdata(self, valuelist):
        if valuelist:
            self.data = valuelist[1]
            self.raw_data = [valuelist[1]]
        else:
            self.data = ''




async def create_template(file_name:str, **kwargs):
    try:
        async with aiofiles.open(f"{file_name}", 'w') as f:
            await f.write(**kwargs)
    except Exception as e:
        raise Exception
    

