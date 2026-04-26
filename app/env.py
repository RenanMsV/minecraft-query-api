# app/env.py

"""Handles the loading and parsing of environment variables"""

import os


class EnvParser:
    """Parsing Environment Variables"""

    TRUE_VALUES = {"1", "true", "yes", "on"}
    FALSE_VALUES = {"0", "false", "no", "off"}

    @staticmethod
    def _infer(value: str):
        """Infer the type of a string value."""
        # Int
        try:
            return int(value)
        except ValueError:
            pass
        # Float
        try:
            return float(value)
        except ValueError:
            pass
        # Bool (only non-numeric strings reach here)
        if value.lower() in EnvParser.TRUE_VALUES:
            return True
        if value.lower() in EnvParser.FALSE_VALUES:
            return False
        # String fallback
        return value

    @staticmethod
    def bool(name, default=False):
        """Parses a string as a boolean.

        Args:
            name: The environment variable name.
            default: A value that must be returned as a fallback.
        """
        value = os.getenv(name)
        if value is None:
            return default
        value = value.strip().lower()
        if value in EnvParser.TRUE_VALUES:
            return True
        if value in EnvParser.FALSE_VALUES:
            return False
        raise ValueError(f"Invalid boolean value for {name}: {value}")

    @staticmethod
    def int(name, default=None):
        """Parses a string as an interger.

        Args:
            name: The environment variable name.
            default: A value that must be returned as a fallback.
        """
        value = os.getenv(name)
        if value is None:
            return default
        try:
            return int(value)
        except ValueError as e:
            raise ValueError(f"Invalid int value for {name}: {value}") from e

    @staticmethod
    def string(name, default=None):
        """Does not parse, just returns the string.

        This works almost the same as:
        ```
        import os
        os.getenv(name: str, default: str)
        ```
        But in here you can set a default value with a type other than string.

        Args:
            name: The environment variable name.
            default: A value that must be returned as a fallback.
        """
        value = os.getenv(name)
        if value is None:
            return default
        return value

    @staticmethod
    def list(name, separator=";", default=None):
        """Parse environment variable into a list using a separator.

        Args:
            name: The environment variable name.
            default: A value that must be returned as a fallback.
        """
        value = os.getenv(name)
        if value is None:
            return default if default is not None else []

        items = [
            item.strip()
            for item in value.split(separator)
            if item.strip()
        ]
        return items

    @staticmethod
    def kwarg(name, separator=";", default=None, infer_types=True):
        """Parse environment variable into a non-nested kwarg dict.

        Args:
            name: The environment variable name.
            default: A value that must be returned as a fallback.
        """
        value = os.getenv(name)
        if value is None:
            return default if default is not None else {}

        result = {}
        for item in value.split(separator):
            item = item.strip()
            if not item:
                continue
            if "=" not in item:
                raise ValueError(
                    f"Invalid key=value pair for {name}: {item!r}"
                )
            key, _, val = item.partition("=")
            key = key.strip()
            val = val.strip()
            if not key:
                raise ValueError(f"Empty key in {name}: {item!r}")
            result[key] = EnvParser._infer(val) if infer_types else val

        return result
