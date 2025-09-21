# tarot-reader

A lightweight, text-based tarot reading package for Python that doubles as a powerful random content generator.

## Overview

**Dual Purpose Package:** Use it for tarot readings OR as a sophisticated random function generator for any application. Perfect for LLM integration, content generation, and personalized randomness.

**For entertainment purposes only.** This package provides a fun, text-only tarot reading experience that can be integrated into apps, chatbots, or used in the terminal.

## Features

### 🔮 Tarot Reading Features
- Complete tarot deck (78 cards) with upright and reversed meanings
- Multiple spreads: Single card, 3-Card (Past/Present/Future), Celtic Cross (10-card)
- Personal seed system for consistent, personalized readings
- Dual output formats: LLM-optimized text and beautiful CUI display

### 🎲 Random Function Features
- **156 unique outcomes** (78 cards × 2 orientations) with meaningful content
- **Seeded randomness** - same input always gives same result
- **Pure randomness** - different result every time when no seed provided
- **Scalable output** - generate 1 to 78 random items in single call
- **Rich content** - each result includes names, states, and detailed meanings
- **LLM-ready text** - clean, structured output perfect for AI processing

## Installation

```bash
pip install tarot-reader
```

## Quick Start

### 🔮 Tarot Reading Usage

#### Basic Tarot Readings
```python
from tarot_reader import draw_single, draw_three, celtic_cross

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

#### Personal Seed System (Consistent Results)
```python
# Same personal info = same reading every time
personal_info = "INFP seeking career guidance"

card1 = draw_single(personal_info)
card2 = draw_single(personal_info)  # Always same as card1

# Different personal info = different results
reading_a = draw_three("ENFJ + A+ blood type")
reading_b = draw_three("ISTJ + relationship questions")
```

### 🎲 Random Function Usage

#### Pure Random Content Generation
```python
from tarot_reader import get_single_card_text, get_random_cards_text

# Random inspirational content
inspiration = get_single_card_text("llm")
# Returns: "Strength - Courage, persuasion, influence, compassion"

# Multiple random elements
story_elements = get_random_cards_text(5, "llm")
# Returns: "1. The Fool - New beginnings\n2. Seven of Cups - Opportunities..."

# Extract just the meanings for random quotes
card = draw_single()
random_quote = card['meaning']
# Returns: "New beginnings, innocence, spontaneity, free spirit"
```

#### Seeded Random (Consistent Results)
```python
# Perfect for user-specific daily content
def daily_content(user_id, date):
    seed = f"{user_id}_{date}"
    return get_single_card_text("llm", seed)

# Same user + same date = same content
content1 = daily_content("user123", "2025-01-15")
content2 = daily_content("user123", "2025-01-15")  # Same as content1
content3 = daily_content("user123", "2025-01-16")  # Different content

# Random decision maker with consistency
def get_guidance(question):
    return get_single_card_text("llm", question)

advice = get_guidance("should I change jobs")  # Consistent for same question
```

#### Random Content for Applications
```python
# Story/game content generator
def generate_character_traits(num_traits=3):
    cards = get_random_cards_text(num_traits, "llm")
    traits = []
    for line in cards.split('\n'):
        trait = line.split(' - ')[1] if ' - ' in line else line
        traits.append(trait)
    return traits

# Random mood/theme generator
def daily_theme():
    card = draw_single()
    return {
        'theme': card['name'],
        'mood': card['orientation'],  # 'Upright' or 'Reversed'
        'description': card['meaning']
    }

# True/False random with meaning
def random_decision_with_context(question):
    card = draw_single(question)
    return {
        'decision': card['orientation'] == 'Upright',  # True/False
        'reasoning': card['meaning'],
        'context': card['name']
    }
```

## Advanced Features

### Dual Format System (LLM + CUI)

All functions support two output formats:

```python
from tarot_reader import get_single_card_text, get_reading_summary

