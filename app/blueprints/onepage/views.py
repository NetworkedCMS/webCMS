# -*- coding: utf-8 -*-
"""onepage section, including homepage and signup."""
import quart.flask_patch
from quart import (
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


from app.blueprints.onepage.forms import ContactForm, PublicContactForm
#from app.user.forms import RegisterForm
from app.models import *

onepage = Blueprint("onepage", __name__, static_folder="../static")



@onepage.route("/", methods=["GET", "POST"])
@login_required
async def home():
    """Home page."""
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
    apple_touch_icon = AppleTouchIcon.query.first()
    return await render_template("OnePage/index.html", footer_image=footer_image, icons=media_icons,
                           footer_text=footer_text, slideshows=slideshows,
                           home_title=hometext, logo=logo, techno_img=techno_img,
                           text_techno=text_techno, copyright_text=copyright_text,
                           background_image=background_image, call_to_action=call_to_action,
                           nav_menu=nav_menu, brand=brand, seo=seo,
                           favicon_image=favicon_image, tracking_script=tracking_script, services=services,
                           about=about, team=team, video=video, counts=counts, media_icons = media_icons,
                           portfolio=portfolio, faq=faq, testimonial=testimonial, client=client, apple_touch_icon=apple_touch_icon,
                           location=location)



@onepage.route('/contact', methods=['GET', 'POST'])
@login_required
async def contact():
    form = PublicContactForm()
    if form.validate_on_submit():
        data = ContactMessage(
            name=form.name.data,
            text=form.text.data,
            email = form.email.data
            )
        db.session.add(data)
        db.session.commit()
        await flash('Successfully sent contact message.', 'success')
        return redirect(url_for('onepage.contact'))
    return await render_template('OnePage/contact.html', form=form)
