# app/config.py

"""A set of constants and config values in use by the app."""

import os
from dotenv import load_dotenv

from app import __version__
from app.env import EnvParser


class AppMetadata:
    """App metadata"""
    APP_VERSION = __version__
    APP_ID = "renanmsv/minecraft-query-api"
    APP_NAME = "Simple Minecraft Query RESTful API"
    APP_DESCRIPTION = (
        "Query Minecraft Java and Bedrock servers for "
        "player and status information."
    )


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


class _Config:
    def __init__(self):
        self._loaded = False

        self.cache_type = None
        self.cache_options = None
        self.cache_dir = None
        self.cache_default_timeout = None
        self.cache_ignore_errors = None
        self.cache_threshold = None
        self.cache_redis_host = None
        self.cache_redis_port = None
        self.cache_redis_password = None
        self.cache_redis_db = None
        self.cache_redis_url = None
        self.cache_memcached_servers = None

        self.rate_limit_enabled = None
        self.rate_limit_default = None
        self.rate_limit_in_memory_fallback = None
        self.rate_limit_meta = None
        self.rate_limit_storage_uri = None
        self.rate_limit_storage_options = None
        self.ratelimit_ip_exempt_ips = None
        self.rate_limit_headers_enabled = None
        self.rate_limit_key_prefix = None
        self.rate_limit_strategy = None
        self.rate_limit_swallow_errors = None
        self.rate_limit_in_memory_fallback_enabled = None
        self.rate_limit_fail_on_first_breach = None

    def __getattr__(self, name):
        if not self._loaded:
            raise RuntimeError(
                "Configs not loaded yet. Call config.load_env() first"
            )

        # maps snake_case to uppercase SNAKE_CASE
        return getattr(self, name.lower())

    def load_env(self, _load_dotenv=True):
        """Loads the environment vars into the config.

        This should be called once, usually right before the app starts.

        Args:
            _load_dotenv: Whether or not to load env vars from a .env file
        """
        if self._loaded:
            return

        if _load_dotenv:
            load_dotenv()

        # Cache configs
        self.cache_type = os.getenv("CACHE_TYPE", "SimpleCache")
        self.cache_options = EnvParser.kwarg("CACHE_OPTIONS", ";", {})
        self.cache_dir = EnvParser.string("CACHE_DIR", ".cache")
        self.cache_default_timeout = EnvParser.int(
            "CACHE_DEFAULT_TIMEOUT",
            120
        )
        self.cache_ignore_errors = EnvParser.bool("CACHE_IGNORE_ERRORS", False)
        self.cache_threshold = EnvParser.int("CACHE_THRESHOLD", 500)
        self.cache_redis_host = EnvParser.string("CACHE_REDIS_HOST", "")
        self.cache_redis_port = EnvParser.int("CACHE_REDIS_PORT", 6379)
        self.cache_redis_password = EnvParser.string(
            "CACHE_REDIS_PASSWORD",
            ""
        )
        self.cache_redis_db = EnvParser.int("CACHE_REDIS_DB", 0)
        self.cache_redis_url = EnvParser.string("CACHE_REDIS_URL", "")
        self.cache_memcached_servers = EnvParser.list(
            "CACHE_MEMCACHED_SERVERS",
            ";",
            []
        )

        # Rate Limiter configs
        self.rate_limit_enabled = EnvParser.bool("RATE_LIMIT_ENABLED", True)
        self.rate_limit_default = os.getenv(
            "RATE_LIMIT_DEFAULT", "3 per second;30 per minute"
        )
        self.rate_limit_in_memory_fallback = os.getenv(
            "RATE_LIMIT_IN_MEMORY_FALLBACK", "1 per second;15 per minute"
        )
        self.rate_limit_meta = os.getenv(
            "RATE_LIMIT_META", "1000 per hour;6000 per 12 hours"
        )
        self.rate_limit_storage_uri = os.getenv(
            "RATE_LIMIT_STORAGE_URI",
            "memory://"
        )
        self.rate_limit_storage_options = EnvParser.kwarg(
            "RATE_LIMIT_STORAGE_OPTIONS"
        )
        self.ratelimit_ip_exempt_ips = EnvParser.list(
            "RATELIMIT_IP_EXEMPT_IPS")
        self.rate_limit_headers_enabled = EnvParser.bool(
            "RATE_LIMIT_HEADERS_ENABLED",
            True
        )
        self.rate_limit_key_prefix = os.getenv(
            "RATE_LIMIT_KEY_PREFIX",
            "mcqueryapi:"
        )
        self.rate_limit_strategy = os.getenv(
            "RATE_LIMIT_STRATEGY",
            "fixed-window"
        )
        self.rate_limit_swallow_errors = EnvParser.bool(
            "RATE_LIMIT_SWALLOW_ERRORS",
            True
        )
        self.rate_limit_in_memory_fallback_enabled = EnvParser.bool(
            "RATE_LIMIT_IN_MEMORY_FALLBACK_ENABLED", True
        )
        self.rate_limit_fail_on_first_breach = EnvParser.bool(
            "RATELIMIT_FAIL_ON_FIRST_BREACH", True
        )

        self._loaded = True


config = _Config()
