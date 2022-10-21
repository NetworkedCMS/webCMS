
from aioflask import (
    Blueprint,
    abort,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)
from aioflask.patched.flask_login import login_required
#from app.page_manager.forms import (
    #ChangeAccountTypeForm,
    #ChangeUserEmailForm,
    #InviteUserForm,
    #NewUserForm,
#)
from app.utils.decorators import admin_required
from app.utils.email import send_email
from app.models import *
from app.common.BaseModel import db_session as session
from app.blueprints.page_manager.forms import *

page_manager = Blueprint('page_manager', __name__)


@page_manager.route('/page/setting')
@login_required
async def index():
    return await render_template('page_manager/page/index.html')

# Add Page
@page_manager.route('/page/setting/added', methods=['POST', 'GET'])
@login_required
async def added_page():
    """View added Page setting."""
    data = await Page.all()
    if data is None:
        return redirect(url_for('page_manager.add_page'))
    return await render_template(
        'page_manager/page/added_page.html', data=data)


@page_manager.route('/page/setting/add', methods=['POST', 'GET'])
@login_required
async def add_page():
    form = PageForm()
    if form.validate_on_submit():
        data = await Page.create(
            **dict(name = form.name.data,
            #seo_title = form.seo_title.data,
            #seo_description = form.seo_description.data,
            content = form.content.data
            ))
        flash("Settings Added Successfully.", "success")
        return redirect(url_for('page_manager.added_page'))
    return await render_template('page_manager/page/add_page.html', form=form)


# Edit Page
@page_manager.route('/page/<int:id>/edit', methods=['POST', 'GET'])
@login_required
async def edit_page(id):
    data = await Page.get_or_404(id, 'id')
    form = PageForm(obj=data)
    if form.validate_on_submit():
        data.name=form.name.data
        data.content=form.content.data
        session.add(data)
        await session.commit()

        flash("Link Html Added Successfully.", "success")
        return redirect(url_for('page_manager.added_page'))
    else:
        flash('ERROR! Page was not edited.', 'error')
    return render_template('page_manager/page/add_page.html', form=form)

@page_manager.route('/page/setting/<int:id>/_delete', methods=['GET', 'POST'])
@login_required
async def delete_page(id):
    """Delete the page added """
    data = await Page.get_or_404(id, 'id')
    await data.delete()
    flash('Successfully deleted ' , 'success')
    if data is None:
        return redirect(url_for('page_manager.add_page'))
    return redirect(url_for('page_manager.added_page'))


