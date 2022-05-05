from multiprocessing.connection import wait
import quart.flask_patch
from quart import (
    Blueprint,
    abort,
    flash,
    redirect,
    render_template,
    request,
    url_for,
    jsonify,
    make_response
)
from flask.globals import session
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
from app.decorators import token_required
from app.email import send_email
from app.models import *
from app.blueprints.api.forms import *
import random


api = Blueprint('api', __name__)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@api.route('/setting')
async def index():
    """Api page."""
    data = ApiKey.query.filter_by(id=1).first()
    return await render_template('api/index.html', data=data)

@api.route('/access', methods=['GET', 'POST'])
async def access():
    """Access to API."""

    access_token = ApiKey.query.first()
    if access_token is None:
        await flash("You don't have any access yet")
        raise Exception
    access_token = access_token.access_token
    form = AccessKeyForm()
    if form.validate_on_submit():
        form.user_input.data
        if form.user_input.data == access_token:
            # if the user_input is the same as the expected input, set session
            session['session_id'] = random.uniform(0, 10)
            await flash('You can now access the API. Welcome!', 'success')
            data = ApiAccess(
                session_id = session['session_id'],
                #save the id of the session
                is_allowed = True
            )
            db.session.add(data)
            db.session.commit()
            return redirect(url_for('api.index'))
            
        else:
            await flash('Invalid access token.', 'error')
    return await render_template('api/access.html', form=form)

@api.route('/setting/<int:id>/_delete', methods=['GET', 'POST'])
@login_required
async def delete_access_key(id):
    """Delete the Api Access Key added """
    data = ApiKey.query.filter_by(id=id).first()
    db.session.commit()
    db.session.delete(data)
    await flash('Successfully deleted ' , 'success')
    return redirect(url_for('api.access'))

@api.route('/registered_users/v1/all', methods=['GET'])
@token_required
async def registered_users():
    return jsonify([*map(user_serializer, User.query.all())])

#PUT endpoint
@api.route('/registered_users/v1/<id>', methods=['PUT'])
@token_required
async def put_registered_users(id):
    data = User.query.get(id)
    return jsonify([*map(user_serializer, User.query.all())])

#DELETE endpoint
@api.route('/registered_users/v1/<int:id>', methods=['GET', 'POST'])
@token_required
async def delete_registered_users(id):
    """Delete registered_user with id using the endpoint """
    data = User.query.filter_by(id=id).first()
    if data is None:
        abort(404)
    db.session.delete(data)
    db.session.commit()
    return make_response("", 204)
    

@api.route('/template_settings/v1/all', methods=['GET'])
@token_required
async def template_settings():
    return jsonify([*map(template_settings_serializer, TemplateSetting.query.all())])

#DELETE endpoint
@api.route('/template_settings/v1/<id>', methods=['GET', 'POST'])
@token_required
async def delete_template_settings(id):
    """Delete template_settings with id using the endpoint """
    data = TemplateSetting.query.get(id)
    db.session.delete(data)
    db.session.commit()
    return make_response("", 204)

@api.route('/template_choice/v1/all', methods=['GET'])
@token_required
async def template_choice():
    return jsonify([*map(template_choice_serializer, TemplateChoice.query.all())])


#DELETE endpoint
@api.route('/template_choice/v1/<id>', methods=['GET', 'POST'])
@token_required
async def delete_template_choice(id):
    """Delete template_choice with id using the endpoint """
    data = TemplateChoice.query.get(id)
    db.session.delete(data)
    db.session.commit()
    return make_response("", 204)


@api.route('/page/v1/all', methods=['GET'])
@token_required
async def page():
    return jsonify([*map(page_serializer, Page.query.all())])

#DELETE endpoint
@api.route('/page/v1/<id>', methods=['GET', 'POST'])
@token_required
async def delete_page(id):
    """Delete page with id using the endpoint """
    data = Page.query.get(id)
    db.session.delete(data)
    db.session.commit()
    return make_response("", 204)

@api.route('/messages/v1/all', methods=['GET'])
@token_required
async def messages():
    return jsonify([*map(contact_messages_serializer, ContactMessage.query.all())])

#DELETE endpoint
@api.route('/messages/v1/<id>', methods=['GET', 'POST'])
@token_required
async def delete_messages(id):
    """Delete messages with id using the endpoint """
    data = ContactMessage.query.get(id)
    db.session.delete(data)
    db.session.commit()
    return make_response("", 204)

@api.route('/logo/v1/all', methods=['GET'])
@token_required
async def logo():
    return jsonify([*map(logo_serializer, Logo.query.all())])

