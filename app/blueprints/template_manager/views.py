from aioflask import (
    Blueprint,
    abort,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)
from flask_login import current_user, login_required
from flask_ckeditor import upload_success

#from app.admin.forms import (
    #ChangeAccountTypeForm,
    #ChangeUserEmailForm,
    #InviteUserForm,
    #NewUserForm,
#)
from app.utils.decorators import admin_required
from app.utils.email import send_email
from app.models import *
from app.blueprints.template_manager.forms import *
from app.blueprints.template_manager.views import template_manager

template_manager = Blueprint('template_manager', __name__)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@template_manager.route('/template/setting')
@login_required
async def index():
    """Template manager page."""
        
    data = await TemplateSetting.all()
    form = TemplateChoiceForm()
    if form.validate_on_submit():
        TemplateChoice.create(
            **dict(template_name = form.template_name.data,
            choice = form.choice.data)
            )
        flash("Settings Added Successfully.", "success")
    return render_template('template_manager/index.html', data=data, form=form)


# Add Testimonial
@template_manager.route('/template/setting', methods=['POST', 'GET'])
@login_required
async def added_template_setting():
    """View added template setting."""
    data = await TemplateSetting.all()
    if data is None:
        return redirect(url_for('template_manager.add_template_setting'))
    return render_template(
        'template_manager/template_setting/added_template_setting.html', data=data)


@template_manager.route('/template/setting/add', methods=['POST', 'GET'])
@login_required
async def add_template_setting():
    form = TemplateSettingForm()
    if form.validate_on_submit():
        await TemplateSetting.create(**dict(
            template_name = form.template_name.data,
            category = form.category.data,
            choice = form.choice.data,
            image = images.save(request.files['image']))
            )
        flash("Settings Added Successfully.", "success")
        return redirect(url_for('template_manager.added_template_setting'))
    return render_template('template_manager/template_setting/add_template_setting.html', form=form)

@template_manager.route('/template/setting/<int:id>/_delete', methods=['GET', 'POST'])
@login_required
async def delete_template_setting(id):
    """Delete the template_setting added """
    data = await TemplateSetting.get_or_404(id, 'id')
    await data.delete()
    flash('Successfully deleted ' , 'success')
    if data is None:
        return redirect(url_for('template_manager.add_template_setting'))
    return redirect(url_for('template_manager.added_template_setting'))

@template_manager.route('/preview/<template_name>', methods=['GET', 'POST'])
@login_required
async def preview(template_name):
    """ Peview Templates Added """

    nav_menu = await NavMenu.all()
    slideshows = await SlideShowImage.all()
    hometext = await HomeText.first()
    call_to_action = await CallToAction.first()
    logo = await Logo.first()
    techno_img = await TechnologiesImage.all()
    text_techno = await TechnologiesText.first()
    footer_text = await FooterText.all()
    tracking_script = await TrackingScript.all()
    media_icons = await SocialMediaIcon.all()
    footer_image = await FooterImage.first()
    copyright_text = await CopyRight.first()
    background_image = await BackgroundImage.first()
    favicon_image = await FaviconImage.first()
    brand = await BrandName.first()
    seo = await Seo.first()
    services = await Service.all()
    about = await About.first()
    team = await Team.all()
    video = await Video.first()
    counts = await Counter.all()
    portfolio = await Portfolio.all()
    faq = await Faq.all()
    testimonial = await Testimonial.all()
    client = await Client.all()
    apple_touch_icon = await AppleTouchIcon.first()
    jumbotron_html = await JumbotronHtml.first()
    form_html = await FormHtml.first()
    blank_html = await FormHtml.all()
    album_html = await AlbumHtml.first()
    carousel_html = await CarouselHtml.first()
    header_script = await HeaderScript.all()
    footer_script = await FooterScript.all()
    header_html = await HeaderHtml.first()
    navbar_html = await NavbarHtml.first()
    footer_html = await FooterHtml.first()
    features_html = await FeaturesHtml.all()
    css = await Css.first()
    pricing_html = await PricingHtml.all()
    testimonials_html = await TestimonialsHtml.all()
    contact_html = await ContactHtml.first()
    pages = await Page.all()
    
    item = await TemplateSetting.get_or_404(template_name, 'template_name')
    return render_template(f"{ item.template_name }/index.html", footer_image=footer_image, icons=media_icons,
                           footer_text=footer_text, slideshows=slideshows,
                           home_title=hometext, logo=logo, techno_img=techno_img,
                           text_techno=text_techno, copyright_text=copyright_text,
                           background_image=background_image, call_to_action=call_to_action,
                           nav_menu=nav_menu, brand=brand, seo=seo,
                           favicon_image=favicon_image, tracking_script=tracking_script, services=services,
                           about=about, team=team, video=video, counts=counts, media_icons = media_icons,
                           portfolio=portfolio, faq=faq, testimonial=testimonial, client=client, apple_touch_icon=apple_touch_icon,
                           jumbotron_html = jumbotron_html, form_html = form_html, blank_html = blank_html,
                           album_html = album_html, carousel_html = carousel_html, header_script = header_script,
                           footer_script = footer_script, header_html = header_html, navbar_html = navbar_html,
                           footer_html = footer_html, css = css, features_html = features_html, pricing_html = pricing_html,
                           testimonials_html= testimonials_html, contact_html = contact_html, pages=pages)


