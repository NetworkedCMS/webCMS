# -*- coding: utf-8 -*-
"""presento section, including homepage and signup."""
from aioflask import (
    Blueprint,
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
    logout_user
)


from app.blueprints.presento.forms import ContactForm, PublicContactForm
#from app.user.forms import RegisterForm
from app.models import *


presento = Blueprint("presento", __name__, static_folder="../static")



@presento.route("/", methods=["GET", "POST"])
@login_required
async def home():
    """Home page."""
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
    location = await Location.all()
    apple_touch_icon = await AppleTouchIcon.first()
    return render_template("Presento/index.html", footer_image=footer_image, icons=media_icons,
                           footer_text=footer_text, slideshows=slideshows,
                           home_title=hometext, logo=logo, techno_img=techno_img,
                           text_techno=text_techno, copyright_text=copyright_text,
                           background_image=background_image, call_to_action=call_to_action,
                           nav_menu=nav_menu, brand=brand, seo=seo,
                           favicon_image=favicon_image, tracking_script=tracking_script, services=services,
                           about=about, team=team, video=video, counts=counts, media_icons = media_icons,
                           portfolio=portfolio, faq=faq, testimonial=testimonial, client=client, apple_touch_icon=apple_touch_icon,
                           location=location)


@presento.route('/portfolio/<int:id>/', methods=['GET', 'POST'])
@login_required
async def portfolio_details(id):
    """View portfolio details """
    data = Portfolio.query.filter_by(id=id).first_or_404()
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
    location = Location.query.all()
    client = Client.query.all()
    return render_template("Presento/portfolio-details.html", data=data, footer_image=footer_image, icons=media_icons,
                           footer_text=footer_text, slideshows=slideshows,
                           home_title=hometext, logo=logo, techno_img=techno_img,
                           text_techno=text_techno, copyright_text=copyright_text,
                           background_image=background_image, call_to_action=call_to_action,
                           nav_menu=nav_menu, brand=brand, seo=seo,
                           favicon_image=favicon_image, tracking_script=tracking_script, services=services,
                           about=about, team=team, video=video, counts=counts, media_icons = media_icons,
                           portfolio=portfolio, faq=faq, testimonial=testimonial, client=client, apple_touch_icon=apple_touch_icon,
                           location=location)





@presento.route('/contact', methods=['GET', 'POST'])
async def contact():
    form = PublicContactForm()
    if form.validate_on_submit():
        await ContactMessage.create(
            **dict(name=form.name.data,
            text=form.text.data,
            email = form.email.data
            ))
        flash('Successfully sent contact message.', 'success')
        return redirect(url_for('onepage.contact'))
    return render_template('OnePage/contact.html', form=form)

