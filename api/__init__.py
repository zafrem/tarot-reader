"""
Tarot Reader REST API

FastAPI-based async REST API for tarot readings.
Provides HTTP endpoints for all tarot reading functionality.
"""

from .main import app

__version__ = "0.0.5"

__all__ = ["app"]
