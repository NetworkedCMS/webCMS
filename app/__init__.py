import os

from quart import Quart
from quart_schema import QuartSchema
import quart.flask_patch
from flask_assets import Environment
from flask_compress import Compress
from flask_login import LoginManager
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from app.flask_uploads import UploadSet, configure_uploads, IMAGES
from flask_ckeditor import CKEditor
from flask_jwt_extended import JWTManager



from app.assets import app_css, app_js, vendor_css, vendor_js
from config import config as Config

basedir = os.path.abspath(os.path.dirname(__file__))


mail = Mail()
db = SQLAlchemy()
csrf = CSRFProtect()
compress = Compress()
images = UploadSet('images', IMAGES)
docs = UploadSet('docs', ('rtf', 'odf', 'ods', 'gnumeric', 'abw', 'doc', 'docx', 'xls', 'xlsx', 'pdf', 'css'))


# Set up Flask-Login
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'account.login'


def create_app(config):
    app = Quart(__name__)
    config_name = config

    if not isinstance(config, str):
        config_name = os.environ.get('FLASK_CONFIG')

    app.config.from_object(Config[config_name])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # not using sqlalchemy event system, hence disabling it

    Config[config_name].init_app(app)
    app.config['UPLOADED_IMAGES_DEST'] = os.environ.get('UPLOADED_IMAGES_DEST') or str(basedir)+"/static/uploads"
    app.config['UPLOADED_DOCS_DEST'] = os.environ.get('UPLOADED_DOCS_DEST')or str(basedir)+"/static/uploads"
    app.config['docs'] = app.config['UPLOADED_DOCS_DEST']
    app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this "super secret" with something else!
    #jwt = JWTManager(app)
    QuartSchema(app)



    # Set up extensions
    mail.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)
    #compress.init_app(app)
    configure_uploads(app, images)
    configure_uploads(app, docs)
    CKEditor(app)

    

    # Register Jinja template functions
    from .utils import register_template_utils
    register_template_utils(app)

    # Set up asset pipeline
    """assets_env = Environment(app)
    dirs = ['assets/styles', 'assets/scripts']
    for path in dirs:
        assets_env.append_path(os.path.join(basedir, path))
    assets_env.url_expire = True

    assets_env.register('app_css', app_css)
    assets_env.register('app_js', app_js)
    assets_env.register('vendor_css', vendor_css)
    assets_env.register('vendor_js', vendor_js)"""

    # Configure SSL if platform supports it
    if not app.debug and not app.testing and not app.config['SSL_DISABLE']:
        from flask_sslify import SSLify
        SSLify(app)

    # Create app blueprints
    from .blueprints.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .blueprints.content_manager import content_manager as content_manager_blueprint
    app.register_blueprint(content_manager_blueprint)

    from .blueprints.template_manager import template_manager as template_manager_blueprint
    app.register_blueprint(template_manager_blueprint)

    from .blueprints.messaging_manager import messaging_manager as messaging_manager_blueprint
    app.register_blueprint(messaging_manager_blueprint)

    from .blueprints.html_manager import html_manager as html_manager_blueprint
    app.register_blueprint(html_manager_blueprint)

    from .blueprints.page_manager import page_manager as page_manager_blueprint
    app.register_blueprint(page_manager_blueprint)
    
    from .blueprints.onepage import onepage as onepage_blueprint
    app.register_blueprint(onepage_blueprint)

    from .blueprints.presento import presento as presento_blueprint
    app.register_blueprint(presento_blueprint)
    

    from .blueprints.account import account as account_blueprint
    app.register_blueprint(account_blueprint)

    from .blueprints.admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint, url_prefix='/admin')

    from .blueprints.api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')

    return app
