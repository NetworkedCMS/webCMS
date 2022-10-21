from aioflask import render_template

from app.blueprints.template_manager.views import template_manager


@template_manager.app_errorhandler(403)
async def forbidden(_):
    return await render_template('errors/403.html'), 403


@template_manager.app_errorhandler(404)
async def template_not_found(_):
    return await render_template('errors/404.html'), 404

@template_manager.app_errorhandler(400)
async def handle_bad_request(_):
    return await render_template('errors/500.html'), 400

@template_manager.app_errorhandler(500)
async def internal_server_error(_):
    return await render_template('errors/500.html'), 500



#@template_manager.errorhandler(Exception)
#async def catch_exception_error(error):
    #return await render_template('errors/404.html')
