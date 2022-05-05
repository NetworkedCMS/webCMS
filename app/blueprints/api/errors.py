from flask import render_template

from app.blueprints.api.views import api


@api.app_errorhandler(403)
def forbidden(_):
    return render_template('errors/403.html'), 403


@api.app_errorhandler(404)
def template_not_found(_):
    return render_template('errors/404.html'), 404

@api.app_errorhandler(400)
def handle_bad_request(_):
    return render_template('errors/500.html'), 400

@api.app_errorhandler(500)
def internal_server_error(_):
    return render_template('errors/500.html'), 500



#@template_manager.errorhandler(Exception)
#def catch_exception_error(error):
    #return render_template('errors/404.html')
