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
    @cache.cached(timeout=86400)
    def get(self):
        """The main page shows a status message and other informations"""
        return {
            "status": "online",
            "service": AppMetadata.APP_NAME,
            "version": AppMetadata.APP_VERSION,
            "description": AppMetadata.APP_DESCRIPTION,
            "routes": {
                "full": "/api/{server_type}/full/{ip}/{port?}",
                "player_amount": "/api/{server_type}/playercount/{ip}/{port?}",
                "latency": "/api/{server_type}/latency/{ip}{port?}",
            },
            "server_types": ["java", "legacy", "bedrock"],
            "default_ports": {
                "java": DefaultPorts.JAVA,
                "legacy": DefaultPorts.LEGACY,
                "bedrock": DefaultPorts.BEDROCK
            },
            "cache_timeout_ms": config.CACHE_DEFAULT_TIMEOUT * 1000
        }, HTTPStatus.OK


api.add_resource(Root, "/")
