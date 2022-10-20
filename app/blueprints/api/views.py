
from aioflask import (
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
from aioflask.patched.flask_login import current_user, login_required
from flask_ckeditor import upload_success

#from app.admin.forms import (
    #ChangeAccountTypeForm,
    #ChangeUserEmailForm,
    #InviteUserForm,
    #NewUserForm,
#)
from app.common.db import db_session as db
from app.utils.decorators import token_required
from app.utils.email import send_email
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
    return render_template('api/index.html', data=data)

@api.route('/access', methods=['GET', 'POST'])
async def access():
    """Access to API."""

    access_token = ApiKey.query.first()
    #if access_token is None:
    #    flash("You don't have any access yet")
    #    raise Exception
    access_token = access_token.access_token
    form = AccessKeyForm()
    if form.validate_on_submit():
        form.user_input.data
        if form.user_input.data == access_token:
            # if the user_input is the same as the expected input, set session
            session['session_id'] = random.uniform(0, 10)
            flash('You can now access the API. Welcome!', 'success')
            ApiAccess.create(
                **dict(session_id = session['session_id'],
                #save the id of the session
                is_allowed = True)
            )
            return redirect(url_for('api.index'))
            
        else:
            flash('Invalid access token.', 'error')
    return render_template('api/access.html', form=form)

@api.route('/setting/<int:id>/_delete', methods=['GET', 'POST'])
@login_required
async def delete_access_key(id):
    """Delete the Api Access Key added """
    data = await ApiKey.get_or_404(id, 'id')
    await data.delete()
    flash('Successfully deleted ' , 'success')
    return redirect(url_for('api.access'))

@api.route('/registered_users/v1/all', methods=['GET'])
@token_required
async def registered_users():
    return jsonify([*map(user_serializer, await User.all())])

#PUT endpoint
@api.route('/registered_users/v1/<id>', methods=['PUT'])
@token_required
async def put_registered_users(id):
    #data = User.get_or_404(id, 'id')
    return jsonify([*map(user_serializer, await User.all())])

#DELETE endpoint
@api.route('/registered_users/v1/<int:id>', methods=['GET', 'POST'])
@token_required
async def delete_registered_users(id):
    """Delete registered_user with id using the endpoint """
    data = await User.get_or_404(id, 'id')
    await data.delete()
    return make_response("", 204)
    

@api.route('/template_settings/v1/all', methods=['GET'])
@token_required
async def template_settings():
    return jsonify([*map(template_settings_serializer,
         await TemplateSetting.all())])

#DELETE endpoint
@api.route('/template_settings/v1/<id>', methods=['GET', 'POST'])
@token_required
async def delete_template_settings(id):
    """Delete template_settings with id using the endpoint """
    data = await TemplateSetting.get_or_404(id, 'id')
    await data.delete()
    return make_response("", 204)

@api.route('/template_choice/v1/all', methods=['GET'])
@token_required
async def template_choice():
    return jsonify([*map(template_choice_serializer,
     await TemplateChoice.all())])


#DELETE endpoint
@api.route('/template_choice/v1/<id>', methods=['GET', 'POST'])
@token_required
async def delete_template_choice(id):
    """Delete template_choice with id using the endpoint """
    data = await TemplateChoice.get_or_404(id, 'id')
    await data.delete()
    return make_response("", 204)


@api.route('/page/v1/all', methods=['GET'])
@token_required
async def page():
    return jsonify([*map(page_serializer, await Page.all())])

#DELETE endpoint
@api.route('/page/v1/<id>', methods=['GET', 'POST'])
@token_required
async def delete_page(id):
    """Delete page with id using the endpoint """
    data = await Page.get_or_404(id, 'id')
    await data.delete()
    return make_response("", 204)

@api.route('/messages/v1/all', methods=['GET'])
@token_required
async def messages():
    return jsonify([*map(contact_messages_serializer, await ContactMessage.all())])

#DELETE endpoint
@api.route('/messages/v1/<id>', methods=['GET', 'POST'])
@token_required
async def delete_messages(id):
    """Delete messages with id using the endpoint """
    data = await ContactMessage.get_or_404(id)
    await data.delete()
    return make_response("", 204)

@api.route('/logo/v1/all', methods=['GET'])
@token_required
async def logo():
    return jsonify([*map(logo_serializer, await Logo.all())])

#DELETE endpoint
@api.route('/logo/v1/<id>', methods=['GET', 'POST'])
@token_required
async def delete_logo(id):
    """Delete logo with id using the endpoint """
    data = await Logo.get_or_404(id, 'id')
    await data.delete()
    return make_response("", 204)

@api.route('/slide_show_images/v1/all', methods=['GET'])
@token_required
async def slide_show_images():
    return jsonify([*map(slide_show_images_serializer, 
        await SlideShowImage.all())])

#DELETE endpoint
@api.route('/slide_show_images/v1/<id>', methods=['GET', 'POST'])
@token_required
async def delete_slide_show_images(id):
    """Delete slide_show_images with id using the endpoint """
    data = await SlideShowImage.get_or_404(id, 'id')
    await data.delete()
    return make_response("", 204)

@api.route('/seo/v1/all', methods=['GET'])
@token_required
async def seo():
    return jsonify([*map(seo_serializer, await Seo.all())])

#DELETE endpoint
@api.route('/seo/v1/<id>', methods=['GET', 'POST'])
@token_required
async def delete_seo(id):
    """Delete slide_show_images with id using the endpoint """
    data = await Seo.get_or_404(id, 'id')
    await data.delete()
    return make_response("", 204)

@api.route('/settings/v1/all', methods=['GET'])
@token_required
async def settings():
    return jsonify([*map(settings_serializer, 
        await Setting.all())])

#DELETE endpoint
@api.route('/settings/v1/<id>', methods=['GET', 'POST'])
@token_required
async def delete_settings(id):
    """Delete settings with id using the endpoint """
    data = await Setting.get_or_404(id, 'id')
    await data.delete()
    return make_response("", 204)

@api.route('/counter/v1/all', methods=['GET'])
@token_required
async def counter():
    return jsonify([*map(counter_serializer, 
        await Counter.all())])

#DELETE endpoint
@api.route('/counter/v1/<id>', methods=['GET', 'POST'])
@token_required
async def delete_counter(id):
    """Delete counter with id using the endpoint """
    data = await Counter.get_or_404(id, 'id')
    await data.delete()
    return make_response("", 204)

@api.route('/hometext/v1/all', methods=['GET'])
@token_required
async def hometext():
    return jsonify([*map(hometext_serializer,
         await HomeText.all())])

#DELETE endpoint
@api.route('/hometext/v1/<id>', methods=['GET', 'POST'])
@token_required
async def delete_hometext(id):
    """Delete hometext with id using the endpoint """
    data = await HomeText.get_or_404(id, 'id')
    await data.delete()
    return make_response("", 204)

@api.route('/tracking_script/v1/all', methods=['GET'])
@token_required
async def tracking_script():
    return jsonify([*map(tracking_script_serializer, 
        await TrackingScript.all())])

#DELETE endpoint
@api.route('/tracking_script/v1/<id>', methods=['GET', 'POST'])
@token_required
async def delete_tracking_script(id):
    """Delete tracking_script with id using the endpoint """
    data = await TrackingScript.get_or_404(id)
    await data.delete()
    return make_response("", 204)

@api.route('/technologies_text/v1/all', methods=['GET'])
@token_required
async def technologies_text():
    return jsonify([*map(technologies_text_serializer, 
        await TechnologiesText.all())])

#DELETE endpoint
@api.route('/technologies_text/v1/<id>', methods=['GET', 'POST'])
@token_required
async def delete_technologies_text(id):
    """Delete technologies_text with id using the endpoint """
    data = await TrackingScript.get_or_404(id, 'id')
    await data.delete()
    return make_response("", 204)

@api.route('/services/v1/all', methods=['GET'])
@token_required
async def services():
    return jsonify([*map(services_serializer, 
        await Service.query.all())])

#DELETE endpoint
@api.route('/services/v1/<id>', methods=['GET', 'POST'])
@token_required
async def delete_services(id):
    """Delete services with id using the endpoint """
    data = await Service.get_or_404(id, 'id')
    await data.delete()
    return make_response("", 204)

@api.route('/about/v1/all', methods=['GET'])
@token_required
async def about():
    return jsonify([*map(about_serializer,
         await About.all())])

#DELETE endpoint
@api.route('/about/v1/<id>', methods=['GET', 'POST'])
@token_required
async def delete_about(id):
    """Delete about with id using the endpoint """
    data = await About.get_or_404(id, 'id')
    await data.delete()
    return make_response("", 204)


@api.route('/video/v1/all', methods=['GET'])
@token_required
async def video():
    return jsonify([*map(video_serializer, 
        await Video.all())])

#DELETE endpoint
@api.route('/video/v1/<id>', methods=['GET', 'POST'])
@token_required
async def delete_video(id):
    """Delete video with id using the endpoint """
    data = await Video.get_or_404(id, 'id')
    await data.delete()
    return make_response("", 204)

@api.route('/members/v1/all', methods=['GET'])
@token_required
async def members():
    return jsonify([*map(members_serializer, 
        await Team.query.all())])

#DELETE endpoint
@api.route('/members/v1/<id>', methods=['GET', 'POST'])
@token_required
async def delete_members(id):
    """Delete members with id using the endpoint """
    data = await Team.get_or_404(id, 'id')
    await data.delete()
    return make_response("", 204)

@api.route('/portfolio/v1/all', methods=['GET'])
@token_required
async def portfolio():
    return jsonify([*map(portfolio_serializer,
         await Portfolio.all())])

#DELETE endpoint
@api.route('/portfolio/v1/<id>', methods=['GET', 'POST'])
@token_required
async def delete_portfolio(id):
    """Delete portfolio with id using the endpoint """
    data = await Portfolio.get_or_404(id, 'id')
    await data.delete()
    return make_response("", 204)

@api.route('/testimonial/v1/all', methods=['GET'])
@token_required
async def testimonial():
    return jsonify([*map(testimonial_serializer, 
        await Testimonial.query.all())])

#DELETE endpoint
@api.route('/testimonial/v1/<id>', methods=['GET', 'POST'])
@token_required
async def delete_testimonial(id):
    """Delete testimonial with id using the endpoint """
    data = await Testimonial.get_or_404(id, 'id')
    await data.delete()
    return make_response("", 204)

@api.route('/call_to_action/v1/all', methods=['GET'])
@token_required
async def call_to_action():
    return jsonify([*map(call_to_action_serializer,
         await CallToAction.all())])

#DELETE endpoint
@api.route('/call_to_action/v1/<id>', methods=['GET', 'POST'])
@token_required
async def delete_call_to_action(id):
    """Delete call_to_action with id using the endpoint """
    data = await CallToAction.get_or_404(id, 'id')
    await data.delete()
    return make_response("", 204)

@api.route('/nav_menu/v1/all', methods=['GET'])
@token_required
async def nav_menu():
    return jsonify([*map(nav_menu_serializer,
     await NavMenu.all())])

#DELETE endpoint
@api.route('/nav_menu/v1/<id>', methods=['GET', 'POST'])
@token_required
async def delete_nav_menu(id):
    """Delete call_to_action with id using the endpoint """
    data = await NavMenu.get_or_404(id, 'id')
    await data.delete()
    return make_response("", 204)

@api.route('/technologies_images/v1/all', methods=['GET'])
@token_required
async def technologies_images():
    return jsonify([*map(technologies_images_serializer,
         await TechnologiesImage.all())])

#DELETE endpoint
@api.route('/technologies_images/v1/<id>', methods=['GET', 'POST'])
@token_required
async def delete_technologies_images(id):
    """Delete technologies_images with id using the endpoint """
    data = await TechnologiesImage.get_or_404(id, 'id')
    await data.delete()
    return make_response("", 204)

@api.route('/client/v1/all', methods=['GET'])
@token_required
async def client():
    return jsonify([*map(client_serializer, await Client.all())])

#DELETE endpoint
@api.route('/client/v1/<id>', methods=['GET', 'POST'])
@token_required
async def delete_client(id):
    """Delete client with id using the endpoint """
    data = await Client.get_or_404(id, 'id')
    await data.delete()
    return make_response("", 204)

@api.route('/apple_touch_icon/v1/all', methods=['GET'])
@token_required
async def apple_touch_icon():
    return jsonify([*map(apple_touch_icon_serializer, 
        await AppleTouchIcon.all())])

#DELETE endpoint
@api.route('/apple_touch_icon/v1/<id>', methods=['GET', 'POST'])
@token_required
async def delete_apple_touch_icon(id):
    """Delete apple_touch_icon with id using the endpoint """
    data = await AppleTouchIcon.get_or_404(id, 'id')
    await data.delete()
    return make_response("", 204)

@api.route('/background_image/v1/all', methods=['GET'])
@token_required
async def background_image():
    return jsonify([*map(background_image_serializer,
         await BackgroundImage.all())])

#DELETE endpoint
@api.route('/background_image/v1/<id>', methods=['GET', 'POST'])
@token_required
async def delete_background_image(id):
    """Delete background_image with id using the endpoint """
    data = await BackgroundImage.get_or_404(id, 'id')
    await data.delete()
    return make_response("", 204)

@api.route('/favicon_image/v1/all', methods=['GET'])
@token_required
async def favicon_image():
    return jsonify([*map(favicon_image_serializer,
        await FaviconImage.all())])

#DELETE endpoint
@api.route('/favicon_image/v1/<id>', methods=['GET', 'POST'])
@token_required
async def delete_favicon_image(id):
    """Delete favicon_image with id using the endpoint """
    data = await FaviconImage.get_or_404(id, 'id')
    await data.delete()
    return make_response("", 204)

@api.route('/footertext/v1/all', methods=['GET'])
@token_required
async def footertext():
    return jsonify([*map(footertext_serializer,
     await FooterText.all())])

#DELETE endpoint
@api.route('/footertext/v1/<id>', methods=['GET', 'POST'])
@token_required
async def delete_footertext(id):
    """Delete footertext with id using the endpoint """
    data = await FaviconImage.get_or_404(id, 'id')
    await data.delete()
    return make_response("", 204)

@api.route('/faq/v1/all', methods=['GET'])
@token_required
async def faq():
    return jsonify([*map(faq_serializer,
         await Faq.all())])

#DELETE endpoint
@api.route('/faq/v1/<id>', methods=['GET', 'POST'])
@token_required
async def delete_faq(id):
    """Delete faq with id using the endpoint """
    data = await Faq.get_or_404(id, 'id')
    await data.delete()
    return make_response("", 204)

@api.route('/location/v1/all', methods=['GET'])
@token_required
async def location():
    return jsonify([*map(location_serializer,
     await Location.query.all())])

#DELETE endpoint
@api.route('/location/v1/<id>', methods=['GET', 'POST'])
@token_required
async def delete_location(id):
    """Delete location with id using the endpoint """
    data = await Location.get_or_404(id, 'id')
    await data.delete()
    return make_response("", 204)

@api.route('/brandname/v1/all', methods=['GET'])
@token_required
async def brandname():
    return jsonify([*map(brandname_serializer, await BrandName.all())])

#DELETE endpoint
@api.route('/brandname/v1/<id>', methods=['GET', 'POST'])
@token_required
async def delete_brandname(id):
    """Delete brandname with id using the endpoint """
    data = await BrandName.get_or_404(id, 'id')
    await data.delete()

    return make_response("", 204)


@api.route('/copyright/v1/all', methods=['GET'])
@token_required
async def copyright():
    return jsonify([*map(copyright_serializer,
         await CopyRight.all())])


#DELETE endpoint
@api.route('/copyright/v1/<id>', methods=['GET', 'POST'])
@token_required
async def delete_copyright(id):
    """Delete copyright with id using the endpoint """
    data = await CopyRight.get_or_404(id, 'id')
    await data.delete()
    return make_response("", 204)


@api.route('/resource_detail/v1/all', methods=['GET'])
@token_required
async def resource_detail():
    return jsonify([*map(resource_detail_serializer,
         await ResourceDetail.all())])

#DELETE endpoint
@api.route('/resource_detail/v1/<id>', methods=['GET', 'POST'])
@token_required
async def delete_resource_detail(id):
    """Delete resource_detail with id using the endpoint """
    data = await ResourceDetail.get_or_404(id, 'id')
    await data.delete()
    return make_response("", 204)

@api.route('/pricing/v1/all')
@token_required
async def pricing():
    return jsonify([*map(pricing_serializer, await Pricing.all())])

#DELETE endpoint
@api.route('/pricing/v1/<id>', methods=['GET', 'POST'])
@token_required
async def delete_pricing(id):
    """Delete pricing with id using the endpoint """
    data = await Pricing.get_or_404(id, 'id')
    await data.delete()
    return make_response("", 204)


@api.route('/pricing_attribute/v1/all', methods=['GET'])
@token_required
async def pricing_attribute():
    """Access to Pricing Attribute API."""
    return jsonify([*map(pricing_attribute_serializer, 
        await PricingAttribute.all())])

#DELETE endpoint
@api.route('/pricing_attribute/v1/<id>', methods=['GET', 'POST'])
@token_required
async def delete_pricing_attribute(id):
    """Delete pricing_attribute with id using the endpoint """
    data = await PricingAttribute.get_or_404(id, 'id')
    await data.delete()
    return make_response("", 204)
    


@api.route('/cost/v1/all', methods=['GET'])
@token_required
async def cost():
    """Access to Cost API."""
    return jsonify([*map(cost_serializer, await Cost.all())])

#DELETE endpoint
@api.route('/cost/v1/<id>', methods=['GET', 'POST'])
@token_required
async def delete_cost(id):
    """Delete cost with id using the endpoint """
    data = await Cost.get_or_404(id, 'id')
    await data.delete()
    return make_response("", 204)