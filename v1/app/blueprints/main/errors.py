from aioflask import render_template

from app.blueprints.main.views import main


@main.app_errorhandler(403)
async def forbidden(_):
    return await render_template('errors/403.html'), 403


@main.app_errorhandler(404)
async def page_not_found(_):
    return await render_template('errors/404.html'), 404

@main.app_errorhandler(400)
async def handle_bad_request(_):
    return await render_template('errors/500.html'), 400

@main.app_errorhandler(500)
async def internal_server_error(_):
    return await render_template('errors/500.html'), 500



#@main.errorhandler(Exception)
#async def catch_exception_error(error):
    #return await render_template('errors/404.html')
