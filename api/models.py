"""
Pydantic models for API request/response validation.
"""

from typing import Optional, List, Literal
from pydantic import BaseModel, Field


class CardResponse(BaseModel):
    """Response model for a single tarot card."""

    name: str = Field(..., description="Name of the tarot card")
    orientation: Literal["upright", "reversed"] = Field(
        ..., description="Card orientation"
    )
    meaning: str = Field(..., description="Meaning of the card in this orientation")
    position: Optional[str] = Field(
        None, description="Position in spread (e.g., 'Past', 'Present', 'Future')"
    )

    class Config:
        json_schema_extra = {
            "example": {
                "name": "The Fool",
                "orientation": "upright",
                "meaning": "New beginnings, innocence, spontaneity...",
                "position": "Present",
            }
        }


class ReadingResponse(BaseModel):
    """Response model for a complete reading."""

    spread_type: str = Field(..., description="Type of spread performed")
    cards: List[CardResponse] = Field(..., description="Cards drawn in the reading")
    timestamp: str = Field(..., description="ISO format timestamp of reading")
    seed: Optional[str] = Field(None, description="Personal seed used (if any)")
    summary: Optional[str] = Field(None, description="Reading summary or guidance")

    class Config:
        json_schema_extra = {
            "example": {
                "spread_type": "three_card",
                "cards": [
                    {
                        "name": "The Fool",
                        "orientation": "upright",
                        "meaning": "New beginnings...",
                        "position": "Past",
                    }
                ],
                "timestamp": "2025-10-31T12:00:00Z",
                "seed": "INFP",
                "summary": "This reading suggests...",
            }
        }


class DeckInfoResponse(BaseModel):
    """Response model for deck information."""

    total_cards: int = Field(..., description="Total number of cards in deck")
    major_arcana: int = Field(..., description="Number of Major Arcana cards")
    minor_arcana: int = Field(..., description="Number of Minor Arcana cards")
    suits: List[str] = Field(..., description="List of Minor Arcana suits")

    class Config:
        json_schema_extra = {
            "example": {
                "total_cards": 78,
                "major_arcana": 22,
                "minor_arcana": 56,
                "suits": ["Wands", "Cups", "Swords", "Pentacles"],
            }
        }


class CardDetailResponse(BaseModel):
    """Response model for detailed card information."""

    name: str = Field(..., description="Card name")
    suit: Optional[str] = Field(None, description="Suit (for Minor Arcana)")
    arcana: Literal["major", "minor"] = Field(..., description="Arcana type")
    upright_meaning: str = Field(..., description="Meaning when upright")
    reversed_meaning: str = Field(..., description="Meaning when reversed")

    class Config:
        json_schema_extra = {
            "example": {
                "name": "The Fool",
                "suit": None,
                "arcana": "major",
                "upright_meaning": "New beginnings, innocence...",
                "reversed_meaning": "Recklessness, taken advantage of...",
            }
        }


class DailyReadingResponse(BaseModel):
    """Response model for a daily tarot reading."""

    date: str = Field(..., description="ISO date (YYYY-MM-DD) this reading is for")
    card: CardResponse = Field(..., description="The card drawn for this day")

    class Config:
        json_schema_extra = {
            "example": {
                "date": "2026-09-23",
                "card": {
                    "name": "The Star",
                    "orientation": "upright",
                    "meaning": "Hope, faith, purpose, renewal, spirituality",
                    "position": None,
                },
            }
        }


class HealthCheckResponse(BaseModel):
    """Response model for health check endpoint."""

    status: Literal["healthy", "unhealthy"] = Field(..., description="Service status")
    version: str = Field(..., description="API version")

    class Config:
        json_schema_extra = {"example": {"status": "healthy", "version": "0.0.5"}}