#DELETE endpoint
@api.route('/logo/v1/<id>', methods=['GET', 'POST'])
@token_required
async def delete_logo(id):
    """Delete logo with id using the endpoint """
    data = Logo.query.get(id)
    db.session.delete(data)
    db.session.commit()
    return make_response("", 204)

@api.route('/slide_show_images/v1/all', methods=['GET'])
@token_required
async def slide_show_images():
    return jsonify([*map(slide_show_images_serializer, SlideShowImage.query.all())])

#DELETE endpoint
@api.route('/slide_show_images/v1/<id>', methods=['GET', 'POST'])
@token_required
async def delete_slide_show_images(id):
    """Delete slide_show_images with id using the endpoint """
    data = SlideShowImage.query.get(id)
    db.session.delete(data)
    db.session.commit()
    return make_response("", 204)

@api.route('/seo/v1/all', methods=['GET'])
@token_required
async def seo():
    return jsonify([*map(seo_serializer, Seo.query.all())])

#DELETE endpoint
@api.route('/seo/v1/<id>', methods=['GET', 'POST'])
@token_required
async def delete_seo(id):
    """Delete slide_show_images with id using the endpoint """
    data = Seo.query.get(id)
    db.session.delete(data)
    db.session.commit()
    return make_response("", 204)

@api.route('/settings/v1/all', methods=['GET'])
@token_required
async def settings():
    return jsonify([*map(settings_serializer, Setting.query.all())])

#DELETE endpoint
@api.route('/settings/v1/<id>', methods=['GET', 'POST'])
@token_required
async def delete_settings(id):
    """Delete settings with id using the endpoint """
    data = Setting.query.get(id)
    db.session.delete(data)
    db.session.commit()
    return make_response("", 204)

@api.route('/counter/v1/all', methods=['GET'])
@token_required
async def counter():
    return jsonify([*map(counter_serializer, Counter.query.all())])

#DELETE endpoint
@api.route('/counter/v1/<id>', methods=['GET', 'POST'])
@token_required
async def delete_counter(id):
    """Delete counter with id using the endpoint """
    data = Counter.query.get(id)
    db.session.delete(data)
    db.session.commit()
    return make_response("", 204)

@api.route('/hometext/v1/all', methods=['GET'])
@token_required
async def hometext():
    return jsonify([*map(hometext_serializer, HomeText.query.all())])

#DELETE endpoint
@api.route('/hometext/v1/<id>', methods=['GET', 'POST'])
@token_required
async def delete_hometext(id):
    """Delete hometext with id using the endpoint """
    data = HomeText.query.get(id)
    db.session.delete(data)
    db.session.commit()
    return make_response("", 204)

@api.route('/tracking_script/v1/all', methods=['GET'])
@token_required
async def tracking_script():
    return jsonify([*map(tracking_script_serializer, TrackingScript.query.all())])

#DELETE endpoint
@api.route('/tracking_script/v1/<id>', methods=['GET', 'POST'])
@token_required
async def delete_tracking_script(id):
    """Delete tracking_script with id using the endpoint """
    data = TrackingScript.query.get(id)
    db.session.delete(data)
    db.session.commit()
    return make_response("", 204)

@api.route('/technologies_text/v1/all', methods=['GET'])
@token_required
async def technologies_text():
    return jsonify([*map(technologies_text_serializer, TechnologiesText.query.all())])

#DELETE endpoint
@api.route('/technologies_text/v1/<id>', methods=['GET', 'POST'])
@token_required
async def delete_technologies_text(id):
    """Delete technologies_text with id using the endpoint """
    data = TrackingScript.query.get(id)
    db.session.delete(data)
    db.session.commit()
    return make_response("", 204)

@api.route('/services/v1/all', methods=['GET'])
@token_required
async def services():
    return jsonify([*map(services_serializer, Service.query.all())])

#DELETE endpoint
@api.route('/services/v1/<id>', methods=['GET', 'POST'])
@token_required
async def delete_services(id):
    """Delete services with id using the endpoint """
    data = Service.query.get(id)
    db.session.delete(data)
    db.session.commit()
    return make_response("", 204)

@api.route('/about/v1/all', methods=['GET'])
@token_required
async def about():
    return jsonify([*map(about_serializer, About.query.all())])

#DELETE endpoint
@api.route('/about/v1/<id>', methods=['GET', 'POST'])
@token_required
async def delete_about(id):
    """Delete about with id using the endpoint """
    data = About.query.get(id)
    db.session.delete(data)
    db.session.commit()
    return make_response("", 204)


@api.route('/video/v1/all', methods=['GET'])
@token_required
async def video():
    return jsonify([*map(video_serializer, Video.query.all())])

#DELETE endpoint
@api.route('/video/v1/<id>', methods=['GET', 'POST'])
@token_required
async def delete_video(id):
    """Delete video with id using the endpoint """
    data = Video.query.get(id)
    db.session.delete(data)
    db.session.commit()
    return make_response("", 204)

