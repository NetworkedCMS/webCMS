from flask import (
    Blueprint,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)

from flask_login import (
    current_user,
    login_required,
    login_user,
    logout_user,
)

from app.models import *
from .forms import UploadForm
from flask_uploads import configure_uploads, IMAGES, UploadSet

main = Blueprint('main', __name__)

images = UploadSet('images', IMAGES)
#configure_uploads(main, images)


@main.route("/", methods=["GET", "POST"])
def index():
    """Home page for the website"""

    landing_page = TemplateSetting.query.filter_by(choice=True).first_or_404()
    landing_page_name = landing_page.template_name#.lower()
    
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
    
    return render_template(f"{ landing_page_name }/index.html", footer_image=footer_image, icons=media_icons,
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
                           testimonials_html= testimonials_html, contact_html = contact_html)


@main.route('/<page_name>', methods=['GET', 'POST'])
@login_required
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
    
    item = TemplateSetting.query.filter_by(template_name=template_name).first_or_404()
    form = ContactForm()
    if form.validate_on_submit():
        data = Contact(
            name = form.name.data,
            email = form.email.data,
            text = form.text.data
        )
        db.session.add(data)
        db.session.commit()
        flash("Message sent.", "success")
        
    return render_template(f"{ item.template_name }/inner-page.html", footer_image=footer_image, icons=media_icons,
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


""" @main.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST' and 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        rec = Photo(filename=filename, user=g.user.id)
        rec.store()
        flash("Photo saved.")
        return redirect(url_for('show', id=rec.id))
    return render_template('main/upload.html')

@main.route('/photo/<id>')
def show(id):
    photo = Photo.load(id)
    if photo is None:
        abort(404)
    url = photos.url(photo.filename)
    return render_template('show.html', url=url, photo=photo) """

@main.route('/upload', methods=['GET', 'POST'])
@login_required
def upload():
    form = UploadForm()
    if form.validate_on_submit():
        filename = images.save(form.image.data)
        return f'Filename: {filename}'
    return render_template('main/upload.html', form=form)
	



@main.route('/test')
@login_required
def test():
    return render_template('main/index.html')