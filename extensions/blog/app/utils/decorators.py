from functools import wraps

from aioflask import abort, url_for, redirect
from flask.globals import session
from flask_login import current_user

from app.models import Permission, ApiKey, ApiAccess
from flask_wtf import FlaskForm
from wtforms import ValidationError
from wtforms.fields import (
    StringField,
    SubmitField,
)
from wtforms.validators import EqualTo, InputRequired, Length


class AccessKeyForm(FlaskForm):
    user_input = StringField(
        'Access Token', validators=[InputRequired(),
                             Length(1, 64)])
    submit = SubmitField('Submit')

def permission_required(permission):
    """Restrict a view to users with the given permission."""

    def decorator(f):
        @wraps(f)
        async def decorated_function(*args, **kwargs):
            if not await current_user.can(permission):
                abort(403)
            return f(*args, **kwargs)

        return decorated_function

    return decorator


def admin_required(f):
    return permission_required(Permission.ADMINISTER)(f)


def token_required(f):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not 'session_id' in session:
                 return redirect(url_for('api.access'))
            return f(*args, **kwargs)

        return decorated_function

    return decorator(f)


