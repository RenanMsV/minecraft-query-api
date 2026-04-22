# app/extensions.py

"""Sets up necessary extensions for the app to work."""

import logging
import ipaddress
from flask import jsonify, request
from flask_caching import Cache
from flask_limiter import Limiter, RequestLimit
from flask_limiter.util import get_remote_address

from app import config

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] [%(name)s] %(message)s"
)
logger = logging.getLogger(config.APP_ID)

cache = Cache()


def _rate_limit_exceeded_handler(_request_limit: RequestLimit):
    """
    Handles requests that exceed the configured rate limits.

    Returns a standardized JSON response indicating that the client
    has sent too many requests within the allowed time window. This
    handler is triggered automatically by the rate limiter when any
    configured limit is breached.

    Returns:
        flask.Response: A JSON response with HTTP status code 429
        (Too Many Requests).
    """
    response = jsonify({
        "error": {
            "type": "rate_limit_exceeded",
            "message": config.OutboundMessages.RATE_LIMIT_BREACHED
        }
    })
    response.status_code = 429
    return response


def _resolve_key_func():
    """
    Resolves the key function used for rate limiting.

    Uses the client IP address as the unique identifier for each request.
    This ensures consistent and reliable rate limiting without relying on
    user-supplied headers or authentication mechanisms.

    Returns:
        Callable: A function that returns the client identifier
        (the remote IP address).
    """
    return get_remote_address


def _is_rate_limit_exempt():
    """
    Determines whether the current request should be exempt from rate limiting.

    Checks if the client IP address matches any entry in the configured
    `RATELIMIT_IP_EXEMPT_IPS` list. Entries may be individual IP addresses
    or CIDR ranges (e.g., "192.168.0.0/24").

    Returns:
        bool: True if the client IP is whitelisted and should bypass
        rate limiting, False otherwise.
    """
    ip = ipaddress.ip_address(request.remote_addr)
    for entry in config.RATELIMIT_IP_EXEMPT_IPS:
        if ip in ipaddress.ip_network(entry):
            return True
    return False


limiter = Limiter(
    enabled=config.RATE_LIMIT_ENABLED,
    headers_enabled=config.RATE_LIMIT_HEADERS_ENABLED,
    in_memory_fallback_enabled=config.RATE_LIMIT_IN_MEMORY_FALLBACK_ENABLED,
    swallow_errors=config.RATE_LIMIT_SWALLOW_ERRORS,
    fail_on_first_breach=config.RATE_LIMIT_FAIL_ON_FIRST_BREACH,
    key_func=_resolve_key_func,
    on_breach=_rate_limit_exceeded_handler,
    on_meta_breach=_rate_limit_exceeded_handler,
    default_limits_exempt_when=_is_rate_limit_exempt,
    application_limits_exempt_when=_is_rate_limit_exempt,
    storage_uri=config.RATE_LIMIT_STORAGE_URI,
    storage_options=config.RATE_LIMIT_STORAGE_OPTIONS,
    key_prefix=config.RATE_LIMIT_KEY_PREFIX,
    strategy=config.RATE_LIMIT_STRATEGY,
    default_limits=(
        [config.RATE_LIMIT_DEFAULT]
        if isinstance(config.RATE_LIMIT_DEFAULT, str)
        else list(config.RATE_LIMIT_DEFAULT)
        if config.RATE_LIMIT_DEFAULT is not None else None
    ),
    in_memory_fallback=(
        [config.RATE_LIMIT_IN_MEMORY_FALLBACK]
        if isinstance(config.RATE_LIMIT_IN_MEMORY_FALLBACK, str)
        else list(config.RATE_LIMIT_IN_MEMORY_FALLBACK)
        if config.RATE_LIMIT_IN_MEMORY_FALLBACK is not None else None
    ),
    meta_limits=(
        [config.RATE_LIMIT_META]
        if isinstance(config.RATE_LIMIT_META, str)
        else list(config.RATE_LIMIT_META)
        if config.RATE_LIMIT_META is not None else None
    )
)
