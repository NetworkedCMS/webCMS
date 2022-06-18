# -*- coding: utf-8 -*-
"""onepage section, including homepage and signup."""

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
    location = await Location.all()
    client = await Client.all()
    apple_touch_icon = await AppleTouchIcon.first()
    return render_template("OnePage/index.html", footer_image=footer_image, icons=media_icons,
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
        await ContactMessage.create(
            **dict(name=form.name.data,
            text=form.text.data,
            email = form.email.data
            ))
        flash('Successfully sent contact message.', 'success')
        return redirect(url_for('onepage.contact'))
    return await render_template('OnePage/contact.html', form=form)
