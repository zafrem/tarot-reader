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
- Beautiful terminal display with emojis and formatting

### 🎲 Randomness Features
- **156 unique outcomes** (78 cards × 2 orientations) with meaningful content
- **Time-influenced randomness** - different results each reading, even with same personal info
- **Personal context** - incorporate personal information while maintaining randomness
- **Scalable output** - generate 1 to 78 random cards in single call
- **Rich content** - each result includes names, orientations, and detailed meanings

## Installation

```bash
pip install tarot-reader
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

### Core Functions
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

## Requirements

- Python 3.8+
- No external dependencies

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
