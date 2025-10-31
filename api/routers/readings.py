"""
Reading endpoints for tarot spreads.
"""

from datetime import datetime, timezone
from typing import Optional
from fastapi import APIRouter, Query, HTTPException

from src import draw_single, draw_three, celtic_cross, random_drop
from api.models import ReadingResponse, CardResponse

router = APIRouter(prefix="/api/v1/readings", tags=["readings"])


def _format_card_response(card: dict, position: Optional[str] = None) -> CardResponse:
    """Convert internal card dict to CardResponse model."""
    return CardResponse(
        name=card["name"],
        orientation=card["orientation"].lower(),  # Convert to lowercase for validation
        meaning=card["meaning"],
        position=position,
    )


@router.get("/single", response_model=ReadingResponse)
async def get_single_card_reading(
    seed: Optional[str] = Query(
        None,
        description="Personal seed for influenced randomness (e.g., MBTI type, question)",
        example="INFP",
    )
):
    """
    Draw a single tarot card for daily guidance.

    This endpoint provides a simple one-card reading, perfect for daily guidance
    or quick insights. The card will be randomly selected and can be influenced
    by providing a personal seed.

    **For entertainment purposes only.**
    """
    try:
        card = draw_single(seed)
        return ReadingResponse(
            spread_type="single_card",
            cards=[_format_card_response(card)],
            timestamp=datetime.now(timezone.utc).isoformat(),
            seed=seed,
            summary=None,
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error drawing card: {str(e)}")


@router.get("/three", response_model=ReadingResponse)
async def get_three_card_reading(
    seed: Optional[str] = Query(
        None,
        description="Personal seed for influenced randomness",
        example="relationship question",
    )
):
    """
    Perform a 3-card spread reading (Past/Present/Future).

    This classic spread provides insights into:
    - **Past**: Events or influences from your past
    - **Present**: Your current situation
    - **Future**: Potential outcomes or upcoming influences

    **For entertainment purposes only.**
    """
    try:
        cards_dict = draw_three(seed)  # Returns dict with position keys

        formatted_cards = [
            _format_card_response(card, position)
            for position, card in cards_dict.items()
        ]

        return ReadingResponse(
            spread_type="three_card",
            cards=formatted_cards,
            timestamp=datetime.now(timezone.utc).isoformat(),
            seed=seed,
            summary="A three-card spread revealing past influences, present circumstances, and future potential.",
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error drawing cards: {str(e)}")


@router.get("/celtic-cross", response_model=ReadingResponse)
async def get_celtic_cross_reading(
    seed: Optional[str] = Query(
        None, description="Personal seed for influenced randomness"
    )
):
    """
    Perform a comprehensive 10-card Celtic Cross reading.

    The Celtic Cross is one of the most detailed tarot spreads, examining:
    1. Present Situation
    2. Challenge
    3. Distant Past
    4. Recent Past
    5. Best Outcome
    6. Immediate Future
    7. Your Approach
    8. External Influences
    9. Hopes and Fears
    10. Final Outcome

    **For entertainment purposes only.**
    """
    try:
        cards_dict = celtic_cross(seed)  # Returns dict with position keys

        formatted_cards = [
            _format_card_response(card, position)
            for position, card in cards_dict.items()
        ]

        return ReadingResponse(
            spread_type="celtic_cross",
            cards=formatted_cards,
            timestamp=datetime.now(timezone.utc).isoformat(),
            seed=seed,
            summary="A comprehensive Celtic Cross reading examining all aspects of your situation.",
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error drawing cards: {str(e)}")


@router.get("/random", response_model=ReadingResponse)
async def get_random_drop_reading(
    count: int = Query(
        1,
        ge=1,
        le=78,
        description="Number of cards to draw (1-78)",
        example=5,
    )
):
    """
    Draw random cards using pure time-based randomness.

    Unlike other endpoints, this uses completely random selection without
    personal seed influence. Useful for:
    - Creative inspiration
    - Story prompts
    - Random exploration

    **For entertainment purposes only.**
    """
    try:
        if count < 1 or count > 78:
            raise HTTPException(
                status_code=400, detail="Count must be between 1 and 78"
            )

        cards = random_drop(count)
        formatted_cards = [_format_card_response(card) for card in cards]

        return ReadingResponse(
            spread_type="random_drop",
            cards=formatted_cards,
            timestamp=datetime.now(timezone.utc).isoformat(),
            seed=None,
            summary=f"Random draw of {count} card{'s' if count != 1 else ''} using time-based randomness.",
        )
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error drawing cards: {str(e)}")
