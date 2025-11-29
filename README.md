# tarot-reader

A lightweight, text-based tarot reading package for Python with beautiful terminal display.

## Overview

A pure tarot reading package with randomized results and optional personal seeding for consistent readings.

**For entertainment purposes only.** This package provides a fun, text-only tarot reading experience that can be integrated into apps, chatbots, or used in the terminal.

## Features

### 🔮 Tarot Reading Features
- Complete tarot deck (78 cards) with upright and reversed meanings
- Multiple spreads: Single card, 3-Card (Past/Present/Future), Celtic Cross (10-card)
- Personal seed system with time component for truly random readings
- **NEW:** Async REST API with FastAPI and automatic OpenAPI documentation

### 💻 CLI Features
- Beautiful terminal display with emojis and formatting
- Interactive CLI with card search functionality

### 🎲 Randomness Features
- **156 unique outcomes** (78 cards × 2 orientations) with meaningful content
- **Time-influenced randomness** - different results each reading, even with same personal info
- **Personal context** - incorporate personal information while maintaining randomness
- **Scalable output** - generate 1 to 78 random cards in single call
- **Rich content** - each result includes names, orientations, and detailed meanings

## Installation

### Core Library
```bash
pip install tarot-reader
```

### With REST API Support
```bash
pip install tarot-reader[api]
```

## Quick Start

### 🔮 Tarot Reading Usage

#### Basic Tarot Readings
```python
from src import draw_single, draw_three, celtic_cross

# Single card draw
card = draw_single()
print(f"{card['name']} - {card['meaning']}")

# 3-Card spread (Past/Present/Future)
reading = draw_three()
for position, card in reading.items():
    print(f"{position}: {card['name']} - {card['meaning']}")

# Celtic Cross (10-card spread)
reading = celtic_cross()
for position, card in reading.items():
    print(f"{position}: {card['name']} - {card['meaning']}")
```

## CLI Usage

The package includes an interactive command-line interface. To use it, run the `cli.py` script:

```bash
python3 cli.py
```

You will be presented with a main menu with the following options:

1.  **Search for a card**: Look up a specific card by name, number, or alias.
2.  **Shuffle cards for a reading**: Start a classic tarot reading session.
3.  **Exit**: Close the CLI.

### Card Search

When you choose the search option, you can enter a query to find cards. The search is case-insensitive.

**Search by Name:**

```
Enter your search query: The Fool
```

**Search by Number (for Major Arcana):**

```
Enter your search query: 10
```

**Search by Alias:**

Aliases are created using the first letter of the suit and the card's rank.

*   **Suits**: `w` (Wands), `c` (Cups), `s` (Swords), `p` (Pentacles)
*   **Ranks**: `a` (Ace), `2-10`, `p` (Page), `kn` (Knight), `q` (Queen), `k` (King)

Examples:

*   `s1` or `sa` for **Ace of Swords**
*   `w10` for **Ten of Wands**
*   `ck` for **King of Cups**

```
Enter your search query: s1
```

### Tarot Reading

This option will start the original tarot reading flow, where you can get a single card, a three-card spread, or a creative elements reading. You can also provide a personal seed for a more personalized experience.

#### Personal Context (Time-Influenced Randomness)
```python
# Personal info influences but doesn't determine results
personal_info = "INFP seeking career guidance"

card1 = draw_single(personal_info)
card2 = draw_single(personal_info)  # Different from card1 due to time component

# Different personal info = different results
reading_a = draw_three("ENFJ + A+ blood type")
reading_b = draw_three("ISTJ + relationship questions")
```

#### Terminal Display
```python
from src import get_single_card_text, get_random_cards_text

# Beautiful terminal display
card_display = get_single_card_text()
# Returns: "🎴 Strength\n   ↳ Courage, persuasion, influence, compassion"

# Multiple cards with formatting
cards_display = get_random_cards_text(3)
# Returns formatted multi-card display with headers and numbering

# Extract just the meanings for simple use
card = draw_single()
meaning = card['meaning']
# Returns: "New beginnings, innocence, spontaneity, free spirit"
```