# LLM Format - Clean text for AI processing
llm_text = get_single_card_text("llm")
# Returns: "The Fool (Reversed) - Recklessness, lack of direction"

# CUI Format - Beautiful terminal display
cui_text = get_single_card_text("cui")
# Returns: "🎴 The Fool (Reversed)\n   ↳ Recklessness, lack of direction"

# Complete readings with context
llm_reading = get_reading_summary("three", "llm", "INFP career guidance")
cui_reading = get_reading_summary("three", "cui", "INFP career guidance")
```

### LLM Integration Examples

```python
from tarot_reader import get_reading_summary, get_random_cards_text

# Perfect for sending to ChatGPT, Claude, etc.
def generate_story_with_ai(theme):
    # Get tarot-based story elements
    elements = get_random_cards_text(3, "llm", theme)

    # Send to your LLM
    prompt = f"Create a story using these elements:\n{elements}"
    # return openai.chat.completions.create(messages=[{"role": "user", "content": prompt}])

# Personal daily content for users
def personal_daily_insight(user_id, mbti_type):
    seed = f"{user_id}_{mbti_type}"
    reading = get_reading_summary("single", "llm", seed)

    # Process with LLM for personalized interpretation
    prompt = f"Interpret this tarot reading for someone with {mbti_type} personality:\n{reading}"
    # return your_llm_api(prompt)

# Consistent random content for applications
def app_feature_randomizer(feature_name, date):
    seed = f"{feature_name}_{date}"
    content = get_random_cards_text(1, "llm", seed)
    return content.split(" - ")[1]  # Just the meaning part
```

### Personal Seed Examples

```python
# MBTI Personality Types
reading = get_reading_summary("three", "llm", "ENFJ")

# Blood Types
daily_card = get_single_card_text("llm", "A+ blood type")

# Personal Questions/Reasons
guidance = get_reading_summary("single", "cui", "seeking love guidance")

# Combined Personal Information
complex_reading = get_reading_summary("celtic", "llm", "INFP + O+ blood + career change 2025")

# Any text works as a seed
user_reading = get_reading_summary("three", "cui", "username123_today")
```

## Use Cases

### 🔮 Tarot Applications
- Personal tarot reading apps
- Daily card/guidance features
- Chatbot integration for entertainment
- Meditation and mindfulness apps
- Fortune telling websites

### 🎲 Random Content Generation
- **Story/Game Development**: Generate character traits, plot elements, themes
- **Daily Content Apps**: Consistent daily quotes, moods, themes per user
- **Decision Making Tools**: Random guidance with meaningful context
- **Creative Writing**: Inspiration prompts and story seeds
- **Social Apps**: Personalized daily content based on user profiles
- **Educational Tools**: Random discussion topics, icebreakers
- **Marketing**: Consistent brand messaging with personal touch

### 🤖 LLM & AI Integration
- Feed structured random content to AI models
- Generate prompts for creative AI applications
- Provide consistent seeds for reproducible AI outputs
- Create personalized AI interactions based on user data
- Augment chatbots with meaningful random responses

## API Reference

### Core Functions
```python
# Basic tarot functions
draw_single(personal_seed=None) -> Dict
draw_three(personal_seed=None) -> Dict
celtic_cross(personal_seed=None) -> Dict

# Text formatter functions
get_single_card_text(format_type="llm", personal_seed=None) -> str
get_three_card_text(format_type="llm", personal_seed=None) -> str
get_celtic_cross_text(format_type="llm", personal_seed=None) -> str
get_random_cards_text(num_cards, format_type="llm", personal_seed=None) -> str
get_reading_summary(reading_type="single", format_type="llm", personal_seed=None) -> str
```

**Parameters:**
- `personal_seed`: Any string for consistent results (MBTI, blood type, questions, etc.)
- `format_type`: "llm" for clean text, "cui" for rich terminal display
- `reading_type`: "single", "three", "celtic", or number as string
- `num_cards`: Integer 1-78 for random card draws

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
