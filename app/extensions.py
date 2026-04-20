# app/extensions.py

"""Sets up necessary extensions for the app to work."""

import logging
from flask import jsonify
from flask_caching import Cache
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from app.config import APP_ID, RATE_LIMIT_DEFAULT, OutboundMessages

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] [%(name)s] %(message)s"
)
logger = logging.getLogger(APP_ID)

cache = Cache()


def rate_limit_exceeded_handler(_request_limit):
    '''Warns the user he breached the rate limit'''
    response = jsonify({
        "success": False,
        "error": {
            "type": "rate_limit_exceeded",
            "message": OutboundMessages.RATE_LIMIT_BREACHED
        }
    })
    response.status_code = 429
    return response


limiter = Limiter(
    headers_enabled=True,
    key_func=get_remote_address,
    default_limits=RATE_LIMIT_DEFAULT,
    on_breach=rate_limit_exceeded_handler
)