#### Reading Applications
```python
# Daily guidance with personal context
def daily_guidance(user_info):
    return get_single_card_text(user_info)

# Themed readings
def themed_reading(theme, num_cards=3):
    return get_random_cards_text(num_cards, theme)

# Simple decision helper
def get_guidance(question):
    card = draw_single(question)
    return {
        'card': card['name'],
        'orientation': card['orientation'],
        'guidance': card['meaning']
    }
```

## Advanced Features

### Complete Reading Summaries

Get full reading experiences with context and beautiful formatting:

```python
from src import get_reading_summary

# Single card with decorative header
daily_reading = get_reading_summary("single", "INFP career guidance")
# Returns: Full formatted reading with header, card, and interpretation

# Three-card spread with guidance
three_card = get_reading_summary("three", "seeking relationship advice")
# Returns: Past/Present/Future spread with context

# Celtic Cross for deep insight
celtic = get_reading_summary("celtic", "major life decision")
# Returns: Full 10-card spread with position explanations
```

### Personal Context Examples

```python
# MBTI Personality Types
reading = get_reading_summary("three", "ENFJ")

# Personal Questions/Reasons
guidance = get_reading_summary("single", "seeking love guidance")

# Combined Personal Information
complex_reading = get_reading_summary("celtic", "INFP + career change 2025")

# Themed readings
themed = get_reading_summary("single", "morning meditation")
```

## Use Cases

### 🔮 Tarot Applications
- Personal tarot reading apps
- Daily card/guidance features
- Terminal-based tarot readers
- Meditation and mindfulness apps
- Fortune telling websites
- Personal guidance tools

### 🎲 Content Generation
- **Story/Game Development**: Generate character traits, plot elements, themes
- **Daily Content Apps**: Time-influenced daily quotes, moods, themes
- **Decision Making Tools**: Random guidance with meaningful context
- **Creative Writing**: Inspiration prompts and story seeds
- **Educational Tools**: Random discussion topics, icebreakers
- **Personal Tools**: Themed guidance and reflection prompts

## API Reference

### Python Library API

#### Core Functions
```python
# Basic tarot functions
draw_single(personal_seed=None) -> Dict
draw_three(personal_seed=None) -> Dict
celtic_cross(personal_seed=None) -> Dict

# Text formatter functions
get_single_card_text(personal_seed=None) -> str
get_three_card_text(personal_seed=None) -> str
get_celtic_cross_text(personal_seed=None) -> str
get_random_cards_text(num_cards, personal_seed=None) -> str
get_reading_summary(reading_type="single", personal_seed=None) -> str
```

**Parameters:**
- `personal_seed`: Any string for personal context (MBTI, questions, themes, etc.)
- `reading_type`: "single", "three", "celtic", or number as string
- `num_cards`: Integer 1-78 for random card draws

**Note:** All functions now include time-based randomness, so identical inputs will produce different results each time.

### REST API

The Tarot Reader now includes a fully async FastAPI-based REST API with automatic OpenAPI documentation.

#### Starting the API Server

**Local Development:**
```bash
# Install with API dependencies
pip install tarot-reader[api]

# Start the server
uvicorn api.main:app --reload

# Or run directly
python -m api.main
```

**Using Docker:**
```bash
# Build and run with docker-compose
docker-compose up api

# Or build manually
docker build -f docker/Dockerfile.api -t tarot-reader-api .
docker run -p 8000:8000 tarot-reader-api
```

**Production Deployment:**
```bash
# With multiple workers
uvicorn api.main:app --host 0.0.0.0 --port 8000 --workers 4
```

#### API Endpoints

**Interactive Documentation:**
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`
- OpenAPI JSON: `http://localhost:8000/openapi.json`

**Reading Endpoints:**

