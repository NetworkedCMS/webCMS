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
from app.blueprints.template_manager.forms import *
from app.blueprints.template_manager.views import template_manager

template_manager = Blueprint('template_manager', __name__)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@template_manager.route('/template/setting')
@login_required
def index():
    """Template manager page."""
        
    data = TemplateSetting.query.all()
    form = TemplateChoiceForm()
    if form.validate_on_submit():
        choice = TemplateChoice(
            template_name = form.template_name.data,
            choice = form.choice.data
            )
        db.session.add(choice)
        db.session.commit()
        flash("Settings Added Successfully.", "success")
    return render_template('template_manager/index.html', data=data, form=form)


# Add Testimonial
@template_manager.route('/template/setting', methods=['POST', 'GET'])
@login_required
def added_template_setting():
    """View added template setting."""
    data = TemplateSetting.query.all()
    if data is None:
        return redirect(url_for('template_manager.add_template_setting'))
    return render_template(
        'template_manager/template_setting/added_template_setting.html', data=data)


@template_manager.route('/template/setting/add', methods=['POST', 'GET'])
@login_required
def add_template_setting():
    form = TemplateSettingForm()
    if form.validate_on_submit():
        data = TemplateSetting(
            template_name = form.template_name.data,
            category = form.category.data,
            choice = form.choice.data,
            image = images.save(request.files['image'])
            )
        db.session.add(data)
        db.session.commit()
        flash("Settings Added Successfully.", "success")
        return redirect(url_for('template_manager.added_template_setting'))
    return render_template('template_manager/template_setting/add_template_setting.html', form=form)

@template_manager.route('/template/setting/<int:id>/_delete', methods=['GET', 'POST'])
@login_required
def delete_template_setting(id):
    """Delete the template_setting added """
    data = TemplateSetting.query.filter_by(id=id).first()
    db.session.commit()
    db.session.delete(data)
    flash('Successfully deleted ' , 'success')
    if data is None:
        return redirect(url_for('template_manager.add_template_setting'))
    return redirect(url_for('template_manager.added_template_setting'))

@template_manager.route('/preview/<template_name>', methods=['GET', 'POST'])
@login_required
def preview(template_name):
    """ Peview Templates Added """

    nav_menu = NavMenu.query.all()
    slideshows = SlideShowImage.query.all()
    hometext = HomeText.query.first()
    call_to_action = CallToAction.query.all()
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
    #page_content = Page.query.filter_by(name=page_name).first_or_404()
    pages = Page.query.all()
    headline = Headline.query.all()
    process_title = ProcessTitle.query.first()
    client_title = ClientTitle.query.first()
    process = Process.query.all()
    
    item = TemplateSetting.query.filter_by(template_name=template_name).first_or_404()
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
                           testimonials_html= testimonials_html, contact_html = contact_html, pages=pages, headline=headline,
                           process_title=process_title, process=process, client_title=client_title)
                        
    
    if item == 'Presento':
        return render_template("Presento/index.html", footer_image=footer_image, icons=media_icons,
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
    elif item == 'OnePage':
        return render_template("OnePage/index.html", footer_image=footer_image, icons=media_icons,
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

    else:
        return redirect(url_for('template_manager.index'))

@template_manager.route('/preview/Bare/<page_name>', methods=['GET', 'POST'])
def page(page_name):
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
    headline = Headline.query.all()
    
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
                           page_content = page_content, pages=pages, headline=headline)

@template_manager.route('/default/<int:id>/<template_name>', methods=['GET', 'POST'])
@login_required
def add_default(id, template_name):
    """ Default Templates Added """

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
    

