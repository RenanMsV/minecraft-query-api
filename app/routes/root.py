# app/routes/root.py

"""Defines the main page/root route."""

from http import HTTPStatus
from flask import Blueprint
from flask_restful import Api, Resource

from app.extensions import cache
from app.config import (
    config,
    AppMetadata,
    DefaultPorts
)

root_bp = Blueprint("root", __name__)
api = Api(root_bp)


class Root(Resource):
    """Main page route."""
    @cache.cached(timeout=config.CACHE_DEFAULT_TIMEOUT)
    def get(self):
        """The main page shows a status message and other informations"""
        return {
            "status": "online",
            "service": AppMetadata.APP_NAME,
            "version": AppMetadata.APP_VERSION,
            "description": AppMetadata.APP_DESCRIPTION,
            "routes": {
                "java_full": "/api/java/full/{ip}/{port?}",
                "java_players": "/api/java/playercount/{ip}/{port?}",
                "java_latency": "/api/java/latency/{ip}{port?}",

                "legacy_full": "/api/legacy/full/{ip}/{port?}",
                "legacy_players": "/api/legacy/playercount/{ip}/{port?}",
                "legacy_latency": "/api/legacy/latency/{ip}{port?}",

                "bedrock_full": "/api/bedrock/full/{ip}/{port?}",
                "bedrock_players": "/api/bedrock/playercount/{ip}/{port?}",
                "bedrock_latency": "/api/bedrock/latency/{ip}/{port?}"
            },
            "default_ports": {
                "java": DefaultPorts.JAVA,
                "legacy": DefaultPorts.LEGACY,
                "bedrock": DefaultPorts.BEDROCK
            },
            "cache": {
                "cache_timeout_ms": config.CACHE_DEFAULT_TIMEOUT * 1000
            }
        }, HTTPStatus.OK


api.add_resource(Root, "/")
