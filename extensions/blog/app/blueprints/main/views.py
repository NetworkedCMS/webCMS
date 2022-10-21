from sqlalchemy import select
from aioflask import (
    Blueprint,
    abort,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)

from aioflask.patched.flask_login import (
    current_user,
    login_required,
    login_user,
    logout_user,
)

from app.models import *
from .forms import UploadForm, ContactForm
from app.utils.flask_uploads import configure_uploads, IMAGES, UploadSet
from app.common.db import db_session as session



main = Blueprint('main', __name__)

images = UploadSet('images', IMAGES)
#configure_uploads(main, images)


@main.route("/", methods=["GET", "POST"])
async def index():
    """Home page for the website"""
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
    
    return await render_template("Bare/index.html", footer_image=footer_image, icons=media_icons,
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
async def page(page_name:str):
    """ Pages Added """

    landing_page = TemplateSetting.query.filter_by(choice=True).first()
    if landing_page is None:
        flash('Template not found, consider creating one')
        abort(404)
    template_name = landing_page.template_name#.lower()   
    nav_menu = NavMenu.all()
    slideshows = SlideShowImage.all()
    hometext = HomeText.query.first()
    call_to_action = CallToAction.query.first()
    logo = Logo.query.first()
    techno_img = TechnologiesImage.all()
    text_techno = TechnologiesText.query.first()
    footer_text = FooterText.all()
    tracking_script = TrackingScript.all()
    media_icons = SocialMediaIcon.all()
    footer_image = FooterImage.query.first()
    copyright_text = CopyRight.query.first()
    background_image = BackgroundImage.query.first()
    favicon_image = FaviconImage.query.first()
    brand = BrandName.query.first()
    seo = Seo.query.first()
    services = Service.all()
    about = About.query.first()
    team = Team.all()
    video = Video.query.first()
    counts = Counter.all()
    portfolio = Portfolio.all()
    faq = Faq.all()
    testimonial = Testimonial.all()
    client = Client.all()
    apple_touch_icon = AppleTouchIcon.query.first()
    jumbotron_html = JumbotronHtml.query.first()
    form_html = FormHtml.query.first()
    blank_html = FormHtml.all()
    album_html = AlbumHtml.query.first()
    carousel_html = CarouselHtml.query.first()
    header_script = HeaderScript.all()
    footer_script = FooterScript.all()
    header_html = HeaderHtml.query.first()
    navbar_html = NavbarHtml.query.first()
    footer_html = FooterHtml.query.first()
    features_html = FeaturesHtml.all()
    css = Css.query.first()
    pricing_html = PricingHtml.all()
    testimonials_html = TestimonialsHtml.all()
    contact_html = ContactHtml.query.first()
    page_content = Page.query.filter_by(name=page_name).first()
    pages = Page.all()
    
    #item = TemplateSetting.query.filter_by(template_name=template_name).first()
    form = ContactForm()
    if form.validate_on_submit():
        data = ContactMessage(
            name = form.name.data,
            email = form.email.data,
            text = form.text.data
        )
        session.add(data)
        await session.commit()
        flash("Message sent.", "success")
                               
    return await render_template("Bare/inner-page.html", footer_image=footer_image, icons=media_icons,
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
async def upload():
    if request.method == 'POST' and 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        rec = Photo(filename=filename, user=g.user.id)
        rec.store()
        flash("Photo saved.")
        return redirect(url_for('show', id=rec.id))
    return render_template('main/upload.html')

@main.route('/photo/<id>')
async def show(id):
    photo = Photo.load(id)
    if photo is None:
        abort(404)
    url = photos.url(photo.filename)
    return render_template('show.html', url=url, photo=photo) """

@main.route('/upload', methods=['GET', 'POST'])
@login_required
async def upload():
    form = UploadForm()
    if form.validate_on_submit():
        filename = images.save(form.image.data)
        return f'Filename: {filename}'
    return render_template('main/upload.html', form=form)
	



@main.route('/test')
@login_required
async def test():
    return render_template('main/index.html')