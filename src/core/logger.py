"""Loguru configuration for advanced logging."""

from loguru import logger


def setup_logging(level="INFO"):
    """Configure loguru with file and console output."""
    logger.add(
        "archipel.log",
        format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function}:{line} - {message}",
        level=level
    )
    return logger
