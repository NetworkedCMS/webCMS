from flask import render_template
from app.models import *

from app.blueprints.presento.views import presento


@presento.app_errorhandler(403)
async def forbidden(_):
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
    return render_template('Presento/errors/403.html', footer_image=footer_image, icons=media_icons,
                           footer_text=footer_text, slideshows=slideshows,
                           home_title=hometext, logo=logo, techno_img=techno_img,
                           text_techno=text_techno, copyright_text=copyright_text,
                           background_image=background_image, call_to_action=call_to_action,
                           nav_menu=nav_menu, brand=brand, seo=seo,
                           favicon_image=favicon_image, tracking_script=tracking_script, services=services,
                           about=about, team=team, video=video, counts=counts, media_icons = media_icons,
                           portfolio=portfolio, faq=faq, testimonial=testimonial, client=client), 403
                           #apple_touch_icon=apple_touch_icon)


@presento.app_errorhandler(404)
async def page_not_found(_):
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
    return render_template('Presento/errors/404.html', footer_image=footer_image, icons=media_icons,
                           footer_text=footer_text, slideshows=slideshows,
                           home_title=hometext, logo=logo, techno_img=techno_img,
                           text_techno=text_techno, copyright_text=copyright_text,
                           background_image=background_image, call_to_action=call_to_action,
                           nav_menu=nav_menu, brand=brand, seo=seo,
                           favicon_image=favicon_image, tracking_script=tracking_script, services=services,
                           about=about, team=team, video=video, counts=counts, media_icons = media_icons,
                           portfolio=portfolio, faq=faq, testimonial=testimonial, client=client), 404
                           #apple_touch_icon=apple_touch_icon)

                    


@presento.app_errorhandler(500)
async def internal_server_error(_):
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
    return render_template('Presento/errors/500.html', footer_image=footer_image, icons=media_icons,
                           footer_text=footer_text, slideshows=slideshows,
                           home_title=hometext, logo=logo, techno_img=techno_img,
                           text_techno=text_techno, copyright_text=copyright_text,
                           background_image=background_image, call_to_action=call_to_action,
                           nav_menu=nav_menu, brand=brand, seo=seo,
                           favicon_image=favicon_image, tracking_script=tracking_script, services=services,
                           about=about, team=team, video=video, counts=counts, media_icons = media_icons,
                           portfolio=portfolio, faq=faq, testimonial=testimonial, client=client), 500
                           #apple_touch_icon=apple_touch_icon)
