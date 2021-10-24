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
from app.models import *
from app.blueprints.messaging_manager.forms import *
from app.blueprints.messaging_manager.views import messaging_manager

messaging_manager = Blueprint('messaging_manager', __name__)



@messaging_manager.route('/contact_messages', defaults={'page': 1, 'mtype': 'primary'}, methods=['GET'])
@messaging_manager.route('/contact_messages/<string:mtype>', defaults={'page': 1}, methods=['GET'])
@messaging_manager.route('/contact_messages/<string:mtype>/<int:page>', defaults={'mtype': 'primary'}, methods=['GET'])
@login_required
def contact_messages(mtype, page):
    if mtype == 'primary':
        contact_messages_result = ContactMessage.query.filter_by(spam=False).order_by(
            ContactMessage.created_at.desc()).paginate(page, per_page=100)
    elif mtype == 'spam':
        contact_messages_result = ContactMessage.query.filter(
            (ContactMessage.spam == True) | (ContactMessage.spam == None)).order_by(
            ContactMessage.created_at.desc()).paginate(page, per_page=100)
        print(contact_messages_result.items)
    else:
        abort(404)
    return render_template('messaging_manager/contact_messages/browse.html', contact_messages=contact_messages_result, mtype=mtype)


@messaging_manager.route('/contact_message/<message_id>', methods=['GET'])
@login_required
def view_contact_message(message_id):
    message = ContactMessage.query.filter_by(id=message_id).first_or_404()
    message.read = True
    db.session.commit()
    return render_template('messaging_manager/contact_messages/view.html', contact_message=message)


@messaging_manager.route('/contact_messages/<int:message_id>/_delete', methods=['POST'])
@login_required
def delete_contact_message(message_id):
    message = ContactMessage.query.filter_by(id=message_id).first()
    db.session.delete(message)
    db.session.commit()
    flash('Successfully deleted Message.', 'success')
    return redirect(url_for('messaging_manager.contact_messages'))


@messaging_manager.route('/contact_messages/<int:message_id>/_toggle', methods=['POST'])
@login_required
def toggle_message(message_id):
    message = ContactMessage.query.filter_by(id=message_id).first()
    message.spam = not message.spam
    db.session.commit()
    flash('Successfully toggles Message status.', 'success')
    return redirect(url_for('messaging_manager.contact_messages'))


@messaging_manager.route('/contact_messages/batch_toggle', methods=['POST'])
@login_required
def batch_toggle():
    try:
        ids = json.loads(request.form.get('items'))
    except:
        flash('Something went wrong, pls try again.', 'error')
        return redirect(url_for('messaging_manager.contact_messages'))

    messages = ContactMessage.query.filter(ContactMessage.id.in_(ids)).all()
    print(messages)
    for message in messages:
        message.spam = not message.spam
    db.session.commit()
    flash('Successfully toggles Messages status.', 'success')
    return redirect(url_for('messaging_manager.contact_messages'))


@messaging_manager.route('/contact_messages/batch_delete', methods=['POST'])
@login_required
def batch_delete():
    try:
        ids = json.loads(request.form.get('items'))
    except:
        flash('Something went wrong, pls try again.', 'error')
        return redirect(url_for('messaging_manager.contact_messages'))

    messages = ContactMessage.query.filter(ContactMessage.id.in_(ids)).delete(synchronize_session=False)
    # db.session.delete(messages)
    db.session.commit()
    flash('Successfully deleted Messages.', 'success')
    return redirect(url_for('messaging_manager.contact_messages'))