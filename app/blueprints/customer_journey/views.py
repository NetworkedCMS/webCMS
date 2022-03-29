from flask import (
    Blueprint,
    abort,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)
from flask_login import current_user, login_required
from flask_rq import get_queue
from flask_ckeditor import upload_success
from flask_sqlalchemy import Pagination

from app import db
#from app.admin.forms import (
    #ChangeAccountTypeForm,
    #ChangeUserEmailForm,
    #InviteUserForm,
    #NewUserForm,
#)
from app.decorators import admin_required
from app.email import send_email
from app.models import *
from app.models.content_manager import Headline
from app.blueprints.content_manager.forms import *

customer_journey = Blueprint('customer_journey', __name__)


@customer_journey.route('/brandname', methods=['GET', 'POST'])
@login_required
def add_brand_name():
    """Add a new brand name."""
    item = BrandName.query.first()
    if item is not None:
        return redirect(url_for('customer_journey.added_brandname'))
        
    form = BrandNameForm()
    if form.validate_on_submit():
        data = BrandName(
            text=form.text.data
            )
        db.session.add(data)
        db.session.commit()
        flash('BrandName {} successfully created'.format(data.text),
              'form-success')
        return redirect(url_for('template_manager.index'))
    return render_template('content_manager/brandname/add_brandname.html', form=form)

