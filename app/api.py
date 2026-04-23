# app/api.py

"""The API skeleton uses a generic resource blueprint builder."""

from flask_restful import Resource
from flask import request
from app.handlers import handle_query
from app.extensions import cache
from app.config import CACHE_DEFAULT_TIMEOUT


def create_resource(
    name,
    wrapper_func,
    timeout_msg,
    extractor,
    default_port
):
    """Custom resource factory."""
    class GenericResource(Resource):
        """A class defining a customizable resource"""
        @cache.cached(
            timeout=CACHE_DEFAULT_TIMEOUT,
            key_prefix=lambda: f"{request.path}:{request.view_args}"
        )
        def get(self, ip, port=None):
            "Method: GET HTTP"
            port = port or default_port
            return handle_query(
                lambda: wrapper_func(ip, port),
                timeout_msg,
                extractor
            )

    GenericResource.__name__ = name
    return GenericResource
