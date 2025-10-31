"""
FastAPI main application.

Async REST API for tarot readings with automatic OpenAPI documentation.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from api.routers import readings, cards
from api.models import HealthCheckResponse

# Create FastAPI app with metadata
app = FastAPI(
    title="Tarot Reader API",
    description="""
    🔮 **Tarot Reader REST API** - Async tarot readings for web and mobile apps.

    This API provides:
    - **Tarot Readings**: Single card, 3-card spread, Celtic Cross, and random draws
    - **Card Information**: Browse the complete 78-card deck with meanings
    - **Personal Seeds**: Influence readings with MBTI types, questions, or traits
    - **Zero Dependencies**: Pure Python implementation with no external requirements

    ## Features
    - ✨ Async/await support for high concurrency
    - 📚 Complete 78-card tarot deck (Major + Minor Arcana)
    - 🎴 Multiple spread types for different needs
    - 🔀 Time-based randomness with optional personal seeding
    - 📖 Full upright and reversed meanings
    - 🌐 CORS enabled for browser access

    ## Entertainment Notice
    **For entertainment purposes only.** Not intended for medical, legal, or financial advice.

    ## Source Code
    GitHub: [zafrem/tarot-reader](https://github.com/zafrem/tarot-reader)
    PyPI: [tarot-reader](https://pypi.org/project/tarot-reader/)
    """,
    version="0.0.5",
    contact={
        "name": "Tarot Reader",
        "url": "https://github.com/zafrem/tarot-reader",
        "email": "zafrem@gmail.com",
    },
    license_info={
        "name": "MIT License",
        "url": "https://opensource.org/licenses/MIT",
    },
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
)

# Add CORS middleware for browser access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify actual origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(readings.router)
app.include_router(cards.router)


@app.get("/", response_model=dict)
async def root():
    """
    Root endpoint with API information.

    Returns links to documentation and available endpoints.
    """
    return {
        "message": "🔮 Welcome to Tarot Reader API",
        "version": "0.0.5",
        "documentation": "/docs",
        "redoc": "/redoc",
        "openapi_spec": "/openapi.json",
        "endpoints": {
            "readings": {
                "single": "/api/v1/readings/single",
                "three_card": "/api/v1/readings/three",
                "celtic_cross": "/api/v1/readings/celtic-cross",
                "random": "/api/v1/readings/random?count=5",
            },
            "cards": {
                "deck_info": "/api/v1/cards/deck-info",
                "major_arcana": "/api/v1/cards/major-arcana",
                "minor_arcana": "/api/v1/cards/minor-arcana",
                "by_suit": "/api/v1/cards/suit/wands",
                "search": "/api/v1/cards/search/fool",
            },
        },
        "disclaimer": "For entertainment purposes only",
    }


@app.get("/health", response_model=HealthCheckResponse)
async def health_check():
    """
    Health check endpoint for monitoring.

    Returns service status and version information.
    """
    return HealthCheckResponse(status="healthy", version="0.0.5")


@app.exception_handler(404)
async def not_found_handler(request, exc):
    """Custom 404 handler."""
    return JSONResponse(
        status_code=404,
        content={
            "detail": "Endpoint not found. Visit /docs for API documentation.",
            "documentation": "/docs",
        },
    )


@app.exception_handler(500)
async def internal_error_handler(request, exc):
    """Custom 500 handler."""
    return JSONResponse(
        status_code=500,
        content={
            "detail": "An internal error occurred. Please try again later.",
            "support": "https://github.com/zafrem/tarot-reader/issues",
        },
    )


# For running with: python -m api.main
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
