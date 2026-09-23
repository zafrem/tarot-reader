"""
Daily Tarot endpoints.
"""

from typing import List, Optional
from fastapi import APIRouter, Query, HTTPException

from src.core import daily_reading
from src.history import record_daily_reading, get_daily_history
from api.models import DailyReadingResponse, CardResponse

router = APIRouter(prefix="/api/v1/daily", tags=["daily"])


def _format_daily_response(reading: dict) -> DailyReadingResponse:
    """Convert an internal daily reading dict to a DailyReadingResponse."""
    return DailyReadingResponse(
        date=reading["date"],
        card=CardResponse(
            name=reading["name"],
            orientation=reading["orientation"].lower(),
            meaning=reading["meaning"],
            position=None,
        ),
    )


@router.get("", response_model=DailyReadingResponse)
async def get_daily_card(
    seed: Optional[str] = Query(
        None,
        description=(
            "Optional personal seed for a personalized daily card. Without "
            "one, every caller gets the same card for the day, and that "
            "card is saved to the server's public daily-card history. With "
            "a seed, the card is computed but not saved server-side — the "
            "client is responsible for persisting it if desired."
        ),
        example="INFP",
    )
):
    """
    Get today's tarot card.

    Deterministic per calendar date: repeated calls on the same day (with
    the same seed, if any) return the same card.

    **For entertainment purposes only.**
    """
    try:
        if seed:
            reading = daily_reading(seed)
        else:
            reading = record_daily_reading()
        return _format_daily_response(reading)
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error getting daily card: {str(e)}"
        )


@router.get("/history", response_model=List[DailyReadingResponse])
async def get_daily_card_history():
    """
    Get the server's public history of past (seed-less) daily cards.

    Only the shared card-of-the-day is persisted server-side; personalized
    (seeded) daily cards are never saved here.
    """
    try:
        history = get_daily_history()
        return [_format_daily_response(reading) for reading in history]
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error reading daily history: {str(e)}"
        )