@template_manager.route('/preview/Bare/<page_name>', methods=['GET', 'POST'])
async def page(page_name):
    """ Pages Added """


    landing_page = TemplateSetting.query.filter_by(choice=True).first_or_404()
    template_name = landing_page.template_name#.lower()
    
    nav_menu = NavMenu.query.all()
    slideshows = SlideShowImage.query.all()
    hometext = HomeText.query.first()
    call_to_action = CallToAction.query.first()
    logo = Logo.query.first()
    techno_img = TechnologiesImage.query.all()
    text_techno = TechnologiesText.query.first()
    footer_text = FooterText.query.all()
    tracking_script = TrackingScript.query.all()
    media_icons = SocialMediaIcon.query.all()
    footer_image = FooterImage.query.first()
    copyright_text = CopyRight.query.first()
    background_image = BackgroundImage.query.first()
    favicon_image = FaviconImage.query.first()
    brand = BrandName.query.first()
    seo = Seo.query.first()
    services = Service.query.all()
    about = About.query.first()
    team = Team.query.all()
    video = Video.query.first()
    counts = Counter.query.all()
    portfolio = Portfolio.query.all()
    faq = Faq.query.all()
    testimonial = Testimonial.query.all()
    client = Client.query.all()
    apple_touch_icon = AppleTouchIcon.query.first()
    jumbotron_html = JumbotronHtml.query.first()
    form_html = FormHtml.query.first()
    blank_html = FormHtml.query.all()
    album_html = AlbumHtml.query.first()
    carousel_html = CarouselHtml.query.first()
    header_script = HeaderScript.query.all()
    footer_script = FooterScript.query.all()
    header_html = HeaderHtml.query.first()
    navbar_html = NavbarHtml.query.first()
    footer_html = FooterHtml.query.first()
    features_html = FeaturesHtml.query.all()
    css = Css.query.first()
    pricing_html = PricingHtml.query.all()
    testimonials_html = TestimonialsHtml.query.all()
    contact_html = ContactHtml.query.first()
    page_content = Page.query.filter_by(name=page_name).first_or_404()
    pages = Page.query.all()
    
    item = TemplateSetting.query.filter_by(template_name=template_name).first_or_404()
    return render_template("Bare/inner-page.html", footer_image=footer_image, icons=media_icons,
                           footer_text=footer_text, slideshows=slideshows,
                           home_title=hometext, logo=logo, techno_img=techno_img,
                           text_techno=text_techno, copyright_text=copyright_text,
                           background_image=background_image, call_to_action=call_to_action,
                           nav_menu=nav_menu, brand=brand, seo=seo,
                           favicon_image=favicon_image, tracking_script=tracking_script, services=services,
                           about=about, team=team, video=video, counts=counts, media_icons = media_icons,
                           portfolio=portfolio, faq=faq, testimonial=testimonial, client=client, apple_touch_icon=apple_touch_icon,
                           jumbotron_html = jumbotron_html, form_html = form_html, blank_html = blank_html,
                           album_html = album_html, carousel_html = carousel_html, header_script = header_script,
                           footer_script = footer_script, header_html = header_html, navbar_html = navbar_html,
                           footer_html = footer_html, css = css, features_html = features_html, pricing_html = pricing_html,
                           testimonials_html= testimonials_html, contact_html = contact_html, page_name=page_name,
                           page_content = page_content, pages=pages)

@template_manager.route('/default/<int:id>/<template_name>', methods=['GET', 'POST'])
@login_required
async def add_default(id, template_name):
    """ async Default Templates Added """

    data = TemplateSetting.query.filter_by(choice=True).first_or_404()
    data.choice = False
    db.session.add(data)
    #db.session.commit()
    
    default = TemplateSetting.query.get_or_404(id)
    default.choice = True
    default.template_name = template_name
    db.session.add(default)
    db.session.commit()
    flash("Default Template Chosen Successfully.", "success")
    return redirect(url_for('main.index'))
    

