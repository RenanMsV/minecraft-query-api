# app/config.py

"""A set of constants and config values in use by the app."""

import os

from app import __version__
from app.env import EnvParser

# App Metadata
APP_VERSION = __version__
APP_ID = "renanmsv/minecraft-query-api"
APP_NAME = "Simple Minecraft Query RESTful API"
APP_DESCRIPTION = (
    "Query Minecraft Java and Bedrock servers for "
    "player and status information."
)


# Constants
class DefaultPorts:
    """Default ports used by Minecraft servers"""
    JAVA = 25565
    LEGACY = 25565
    BEDROCK = 19132


class OutboundMessages:
    """Messages used in warnings, prints, etc..."""
    TIMEOUT_JAVA = "Timeout. Wrong port, offline or not Java 1.7+"
    TIMEOUT_LEGACY = (
        "Timeout. Wrong port, offline or not "
        "Java Legacy (Beta 1.8 - 1.6)"
    )
    TIMEOUT_BEDROCK = "Timeout. Wrong port, offline or not Bedrock"
    RATE_LIMIT_BREACHED = "Too many requests. Please slow down."


# Cache Configs
CACHE_TYPE = os.getenv("CACHE_TYPE", "SimpleCache")
CACHE_OPTIONS = EnvParser.kwarg("CACHE_OPTIONS", ";", {})
CACHE_DIR = EnvParser.string("CACHE_DIR", ".cache")
CACHE_DEFAULT_TIMEOUT = EnvParser.int("CACHE_DEFAULT_TIMEOUT", 120)
CACHE_IGNORE_ERRORS = EnvParser.bool("CACHE_IGNORE_ERRORS", False)
CACHE_THRESHOLD = EnvParser.int("CACHE_THRESHOLD", 500)
CACHE_REDIS_HOST = EnvParser.string("CACHE_REDIS_HOST", "")
CACHE_REDIS_PORT = EnvParser.int("CACHE_REDIS_PORT", 6379)
CACHE_REDIS_PASSWORD = EnvParser.string("CACHE_REDIS_PASSWORD", "")
CACHE_REDIS_DB = EnvParser.int("CACHE_REDIS_DB", 0)
CACHE_REDIS_URL = EnvParser.string("CACHE_REDIS_URL", "")
CACHE_MEMCACHED_SERVERS = EnvParser.list("CACHE_MEMCACHED_SERVERS", ";", [])

# Rate Limiter Configs
RATE_LIMIT_ENABLED = EnvParser.bool("RATE_LIMIT_ENABLED", True)
RATE_LIMIT_DEFAULT = os.getenv(
    "RATE_LIMIT_DEFAULT",
    "3 per second;30 per minute"
)
RATE_LIMIT_IN_MEMORY_FALLBACK = os.getenv(
    "RATE_LIMIT_IN_MEMORY_FALLBACK",
    "1 per second;15 per minute"
)
RATE_LIMIT_META = os.getenv(
    "RATE_LIMIT_META",
    "1000 per hour;6000 per 12 hours"
)
RATE_LIMIT_STORAGE_URI = os.getenv("RATE_LIMIT_STORAGE_URI", "memory://")
RATE_LIMIT_STORAGE_OPTIONS = EnvParser.kwarg("RATE_LIMIT_STORAGE_OPTIONS")
RATELIMIT_IP_EXEMPT_IPS = EnvParser.list("RATELIMIT_IP_EXEMPT_IPS")
RATE_LIMIT_HEADERS_ENABLED = EnvParser.bool("RATE_LIMIT_HEADERS_ENABLED", True)
RATE_LIMIT_KEY_PREFIX = os.getenv("RATE_LIMIT_KEY_PREFIX", "mcqueryapi:")
RATE_LIMIT_STRATEGY = os.getenv("RATE_LIMIT_STRATEGY", "fixed-window")
RATE_LIMIT_SWALLOW_ERRORS = EnvParser.bool("RATE_LIMIT_SWALLOW_ERRORS", True)
RATE_LIMIT_IN_MEMORY_FALLBACK_ENABLED = EnvParser.bool(
    "RATE_LIMIT_IN_MEMORY_FALLBACK_ENABLED",
    True
)
RATE_LIMIT_FAIL_ON_FIRST_BREACH = EnvParser.bool(
    "RATELIMIT_FAIL_ON_FIRST_BREACH",
    True
)