@api.route('/members/v1/all', methods=['GET'])
@token_required
async def members():
    return jsonify([*map(members_serializer, Team.query.all())])

#DELETE endpoint
@api.route('/members/v1/<id>', methods=['GET', 'POST'])
@token_required
async def delete_members(id):
    """Delete members with id using the endpoint """
    data = Team.query.get(id)
    db.session.delete(data)
    db.session.commit()
    return make_response("", 204)

@api.route('/portfolio/v1/all', methods=['GET'])
@token_required
async def portfolio():
    return jsonify([*map(portfolio_serializer, Portfolio.query.all())])

#DELETE endpoint
@api.route('/portfolio/v1/<id>', methods=['GET', 'POST'])
@token_required
async def delete_portfolio(id):
    """Delete portfolio with id using the endpoint """
    data = Portfolio.query.get(id)
    db.session.delete(data)
    db.session.commit()
    return make_response("", 204)

@api.route('/testimonial/v1/all', methods=['GET'])
@token_required
async def testimonial():
    return jsonify([*map(testimonial_serializer, Testimonial.query.all())])

#DELETE endpoint
@api.route('/testimonial/v1/<id>', methods=['GET', 'POST'])
@token_required
async def delete_testimonial(id):
    """Delete testimonial with id using the endpoint """
    data = Testimonial.query.get(id)
    db.session.delete(data)
    db.session.commit()
    return make_response("", 204)

@api.route('/call_to_action/v1/all', methods=['GET'])
@token_required
async def call_to_action():
    return jsonify([*map(call_to_action_serializer, CallToAction.query.all())])

#DELETE endpoint
@api.route('/call_to_action/v1/<id>', methods=['GET', 'POST'])
@token_required
async def delete_call_to_action(id):
    """Delete call_to_action with id using the endpoint """
    data = CallToAction.query.get(id)
    db.session.delete(data)
    db.session.commit()
    return make_response("", 204)

@api.route('/nav_menu/v1/all', methods=['GET'])
@token_required
async def nav_menu():
    return jsonify([*map(nav_menu_serializer, NavMenu.query.all())])

#DELETE endpoint
@api.route('/nav_menu/v1/<id>', methods=['GET', 'POST'])
@token_required
async def delete_nav_menu(id):
    """Delete call_to_action with id using the endpoint """
    data = NavMenu.query.get(id)
    db.session.delete(data)
    db.session.commit()
    return make_response("", 204)

@api.route('/technologies_images/v1/all', methods=['GET'])
@token_required
async def technologies_images():
    return jsonify([*map(technologies_images_serializer, TechnologiesImage.query.all())])

#DELETE endpoint
@api.route('/technologies_images/v1/<id>', methods=['GET', 'POST'])
@token_required
async def delete_technologies_images(id):
    """Delete technologies_images with id using the endpoint """
    data = TechnologiesImage.query.get(id)
    db.session.delete(data)
    db.session.commit()
    return make_response("", 204)

@api.route('/client/v1/all', methods=['GET'])
@token_required
async def client():
    return jsonify([*map(client_serializer, Client.query.all())])

#DELETE endpoint
@api.route('/client/v1/<id>', methods=['GET', 'POST'])
@token_required
async def delete_client(id):
    """Delete client with id using the endpoint """
    data = Client.query.get(id)
    db.session.delete(data)
    db.session.commit()
    return make_response("", 204)

@api.route('/apple_touch_icon/v1/all', methods=['GET'])
@token_required
async def apple_touch_icon():
    return jsonify([*map(apple_touch_icon_serializer, AppleTouchIcon.query.all())])

#DELETE endpoint
@api.route('/apple_touch_icon/v1/<id>', methods=['GET', 'POST'])
@token_required
async def delete_apple_touch_icon(id):
    """Delete apple_touch_icon with id using the endpoint """
    data = AppleTouchIcon.query.get(id)
    db.session.delete(data)
    db.session.commit()
    return make_response("", 204)

@api.route('/background_image/v1/all', methods=['GET'])
@token_required
async def background_image():
    return jsonify([*map(background_image_serializer, BackgroundImage.query.all())])

#DELETE endpoint
@api.route('/background_image/v1/<id>', methods=['GET', 'POST'])
@token_required
async def delete_background_image(id):
    """Delete background_image with id using the endpoint """
    data = BackgroundImage.query.get(id)
    db.session.delete(data)
    db.session.commit()
    return make_response("", 204)

@api.route('/favicon_image/v1/all', methods=['GET'])
@token_required
async def favicon_image():
    return jsonify([*map(favicon_image_serializer, FaviconImage.query.all())])

