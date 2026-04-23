# app/__init__.py

"""The Minecraft Query API app definition."""

__version__ = "1.2.0"

from flask import Flask
from app.extensions import cache, limiter
from app.routes.root import root_bp
from app.routes.java import java_bp
from app.routes.bedrock import bedrock_bp
from app.routes.legacy import legacy_bp


def create_app():
    """Creates the app

    Returns:
        Flask: The flask app
    """
    app = Flask(__name__.split('.', maxsplit=1)[0])
    app.url_map.strict_slashes = False

    cache.init_app(app)
    limiter.init_app(app)

    app.register_blueprint(root_bp)  # prefix: "/"
    app.register_blueprint(java_bp, url_prefix="/api/java")
    app.register_blueprint(bedrock_bp, url_prefix="/api/bedrock")
    app.register_blueprint(legacy_bp, url_prefix="/api/java_legacy")

    return app
