# app/__init__.py

"""The Minecraft Query API app definition."""

__version__ = "1.2.0"

from flask import Flask, Blueprint
from app.extensions import cache, limiter, logger
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
    logger.info(
        "Cache initialized. Type: %s, Timeout: %s",
        cache.config["CACHE_TYPE"],
        cache.config["CACHE_DEFAULT_TIMEOUT"]
    )

    limiter.init_app(app)
    logger.info(
        "Rate limiter initialized. Enabled: %s, Storage type(s): %s",
        limiter.enabled,
        limiter.storage.STORAGE_SCHEME
    )

    def _register_bp(bp: Blueprint, url_prefix=None):
        app.register_blueprint(blueprint=bp, url_prefix=url_prefix)
        logger.info(
            "Registered route bp (%s) into url (%s)",
            bp.name,
            url_prefix
        )

    _register_bp(root_bp, "/")  # prefix: "/"
    _register_bp(java_bp, url_prefix="/api/java")
    _register_bp(bedrock_bp, url_prefix="/api/bedrock")
    _register_bp(legacy_bp, url_prefix="/api/java_legacy")

    return app
