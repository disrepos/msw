"""this is for packaging the code"""

from flask import Flask
from website.auth import auth
from website.views import views


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "77372"

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    return app
