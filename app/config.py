# app/config.py

"""A set of constants and config values in use by the app."""

from app import __version__

APP_VERSION = __version__
APP_ID = "renanmsv/minecraft-query-api"
APP_NAME = "Simple Minecraft Query RESTful API"
APP_DESCRIPTION = (
    "Query Minecraft Java and Bedrock servers for "
    "player and status information."
)

CACHE_TIMEOUT = 120
RATE_LIMIT_DEFAULT = "30 per minute"
PRINT_ROUTES_ON_START = False


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