#DELETE endpoint
@api.route('/favicon_image/v1/<id>', methods=['GET', 'POST'])
@token_required
async def delete_favicon_image(id):
    """Delete favicon_image with id using the endpoint """
    data = FaviconImage.query.get(id)
    db.session.delete(data)
    db.session.commit()
    return make_response("", 204)

@api.route('/footertext/v1/all', methods=['GET'])
@token_required
async def footertext():
    return jsonify([*map(footertext_serializer, FooterText.query.all())])

#DELETE endpoint
@api.route('/footertext/v1/<id>', methods=['GET', 'POST'])
@token_required
async def delete_footertext(id):
    """Delete footertext with id using the endpoint """
    data = FaviconImage.query.get(id)
    db.session.delete(data)
    db.session.commit()
    return make_response("", 204)

@api.route('/faq/v1/all', methods=['GET'])
@token_required
async def faq():
    return jsonify([*map(faq_serializer, Faq.query.all())])

#DELETE endpoint
@api.route('/faq/v1/<id>', methods=['GET', 'POST'])
@token_required
async def delete_faq(id):
    """Delete faq with id using the endpoint """
    data = Faq.query.get(id)
    db.session.delete(data)
    db.session.commit()
    return make_response("", 204)

@api.route('/location/v1/all', methods=['GET'])
@token_required
async def location():
    return jsonify([*map(location_serializer, Location.query.all())])

#DELETE endpoint
@api.route('/location/v1/<id>', methods=['GET', 'POST'])
@token_required
async def delete_location(id):
    """Delete location with id using the endpoint """
    data = Location.query.get(id)
    db.session.delete(data)
    db.session.commit()
    return make_response("", 204)

@api.route('/brandname/v1/all', methods=['GET'])
@token_required
async def brandname():
    return jsonify([*map(brandname_serializer, BrandName.query.all())])

#DELETE endpoint
@api.route('/brandname/v1/<id>', methods=['GET', 'POST'])
@token_required
async def delete_brandname(id):
    """Delete brandname with id using the endpoint """
    data = BrandName.query.get(id)
    db.session.delete(data)
    db.session.commit()
    return make_response("", 204)


@api.route('/copyright/v1/all', methods=['GET'])
@token_required
async def copyright():
    return jsonify([*map(copyright_serializer, CopyRight.query.all())])


#DELETE endpoint
@api.route('/copyright/v1/<id>', methods=['GET', 'POST'])
@token_required
async def delete_copyright(id):
    """Delete copyright with id using the endpoint """
    data = CopyRight.query.get(id)
    db.session.delete(data)
    db.session.commit()
    return make_response("", 204)


@api.route('/resource_detail/v1/all', methods=['GET'])
@token_required
async def resource_detail():
    return jsonify([*map(resource_detail_serializer, ResourceDetail.query.all())])

#DELETE endpoint
@api.route('/resource_detail/v1/<id>', methods=['GET', 'POST'])
@token_required
async def delete_resource_detail(id):
    """Delete resource_detail with id using the endpoint """
    data = ResourceDetail.query.get(id)
    db.session.delete(data)
    db.session.commit()
    return make_response("", 204)

@api.route('/pricing/v1/all')
@token_required
async def pricing():
    return jsonify([*map(pricing_serializer, Pricing.query.all())])

#DELETE endpoint
@api.route('/pricing/v1/<id>', methods=['GET', 'POST'])
@token_required
async def delete_pricing(id):
    """Delete pricing with id using the endpoint """
    data = Pricing.query.get(id)
    db.session.delete(data)
    db.session.commit()
    return make_response("", 204)


@api.route('/pricing_attribute/v1/all', methods=['GET'])
@token_required
async def pricing_attribute():
    """Access to Pricing Attribute API."""
    return jsonify([*map(pricing_attribute_serializer, PricingAttribute.query.all())])

#DELETE endpoint
@api.route('/pricing_attribute/v1/<id>', methods=['GET', 'POST'])
@token_required
async def delete_pricing_attribute(id):
    """Delete pricing_attribute with id using the endpoint """
    data = PricingAttribute.query.get(id)
    db.session.delete(data)
    db.session.commit()
    return make_response("", 204)
    


@api.route('/cost/v1/all', methods=['GET'])
@token_required
async def cost():
    """Access to Cost API."""
    return jsonify([*map(cost_serializer, Cost.query.all())])

#DELETE endpoint
@api.route('/cost/v1/<id>', methods=['GET', 'POST'])
@token_required
async def delete_cost(id):
    """Delete cost with id using the endpoint """
    data = Cost.query.get(id)
    db.session.delete(data)
    db.session.commit()
    return make_response("", 204)