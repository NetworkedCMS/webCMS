from aioflask import (
    Blueprint,
    abort,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)
from aioflask.patched.flask_login import current_user, login_required
from app.utils.dep import redis_q

from app.common.db import db_session as session
from app.blueprints.admin.forms import (
    ChangeAccountTypeForm,
    ChangeUserEmailForm,
    InviteUserForm,
    NewUserForm,
)
from app.utils.decorators import admin_required
from app.utils.email import send_email
from app.models import EditableHTML, Role, User

admin = Blueprint('admin', __name__)


@admin.route('/')
@login_required
@admin_required
async def index():
    """Admin dashboard page."""
    return await render_template('admin/index.html')


@admin.route('/new-user', methods=['GET', 'POST'])
@login_required
@admin_required
async def new_user():
    """Create a new user."""
    form = NewUserForm()
    if form.validate_on_submit():
        user = User(
            role=form.role.data,
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email=form.email.data,
            password=form.password.data)
        session.add(user)
        await session.commit()
        flash('User {} successfully created'.format(user.full_name()),
              'form-success')
    return await render_template('admin/new_user.html', form=form)


@admin.route('/invite-user', methods=['GET', 'POST'])
@login_required
@admin_required
async def invite_user():
    """Invites a new user to create an account and set their own password."""
    form = InviteUserForm()
    if form.validate_on_submit():
        user = await User.create(
            **dict(role=form.role.data,
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email=form.email.data))
        token = user.generate_confirmation_token()
        invite_link = url_for(
            'account.join_from_invite',
            user_id=user.id,
            token=token,
            _external=True)
        redis_q.enqueue(
            send_email,
            recipient=user.email,
            subject='You Are Invited To Join',
            template='account/email/invite',
            user=user,
            invite_link=invite_link,
        )
        flash('User {} successfully invited'.format(user.full_name()),
              'form-success')
    return await render_template('admin/new_user.html', form=form)


@admin.route('/users')
@login_required
@admin_required
async def registered_users():
    """View all registered users."""
    users = await User.all()
    roles = await Role.all()
    return await render_template(
        'admin/registered_users.html', users=users, roles=roles)


@admin.route('/user/<int:user_id>')
@admin.route('/user/<int:user_id>/info')
@login_required
@admin_required
async def user_info(user_id):
    """View a user's profile."""
    user = await User.get(user_id)
    if user is None:
        raise Exception
    return await render_template('admin/manage_user.html', user=user)


@admin.route('/user/<int:user_id>/change-email', methods=['GET', 'POST'])
@login_required
@admin_required
async def change_user_email(user_id):
    """Change a user's email."""
    user = await User.get(id=user_id)
    if user is None:
        raise Exception
    form = ChangeUserEmailForm()
    if form.validate_on_submit():
        user.email = form.email.data
        session.add(user)
        await session.commit()
        flash('Email for user {} successfully changed to {}.'.format(
            user.full_name(), user.email), 'form-success')
    return await render_template('admin/manage_user.html', user=user, form=form)


@admin.route(
    '/user/<int:user_id>/change-account-type', methods=['GET', 'POST'])
@login_required
@admin_required
async def change_account_type(user_id):
    """Change a user's account type."""
    if current_user.id == user_id:
        flash('You cannot change the type of your own account. Please ask '
              'another administrator to do this.', 'error')
        return redirect(url_for('admin.user_info', user_id=user_id))

    user = await User.get(user_id)
    if user is None:
        raise Exception
    form = ChangeAccountTypeForm()
    if form.validate_on_submit():
        user.role = form.role.data
        session.add(user)
        await session.commit()
        flash('Role for user {} successfully changed to {}.'.format(
            user.full_name(), user.role.name), 'form-success')
    return await render_template('admin/manage_user.html', user=user, form=form)


@admin.route('/user/<int:user_id>/delete')
@login_required
@admin_required
async def delete_user_request(user_id):
    """Request deletion of a user's account."""
    user = User.get(id=user_id)
    if user is None:
        raise Exception
    return await render_template('admin/manage_user.html', user=user)


@admin.route('/user/<int:user_id>/_delete')
@login_required
@admin_required
async def delete_user(user_id):
    """Delete a user's account."""
    if current_user.id == user_id:
        flash('You cannot delete your own account. Please ask another '
              'administrator to do this.', 'error')
    else:
        user = await User.get(user_id)
        await session.delete(user)
        flash('Successfully deleted user %s.' % user.full_name(), 'success')
    return redirect(url_for('admin.registered_users'))


@admin.route('/_update_editor_contents', methods=['POST'])
@login_required
@admin_required
async def update_editor_contents():
    """Update the contents of an editor."""

    edit_data = request.form.get('edit_data')
    editor_name = request.form.get('editor_name')

    editor_contents = await EditableHTML.get_or_404(
        editor_name, 'editor_name')
    if editor_contents is None:
        editor_contents = EditableHTML(editor_name=editor_name)
    editor_contents.value = edit_data

    session.add(editor_contents)
    await session.commit()

    return 'OK', 200