```bash
# Single card reading
GET /api/v1/readings/single?seed=INFP
curl "http://localhost:8000/api/v1/readings/single?seed=INFP"

# Three-card spread
GET /api/v1/readings/three?seed=relationship+question
curl "http://localhost:8000/api/v1/readings/three"

# Celtic Cross (10 cards)
GET /api/v1/readings/celtic-cross?seed=career+decision
curl "http://localhost:8000/api/v1/readings/celtic-cross"

# Random drop (1-78 cards)
GET /api/v1/readings/random?count=5
curl "http://localhost:8000/api/v1/readings/random?count=5"
```

**Card Information Endpoints:**

```bash
# Get deck information
GET /api/v1/cards/deck-info
curl "http://localhost:8000/api/v1/cards/deck-info"

# Get all Major Arcana cards
GET /api/v1/cards/major-arcana
curl "http://localhost:8000/api/v1/cards/major-arcana"

# Get all Minor Arcana cards
GET /api/v1/cards/minor-arcana
curl "http://localhost:8000/api/v1/cards/minor-arcana"

# Get cards by suit
GET /api/v1/cards/suit/wands
curl "http://localhost:8000/api/v1/cards/suit/cups"

# Search for a specific card
GET /api/v1/cards/search/fool
curl "http://localhost:8000/api/v1/cards/search/tower"
```

**Health & Status:**

```bash
# Health check
GET /health
curl "http://localhost:8000/health"

# API root (all endpoints)
GET /
curl "http://localhost:8000/"
```

#### API Response Example

```json
{
  "spread_type": "three_card",
  "cards": [
    {
      "name": "The Fool",
      "orientation": "upright",
      "meaning": "New beginnings, innocence, spontaneity, free spirit",
      "position": "Past"
    },
    {
      "name": "The Magician",
      "orientation": "reversed",
      "meaning": "Manipulation, poor planning, untapped talents",
      "position": "Present"
    },
    {
      "name": "The High Priestess",
      "orientation": "upright",
      "meaning": "Intuition, sacred knowledge, divine feminine, subconscious",
      "position": "Future"
    }
  ],
  "timestamp": "2025-10-31T12:00:00Z",
  "seed": "INFP",
  "summary": "A three-card spread revealing past influences, present circumstances, and future potential."
}
```

#### Python Client Example

```python
import requests

# Single card reading
response = requests.get(
    "http://localhost:8000/api/v1/readings/single",
    params={"seed": "INFP"}
)
reading = response.json()

print(f"Card: {reading['cards'][0]['name']}")
print(f"Orientation: {reading['cards'][0]['orientation']}")
print(f"Meaning: {reading['cards'][0]['meaning']}")

# Three-card spread
response = requests.get(
    "http://localhost:8000/api/v1/readings/three",
    params={"seed": "career guidance"}
)
reading = response.json()

for card in reading['cards']:
    print(f"{card['position']}: {card['name']} ({card['orientation']})")
    print(f"  {card['meaning']}")
```

#### JavaScript/TypeScript Client Example

```typescript
// Single card reading
const response = await fetch(
  'http://localhost:8000/api/v1/readings/single?seed=INFP'
);
const reading = await response.json();

console.log(`Card: ${reading.cards[0].name}`);
console.log(`Meaning: ${reading.cards[0].meaning}`);

// Random cards
const randomResponse = await fetch(
  'http://localhost:8000/api/v1/readings/random?count=3'
);
const randomReading = await randomResponse.json();

randomReading.cards.forEach(card => {
  console.log(`${card.name} (${card.orientation}): ${card.meaning}`);
});
```

#### CORS Support

The API includes CORS middleware configured to allow browser-based clients. For production, update the `allow_origins` in `api/main.py` to specify your frontend domains.

## Requirements

**Core Library:**
- Python 3.8+
- No external dependencies

**REST API (optional):**
- FastAPI >= 0.110.0
- Uvicorn[standard] >= 0.27.0
- Pydantic >= 2.6.0

## Development

```bash
# Clone the repository
git clone https://github.com/yourusername/tarot-reader.git
cd tarot-reader

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode
pip install -e .

# Run tests
python -m unittest discover tests
```

## License

MIT License - see LICENSE file for details.

## Disclaimer

This package is for entertainment purposes only. It is not intended for professional fortune-telling or making important life decisions.
