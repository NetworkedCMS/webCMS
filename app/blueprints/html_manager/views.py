import quart.flask_patch
from quart import (
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
from app.blueprints.html_manager.forms import *
from app.blueprints.html_manager.views import html_manager


html_manager = Blueprint('html_manager', __name__)


@html_manager.route('/html/setting')
async def index():
    return await render_template('html_manager/index.html')


# Add JumbotronHtml
@html_manager.route('/jumbotron_html/setting', methods=['POST', 'GET'])
@login_required
async def added_jumbotron_html():
    """View added Jumbotron HTML setting."""
    data = JumbotronHtml.query.first()
    if data is None:
        return redirect(url_for('admin.add_jumbotron_html'))
    return await render_template(
        'html_manager/jumbotron_html/added_jumbotron_html.html', data=data)


@html_manager.route('/jumbotron_html/setting/add', methods=['POST', 'GET'])
@login_required
async def add_jumbotron_html():
    form = JumbotronHtmlForm()
    if form.validate_on_submit():
        data = JumbotronHtml(
            html = form.html.data
            )
        db.session.add(data)
        db.session.commit()
        await flash("Settings Added Successfully.", "success")
        return redirect(url_for('admin.added_jumbotron_html'))
    return await render_template('html_manager/jumbotron_html/add_jumbotron_html.html', form=form)


# Edit JumbotronHtml
@html_manager.route('/jumbotron_html/<int:id>/edit', methods=['POST', 'GET'])
@login_required
async def edit_jumbotron_html(id):
    data = JumbotronHtml.query.filter_by(id=id).first()
    form = JumbotronHtmlForm(obj=data)
    if form.validate_on_submit():
        data.html=form.html.data
        db.session.add(data)
        db.session.commit()
        await flash("Jumbotron Html Added Successfully.", "success")
        return redirect(url_for('admin.added_jumbotron_html'))
    else:
        await flash('ERROR! Jumbotron Html was not edited.', 'error')
    return await render_template('html_manager/jumbotron_html/add_jumbotron_html.html', form=form)

@html_manager.route('/jumbotron_html/setting/<int:id>/_delete', methods=['GET', 'POST'])
@login_required
async def delete_jumbotron_html(id):
    """Delete the jumbotron html added """
    data = JumbotronHtml.query.filter_by(id=id).first()
    db.session.commit()
    db.session.delete(data)
    await flash('Successfully deleted ' , 'success')
    if data is None:
        return redirect(url_for('admin.add_jumbotron_html'))
    return redirect(url_for('admin.added_jumbotron_html'))


# Add HeaderHtml
@html_manager.route('/header_html/setting', methods=['POST', 'GET'])
@login_required
async def added_header_html():
    """View added Header HTML setting."""
    data = HeaderHtml.query.first()
    if data is None:
        return redirect(url_for('admin.add_header_html'))
    return await render_template(
        'html_manager/header_html/added_header_html.html', data=data)


@html_manager.route('/header_html/setting/add', methods=['POST', 'GET'])
@login_required
async def add_header_html():
    form = HeaderHtmlForm()
    if form.validate_on_submit():
        data = HeaderHtml(
            html = form.html.data
            )
        db.session.add(data)
        db.session.commit()
        await flash("Settings Added Successfully.", "success")
        return redirect(url_for('admin.added_header_html'))
    return await render_template('html_manager/header_html/add_header_html.html', form=form)


# Edit HeaderHtml
@html_manager.route('/header_html/<int:id>/edit', methods=['POST', 'GET'])
@login_required
async def edit_header_html(id):
    data = HeaderHtml.query.filter_by(id=id).first()
    form = HeaderHtmlForm(obj=data)
    if form.validate_on_submit():
        data.html=form.html.data
        db.session.add(data)
        db.session.commit()
        await flash("Header Html Added Successfully.", "success")
        return redirect(url_for('admin.added_header_html'))
    else:
        await flash('ERROR! Header Html was not edited.', 'error')
    return await render_template('html_manager/header_html/add_header_html.html', form=form)

@html_manager.route('/header_html/setting/<int:id>/_delete', methods=['GET', 'POST'])
@login_required
async def delete_header_html(id):
    """Delete the header html added """
    data = HeaderHtml.query.filter_by(id=id).first()
    db.session.commit()
    db.session.delete(data)
    await flash('Successfully deleted ' , 'success')
    if data is None:
        return redirect(url_for('admin.add_header_html'))
    return redirect(url_for('admin.added_header_html'))

# Add HeaderScript
@html_manager.route('/header_script/setting', methods=['POST', 'GET'])
@login_required
async def added_header_script():
    """View added Header HTML setting."""
    data = HeaderScript.query.all()
    if data is None:
        return redirect(url_for('admin.add_header_script'))
    return await render_template(
        'html_manager/header_script/added_header_script.html', data=data)


@html_manager.route('/header_script/setting/add', methods=['POST', 'GET'])
@login_required
async def add_header_script():
    form = HeaderScriptForm()
    if form.validate_on_submit():
        data = HeaderScript(
            js = form.js.data
            )
        db.session.add(data)
        db.session.commit()
        await flash("Settings Added Successfully.", "success")
        return redirect(url_for('admin.added_header_script'))
    return await render_template('html_manager/header_script/add_header_script.html', form=form)


# Edit HeaderScript
@html_manager.route('/header_script/<int:id>/edit', methods=['POST', 'GET'])
@login_required
async def edit_header_script(id):
    data = HeaderScript.query.filter_by(id=id).first()
    form = HeaderScriptForm(obj=data)
    if form.validate_on_submit():
        data.js=form.js.data
        db.session.add(data)
        db.session.commit()
        await flash("Header Script Added Successfully.", "success")
        return redirect(url_for('admin.added_header_script'))
    else:
        await flash('ERROR! Header Script was not edited.', 'error')
    return await render_template('html_manager/header_script/add_header_script.html', form=form)

@html_manager.route('/header_script/setting/<int:id>/_delete', methods=['GET', 'POST'])
@login_required
async def delete_header_script(id):
    """Delete the header html added """
    data = HeaderScript.query.filter_by(id=id).first()
    db.session.commit()
    db.session.delete(data)
    await flash('Successfully deleted ' , 'success')
    if data is None:
        return redirect(url_for('admin.add_header_script'))
    return redirect(url_for('admin.added_header_script'))

# Add NavbarHtml
@html_manager.route('/navbar_html/setting', methods=['POST', 'GET'])
@login_required
async def added_navbar_html():
    """View added Navbar HTML setting."""
    data = NavbarHtml.query.first()
    if data is None:
        return redirect(url_for('admin.add_navbar_html'))
    return await render_template(
        'html_manager/navbar_html/added_navbar_html.html', data=data)


@html_manager.route('/navbar_html/setting/add', methods=['POST', 'GET'])
@login_required
async def add_navbar_html():
    form = NavbarHtmlForm()
    if form.validate_on_submit():
        data = NavbarHtml(
            html = form.html.data
            )
        db.session.add(data)
        db.session.commit()
        await flash("Settings Added Successfully.", "success")
        return redirect(url_for('admin.added_navbar_html'))
    return await render_template('html_manager/navbar_html/add_navbar_html.html', form=form)


# Edit NavbarHtml
@html_manager.route('/navbar_html/<int:id>/edit', methods=['POST', 'GET'])
@login_required
async def edit_navbar_html(id):
    data = NavbarHtml.query.filter_by(id=id).first()
    form = NavbarHtmlForm(obj=data)
    if form.validate_on_submit():
        data.html=form.html.data
        db.session.add(data)
        db.session.commit()
        await flash("Navbar Html Added Successfully.", "success")
        return redirect(url_for('admin.added_navbar_html'))
    else:
        await flash('ERROR! Navbar Html was not edited.', 'error')
    return await render_template('html_manager/navbar_html/add_navbar_html.html', form=form)

@html_manager.route('/navbar_html/setting/<int:id>/_delete', methods=['GET', 'POST'])
@login_required
async def delete_navbar_html(id):
    """Delete the navbar html added """
    data = NavbarHtml.query.filter_by(id=id).first()
    db.session.commit()
    db.session.delete(data)
    await flash('Successfully deleted ' , 'success')
    if data is None:
        return redirect(url_for('admin.add_navbar_html'))
    return redirect(url_for('admin.added_navbar_html'))

# Add FooterHtml
@html_manager.route('/footer_html/setting', methods=['POST', 'GET'])
@login_required
async def added_footer_html():
    """View added Footer HTML setting."""
    data = FooterHtml.query.first()
    if data is None:
        return redirect(url_for('admin.add_footer_html'))
    return await render_template(
        'html_manager/footer_html/added_footer_html.html', data=data)


@html_manager.route('/footer_html/setting/add', methods=['POST', 'GET'])
@login_required
async def add_footer_html():
    form = FooterHtmlForm()
    if form.validate_on_submit():
        data = FooterHtml(
            html = form.html.data
            )
        db.session.add(data)
        db.session.commit()
        await flash("Settings Added Successfully.", "success")
        return redirect(url_for('admin.added_footer_html'))
    return await render_template('html_manager/footer_html/add_footer_html.html', form=form)


# Edit FooterHtml
@html_manager.route('/footer_html/<int:id>/edit', methods=['POST', 'GET'])
@login_required
async def edit_footer_html(id):
    data = FooterHtml.query.filter_by(id=id).first()
    form = FooterHtmlForm(obj=data)
    if form.validate_on_submit():
        data.html=form.html.data
        db.session.add(data)
        db.session.commit()
        await flash("Footer Html Added Successfully.", "success")
        return redirect(url_for('admin.added_footer_html'))
    else:
        await flash('ERROR! Footer Html was not edited.', 'error')
    return await render_template('html_manager/footer_html/add_footer_html.html', form=form)

@html_manager.route('/footer_html/setting/<int:id>/_delete', methods=['GET', 'POST'])
@login_required
async def delete_footer_html(id):
    """Delete the footer html added """
    data = FooterHtml.query.filter_by(id=id).first()
    db.session.commit()
    db.session.delete(data)
    await flash('Successfully deleted ' , 'success')
    if data is None:
        return redirect(url_for('admin.add_footer_html'))
    return redirect(url_for('admin.added_footer_html'))

# Add FooterScript
@html_manager.route('/footer_script/setting', methods=['POST', 'GET'])
@login_required
async def added_footer_script():
    """View added Footer HTML setting."""
    data = FooterScript.query.all()
    if data is None:
        return redirect(url_for('admin.add_footer_script'))
    return await render_template(
        'html_manager/footer_script/added_footer_script.html', data=data)


@html_manager.route('/footer_script/setting/add', methods=['POST', 'GET'])
@login_required
async def add_footer_script():
    form = FooterScriptForm()
    if form.validate_on_submit():
        data = FooterScript(
            js = form.js.data
            )
        db.session.add(data)
        db.session.commit()
        await flash("Settings Added Successfully.", "success")
        return redirect(url_for('admin.added_footer_script'))
    return await render_template('html_manager/footer_script/add_footer_script.html', form=form)


# Edit FooterScript
@html_manager.route('/footer_script/<int:id>/edit', methods=['POST', 'GET'])
@login_required
async def edit_footer_script(id):
    data = FooterScript.query.filter_by(id=id).first()
    form = FooterScriptForm(obj=data)
    if form.validate_on_submit():
        data.js=form.js.data
        db.session.add(data)
        db.session.commit()
        await flash("Footer Script Added Successfully.", "success")
        return redirect(url_for('admin.added_footer_script'))
    else:
        await flash('ERROR! Footer Script was not edited.', 'error')
    return await render_template('html_manager/footer_script/add_footer_script.html', form=form)

@html_manager.route('/footer_script/setting/<int:id>/_delete', methods=['GET', 'POST'])
@login_required
async def delete_footer_script(id):
    """Delete the footer html added """
    data = FooterScript.query.filter_by(id=id).first()
    db.session.commit()
    db.session.delete(data)
    await flash('Successfully deleted ' , 'success')
    if data is None:
        return redirect(url_for('admin.add_footer_script'))
    return redirect(url_for('admin.added_footer_script'))

# Add CarouselHtml
@html_manager.route('/carousel_html/setting', methods=['POST', 'GET'])
@login_required
async def added_carousel_html():
    """View added Carousel HTML setting."""
    data = CarouselHtml.query.first()
    if data is None:
        return redirect(url_for('admin.add_carousel_html'))
    return await render_template(
        'html_manager/carousel_html/added_carousel_html.html', data=data)


@html_manager.route('/carousel_html/setting/add', methods=['POST', 'GET'])
@login_required
async def add_carousel_html():
    form = CarouselHtmlForm()
    if form.validate_on_submit():
        data = CarouselHtml(
            html = form.html.data
            )
        db.session.add(data)
        db.session.commit()
        await flash("Settings Added Successfully.", "success")
        return redirect(url_for('admin.added_carousel_html'))
    return await render_template('html_manager/carousel_html/add_carousel_html.html', form=form)


# Edit CarouselHtml
@html_manager.route('/carousel_html/<int:id>/edit', methods=['POST', 'GET'])
@login_required
async def edit_carousel_html(id):
    data = CarouselHtml.query.filter_by(id=id).first()
    form = CarouselHtmlForm(obj=data)
    if form.validate_on_submit():
        data.html=form.html.data
        db.session.add(data)
        db.session.commit()
        await flash("Carousel Html Added Successfully.", "success")
        return redirect(url_for('admin.added_carousel_html'))
    else:
        await flash('ERROR! Carousel Html was not edited.', 'error')
    return await render_template('html_manager/carousel_html/add_carousel_html.html', form=form)

@html_manager.route('/carousel_html/setting/<int:id>/_delete', methods=['GET', 'POST'])
@login_required
async def delete_carousel_html(id):
    """Delete the carousel html added """
    data = CarouselHtml.query.filter_by(id=id).first()
    db.session.commit()
    db.session.delete(data)
    await flash('Successfully deleted ' , 'success')
    if data is None:
        return redirect(url_for('admin.add_carousel_html'))
    return redirect(url_for('admin.added_carousel_html'))

# Add AlbumHtml
@html_manager.route('/album_html/setting', methods=['POST', 'GET'])
@login_required
async def added_album_html():
    """View added Album HTML setting."""
    data = AlbumHtml.query.first()
    if data is None:
        return redirect(url_for('admin.add_album_html'))
    return await render_template(
        'html_manager/album_html/added_album_html.html', data=data)


@html_manager.route('/album_html/setting/add', methods=['POST', 'GET'])
@login_required
async def add_album_html():
    form = AlbumHtmlForm()
    if form.validate_on_submit():
        data = AlbumHtml(
            html = form.html.data
            )
        db.session.add(data)
        db.session.commit()
        await flash("Settings Added Successfully.", "success")
        return redirect(url_for('admin.added_album_html'))
    return await render_template('html_manager/album_html/add_album_html.html', form=form)


# Edit AlbumHtml
@html_manager.route('/album_html/<int:id>/edit', methods=['POST', 'GET'])
@login_required
async def edit_album_html(id):
    data = AlbumHtml.query.filter_by(id=id).first()
    form = AlbumHtmlForm(obj=data)
    if form.validate_on_submit():
        data.html=form.html.data
        db.session.add(data)
        db.session.commit()
        await flash("Album Html Added Successfully.", "success")
        return redirect(url_for('admin.added_album_html'))
    else:
        await flash('ERROR! Album Html was not edited.', 'error')
    return await render_template('html_manager/album_html/add_album_html.html', form=form)

@html_manager.route('/album_html/setting/<int:id>/_delete', methods=['GET', 'POST'])
@login_required
async def delete_album_html(id):
    """Delete the album html added """
    data = AlbumHtml.query.filter_by(id=id).first()
    db.session.commit()
    db.session.delete(data)
    await flash('Successfully deleted ' , 'success')
    if data is None:
        return redirect(url_for('admin.add_album_html'))
    return redirect(url_for('admin.added_album_html'))

# Add BlankHtml
@html_manager.route('/blank_html/setting', methods=['POST', 'GET'])
@login_required
async def added_blank_html():
    """View added Blank HTML setting."""
    data = BlankHtml.query.first()
    if data is None:
        return redirect(url_for('admin.add_blank_html'))
    return await render_template(
        'html_manager/blank_html/added_blank_html.html', data=data)


@html_manager.route('/blank_html/setting/add', methods=['POST', 'GET'])
@login_required
async def add_blank_html():
    form = BlankHtmlForm()
    if form.validate_on_submit():
        data = BlankHtml(
            html = form.html.data
            )
        db.session.add(data)
        db.session.commit()
        await flash("Settings Added Successfully.", "success")
        return redirect(url_for('admin.added_blank_html'))
    return await render_template('html_manager/blank_html/add_blank_html.html', form=form)


# Edit BlankHtml
@html_manager.route('/blank_html/<int:id>/edit', methods=['POST', 'GET'])
@login_required
async def edit_blank_html(id):
    data = BlankHtml.query.filter_by(id=id).first()
    form = BlankHtmlForm(obj=data)
    if form.validate_on_submit():
        data.html=form.html.data
        db.session.add(data)
        db.session.commit()
        await flash("Blank Html Added Successfully.", "success")
        return redirect(url_for('admin.added_blank_html'))
    else:
        await flash('ERROR! Blank Html was not edited.', 'error')
    return await render_template('html_manager/blank_html/add_blank_html.html', form=form)

@html_manager.route('/blank_html/setting/<int:id>/_delete', methods=['GET', 'POST'])
@login_required
async def delete_blank_html(id):
    """Delete the blank html added """
    data = BlankHtml.query.filter_by(id=id).first()
    db.session.commit()
    db.session.delete(data)
    await flash('Successfully deleted ' , 'success')
    if data is None:
        return redirect(url_for('admin.add_blank_html'))
    return redirect(url_for('admin.added_blank_html'))


# Add FormHtml
@html_manager.route('/form_html/setting', methods=['POST', 'GET'])
@login_required
async def added_form_html():
    """View added Form HTML setting."""
    data = FormHtml.query.first()
    if data is None:
        return redirect(url_for('admin.add_form_html'))
    return await render_template(
        'html_manager/form_html/added_form_html.html', data=data)


@html_manager.route('/form_html/setting/add', methods=['POST', 'GET'])
@login_required
async def add_form_html():
    form = FormHtmlForm()
    if form.validate_on_submit():
        data = FormHtml(
            html = form.html.data,
            form_name = form.form_name.data
            )
        db.session.add(data)
        db.session.commit()
        await flash("Settings Added Successfully.", "success")
        return redirect(url_for('admin.added_form_html'))
    return await render_template('html_manager/form_html/add_form_html.html', form=form)


# Edit FormHtml
@html_manager.route('/form_html/<int:id>/edit', methods=['POST', 'GET'])
@login_required
async def edit_form_html(id):
    data = FormHtml.query.filter_by(id=id).first()
    form = FormHtmlForm(obj=data)
    if form.validate_on_submit():
        data.html=form.html.data
        data.form_name=form.form_name.data
        db.session.add(data)
        db.session.commit()
        await flash("Form Html Added Successfully.", "success")
        return redirect(url_for('admin.added_form_html'))
    else:
        await flash('ERROR! Form Html was not edited.', 'error')
    return await render_template('html_manager/form_html/add_form_html.html', form=form)

@html_manager.route('/form_html/setting/<int:id>/_delete', methods=['GET', 'POST'])
@login_required
async def delete_form_html(id):
    """Delete the form html added """
    data = FormHtml.query.filter_by(id=id).first()
    db.session.commit()
    db.session.delete(data)
    await flash('Successfully deleted ' , 'success')
    if data is None:
        return redirect(url_for('admin.add_form_html'))
    return redirect(url_for('admin.added_form_html'))

# Add FeaturesHtml
@html_manager.route('/features_html/setting', methods=['POST', 'GET'])
@login_required
async def added_features_html():
    """View added Features HTML setting."""
    data = FeaturesHtml.query.all()
    if data is None:
        return redirect(url_for('admin.add_features_html'))
    return await render_template(
        'html_manager/features_html/added_features_html.html', data=data)


@html_manager.route('/features_html/setting/add', methods=['POST', 'GET'])
@login_required
async def add_features_html():
    form = FeaturesHtmlForm()
    if form.validate_on_submit():
        data = FeaturesHtml(
            html = form.html.data
            )
        db.session.add(data)
        db.session.commit()
        await flash("Settings Added Successfully.", "success")
        return redirect(url_for('admin.added_features_html'))
    return await render_template('html_manager/features_html/add_features_html.html', form=form)


# Edit FeaturesHtml
@html_manager.route('/features_html/<int:id>/edit', methods=['POST', 'GET'])
@login_required
async def edit_features_html(id):
    data = FeaturesHtml.query.filter_by(id=id).first()
    form = FeaturesHtmlForm(obj=data)
    if form.validate_on_submit():
        data.html=form.html.data
        db.session.add(data)
        db.session.commit()
        await flash("Features Html Added Successfully.", "success")
        return redirect(url_for('admin.added_features_html'))
    else:
        await flash('ERROR! Features Html was not edited.', 'error')
    return await render_template('html_manager/features_html/add_features_html.html', form=form)

@html_manager.route('/features_html/setting/<int:id>/_delete', methods=['GET', 'POST'])
@login_required
async def delete_features_html(id):
    """Delete the features html added """
    data = FeaturesHtml.query.filter_by(id=id).first()
    db.session.commit()
    db.session.delete(data)
    await flash('Successfully deleted ' , 'success')
    if data is None:
        return redirect(url_for('admin.add_features_html'))
    return redirect(url_for('admin.added_features_html'))

# Add PricingHtml
@html_manager.route('/pricing_html/setting', methods=['POST', 'GET'])
@login_required
async def added_pricing_html():
    """View added Pricing HTML setting."""
    data = PricingHtml.query.all()
    if data is None:
        return redirect(url_for('admin.add_pricing_html'))
    return await render_template(
        'html_manager/pricing_html/added_pricing_html.html', data=data)


@html_manager.route('/pricing_html/setting/add', methods=['POST', 'GET'])
@login_required
async def add_pricing_html():
    form = PricingHtmlForm()
    if form.validate_on_submit():
        data = PricingHtml(
            html = form.html.data
            )
        db.session.add(data)
        db.session.commit()
        await flash("Settings Added Successfully.", "success")
        return redirect(url_for('admin.added_pricing_html'))
    return await render_template('html_manager/pricing_html/add_pricing_html.html', form=form)


# Edit PricingHtml
@html_manager.route('/pricing_html/<int:id>/edit', methods=['POST', 'GET'])
@login_required
async def edit_pricing_html(id):
    data = PricingHtml.query.filter_by(id=id).first()
    form = PricingHtmlForm(obj=data)
    if form.validate_on_submit():
        data.html=form.html.data
        db.session.add(data)
        db.session.commit()
        await flash("Pricing Html Added Successfully.", "success")
        return redirect(url_for('admin.added_pricing_html'))
    else:
        await flash('ERROR! Pricing Html was not edited.', 'error')
    return await render_template('html_manager/pricing_html/add_pricing_html.html', form=form)

@html_manager.route('/pricing_html/setting/<int:id>/_delete', methods=['GET', 'POST'])
@login_required
async def delete_pricing_html(id):
    """Delete the pricing html added """
    data = PricingHtml.query.filter_by(id=id).first()
    db.session.commit()
    db.session.delete(data)
    await flash('Successfully deleted ' , 'success')
    if data is None:
        return redirect(url_for('admin.add_pricing_html'))
    return redirect(url_for('admin.added_pricing_html'))

# Add TestimonialsHtml
@html_manager.route('/testimonials_html/setting', methods=['POST', 'GET'])
@login_required
async def added_testimonials_html():
    """View added Testimonials HTML setting."""
    data = TestimonialsHtml.query.all()
    if data is None:
        return redirect(url_for('admin.add_testimonials_html'))
    return await render_template(
        'html_manager/testimonials_html/added_testimonials_html.html', data=data)


@html_manager.route('/testimonials_html/setting/add', methods=['POST', 'GET'])
@login_required
async def add_testimonials_html():
    form = TestimonialsHtmlForm()
    if form.validate_on_submit():
        data = TestimonialsHtml(
            html = form.html.data
            )
        db.session.add(data)
        db.session.commit()
        await flash("Settings Added Successfully.", "success")
        return redirect(url_for('admin.added_testimonials_html'))
    return await render_template('html_manager/testimonials_html/add_testimonials_html.html', form=form)


# Edit TestimonialsHtml
@html_manager.route('/testimonials_html/<int:id>/edit', methods=['POST', 'GET'])
@login_required
async def edit_testimonials_html(id):
    data = TestimonialsHtml.query.filter_by(id=id).first()
    form = TestimonialsHtmlForm(obj=data)
    if form.validate_on_submit():
        data.html=form.html.data
        db.session.add(data)
        db.session.commit()
        await flash("Testimonials Html Added Successfully.", "success")
        return redirect(url_for('admin.added_testimonials_html'))
    else:
        await flash('ERROR! Testimonials Html was not edited.', 'error')
    return await render_template('html_manager/testimonials_html/add_testimonials_html.html', form=form)

@html_manager.route('/testimonials_html/setting/<int:id>/_delete', methods=['GET', 'POST'])
@login_required
async def delete_testimonials_html(id):
    """Delete the testimonials html added """
    data = TestimonialsHtml.query.filter_by(id=id).first()
    db.session.commit()
    db.session.delete(data)
    await flash('Successfully deleted ' , 'success')
    if data is None:
        return redirect(url_for('admin.add_testimonials_html'))
    return redirect(url_for('admin.added_testimonials_html'))

# Add ContactHtml
@html_manager.route('/contact_html/setting', methods=['POST', 'GET'])
@login_required
async def added_contact_html():
    """View added Contact HTML setting."""
    data = ContactHtml.query.first()
    if data is None:
        return redirect(url_for('admin.add_contact_html'))
    return await render_template(
        'html_manager/contact_html/added_contact_html.html', data=data)


@html_manager.route('/contact_html/setting/add', methods=['POST', 'GET'])
@login_required
async def add_contact_html():
    form = ContactHtmlForm()
    if form.validate_on_submit():
        data = ContactHtml(
            html = form.html.data
            )
        db.session.add(data)
        db.session.commit()
        await flash("Settings Added Successfully.", "success")
        return redirect(url_for('admin.added_contact_html'))
    return await render_template('html_manager/contact_html/add_contact_html.html', form=form)


# Edit ContactHtml
@html_manager.route('/contact_html/<int:id>/edit', methods=['POST', 'GET'])
@login_required
async def edit_contact_html(id):
    data = ContactHtml.query.filter_by(id=id).first()
    form = ContactHtmlForm(obj=data)
    if form.validate_on_submit():
        data.html=form.html.data
        db.session.add(data)
        db.session.commit()
        await flash("Contact Html Added Successfully.", "success")
        return redirect(url_for('admin.added_contact_html'))
    else:
        await flash('ERROR! Contact Html was not edited.', 'error')
    return await render_template('html_manager/contact_html/add_contact_html.html', form=form)

@html_manager.route('/contact_html/setting/<int:id>/_delete', methods=['GET', 'POST'])
@login_required
async def delete_contact_html(id):
    """Delete the contact html added """
    data = ContactHtml.query.filter_by(id=id).first()
    db.session.commit()
    db.session.delete(data)
    await flash('Successfully deleted ' , 'success')
    if data is None:
        return redirect(url_for('admin.add_contact_html'))
    return redirect(url_for('admin.added_contact_html'))


# Add MetatagsHtml
@html_manager.route('/metatags_html/setting', methods=['POST', 'GET'])
@login_required
async def added_metatags_html():
    """View added Metatags HTML setting."""
    data = MetatagsHtml.query.all()
    if data is None:
        return redirect(url_for('admin.add_metatags_html'))
    return await render_template(
        'html_manager/metatags_html/added_metatags_html.html', data=data)


@html_manager.route('/metatags_html/setting/add', methods=['POST', 'GET'])
@login_required
async def add_metatags_html():
    form = MetatagsHtmlForm()
    if form.validate_on_submit():
        data = MetatagsHtml(
            html = form.html.data
            )
        db.session.add(data)
        db.session.commit()
        await flash("Settings Added Successfully.", "success")
        return redirect(url_for('admin.added_metatags_html'))
    return await render_template('html_manager/metatags_html/add_metatags_html.html', form=form)


# Edit MetatagsHtml
@html_manager.route('/metatags_html/<int:id>/edit', methods=['POST', 'GET'])
@login_required
async def edit_metatags_html(id):
    data = MetatagsHtml.query.filter_by(id=id).first()
    form = MetatagsHtmlForm(obj=data)
    if form.validate_on_submit():
        data.html=form.html.data
        db.session.add(data)
        db.session.commit()
        await flash("Metatags Html Added Successfully.", "success")
        return redirect(url_for('admin.added_metatags_html'))
    else:
        await flash('ERROR! Metatags Html was not edited.', 'error')
    return await render_template('html_manager/metatags_html/add_metatags_html.html', form=form)

@html_manager.route('/metatags_html/setting/<int:id>/_delete', methods=['GET', 'POST'])
@login_required
async def delete_metatags_html(id):
    """Delete the metatags html added """
    data = MetatagsHtml.query.filter_by(id=id).first()
    db.session.commit()
    db.session.delete(data)
    await flash('Successfully deleted ' , 'success')
    if data is None:
        return redirect(url_for('admin.add_metatags_html'))
    return redirect(url_for('admin.added_metatags_html'))

# Add TitleHtml
@html_manager.route('/title_html/setting', methods=['POST', 'GET'])
@login_required
async def added_title_html():
    """View added Title HTML setting."""
    data = TitleHtml.query.first()
    if data is None:
        return redirect(url_for('admin.add_title_html'))
    return await render_template(
        'html_manager/title_html/added_title_html.html', data=data)


@html_manager.route('/title_html/setting/add', methods=['POST', 'GET'])
@login_required
async def add_title_html():
    form = TitleHtmlForm()
    if form.validate_on_submit():
        data = TitleHtml(
            html = form.html.data
            )
        db.session.add(data)
        db.session.commit()
        await flash("Settings Added Successfully.", "success")
        return redirect(url_for('admin.added_title_html'))
    return await render_template('html_manager/title_html/add_title_html.html', form=form)


# Edit TitleHtml
@html_manager.route('/title_html/<int:id>/edit', methods=['POST', 'GET'])
@login_required
async def edit_title_html(id):
    data = TitleHtml.query.filter_by(id=id).first()
    form = TitleHtmlForm(obj=data)
    if form.validate_on_submit():
        data.html=form.html.data
        db.session.add(data)
        db.session.commit()
        await flash("Title Html Added Successfully.", "success")
        return redirect(url_for('admin.added_title_html'))
    else:
        await flash('ERROR! Title Html was not edited.', 'error')
    return await render_template('html_manager/title_html/add_title_html.html', form=form)

@html_manager.route('/title_html/setting/<int:id>/_delete', methods=['GET', 'POST'])
@login_required
async def delete_title_html(id):
    """Delete the title html added """
    data = TitleHtml.query.filter_by(id=id).first()
    db.session.commit()
    db.session.delete(data)
    await flash('Successfully deleted ' , 'success')
    if data is None:
        return redirect(url_for('admin.add_title_html'))
    return redirect(url_for('admin.added_title_html'))

# Add LinkHtml
@html_manager.route('/link_html/setting', methods=['POST', 'GET'])
@login_required
async def added_link_html():
    """View added Link HTML setting."""
    data = LinkHtml.query.all()
    if data is None:
        return redirect(url_for('admin.add_link_html'))
    return await render_template(
        'html_manager/link_html/added_link_html.html', data=data)


@html_manager.route('/link_html/setting/add', methods=['POST', 'GET'])
@login_required
async def add_link_html():
    form = LinkHtmlForm()
    if form.validate_on_submit():
        data = LinkHtml(
            html = form.html.data
            )
        db.session.add(data)
        db.session.commit()
        await flash("Settings Added Successfully.", "success")
        return redirect(url_for('admin.added_link_html'))
    return await render_template('html_manager/link_html/add_link_html.html', form=form)


# Edit LinkHtml
@html_manager.route('/link_html/<int:id>/edit', methods=['POST', 'GET'])
@login_required
async def edit_link_html(id):
    data = LinkHtml.query.filter_by(id=id).first()
    form = LinkHtmlForm(obj=data)
    if form.validate_on_submit():
        data.html=form.html.data
        db.session.add(data)
        db.session.commit()
        await flash("Link Html Added Successfully.", "success")
        return redirect(url_for('admin.added_link_html'))
    else:
        await flash('ERROR! Link Html was not edited.', 'error')
    return await render_template('html_manager/link_html/add_link_html.html', form=form)

@html_manager.route('/link_html/setting/<int:id>/_delete', methods=['GET', 'POST'])
@login_required
async def delete_link_html(id):
    """Delete the link html added """
    data = LinkHtml.query.filter_by(id=id).first()
    db.session.commit()
    db.session.delete(data)
    await flash('Successfully deleted ' , 'success')
    if data is None:
        return redirect(url_for('admin.add_link_html'))
    return redirect(url_for('admin.added_link_html'))

