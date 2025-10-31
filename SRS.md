# Software Requirements Specification (SRS)
## Tarot Reader v0.0.5

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) describes the functional and non-functional requirements for the Tarot Reader package - a lightweight, text-based Python library for tarot card readings and random content generation.

#### 1.2 Scope
The Tarot Reader package provides:
- Command-line interface (CLI) for tarot readings
- Python library API for integration into other applications
- REST API for web/mobile integration (planned)
- Zero external dependencies for core functionality
- Support for entertainment, creative writing, and LLM integration use cases

#### 1.3 Intended Audience
- Python developers integrating tarot functionality
- CLI users seeking tarot readings
- Creative writers and storytellers
- Chatbot and LLM developers
- Entertainment application developers

#### 1.4 Definitions and Acronyms
- **Tarot**: A deck of 78 cards used for divination and entertainment
- **Spread**: An arrangement of tarot cards in a specific pattern
- **Upright**: A card drawn in its normal orientation
- **Reversed**: A card drawn in an inverted orientation
- **Seed**: A personal identifier used to influence randomness
- **CLI**: Command-Line Interface
- **API**: Application Programming Interface
- **REST**: Representational State Transfer

---

### 2. Overall Description

#### 2.1 Product Perspective
Tarot Reader is a standalone Python package that:
- Operates independently without external dependencies
- Provides both CLI and programmatic interfaces
- Integrates with Python 3.8+ environments
- Supports cross-platform deployment (Linux, macOS, Windows)
- Available via PyPI for easy installation

#### 2.2 Product Features
1. **Complete Tarot Deck** (78 cards)
   - 22 Major Arcana cards
   - 56 Minor Arcana cards (4 suits: Wands, Cups, Swords, Pentacles)

2. **Multiple Spread Types**
   - Single card draw
   - 3-card spread (Past/Present/Future)
   - Celtic Cross (10-card spread)
   - Random drop (customizable card count)

3. **Personal Seed System**
   - Time-based randomness
   - Personal context integration (MBTI, questions, traits)
   - Reproducible readings with same seed
   - Hash-based seed normalization

4. **Beautiful Text Output**
   - Formatted terminal display with emojis
   - Structured JSON output for API integration
   - Reading summaries with guidance

5. **REST API** (Planned)
   - Async HTTP endpoints
   - OpenAPI documentation
   - Reading history and journal features

#### 2.3 User Classes and Characteristics
- **Developers**: Technical users integrating the library
- **CLI Users**: End users seeking personal readings
- **API Consumers**: Applications/services using REST endpoints
- **Content Creators**: Writers and storytellers using for inspiration

#### 2.4 Operating Environment
- **Platform**: Cross-platform (Linux, macOS, Windows)
- **Python Version**: 3.8, 3.9, 3.10, 3.11, 3.12
- **Dependencies**: None (core library)
- **Optional Dependencies**: FastAPI, Uvicorn (for REST API)

#### 2.5 Design and Implementation Constraints
- Must maintain zero dependencies for core functionality
- Must support Python 3.8+ for broad compatibility
- Must process readings in under 1 second (NFR-2)
- Must provide reproducible results with same seed
- Must include entertainment disclaimer

---

### 3. Functional Requirements

#### FR-1: Tarot Deck Management
**Description**: The system shall provide a complete 78-card tarot deck with upright and reversed meanings.

**Requirements**:
- FR-1.1: System shall include all 22 Major Arcana cards (The Fool through The World)
- FR-1.2: System shall include 56 Minor Arcana cards across 4 suits
- FR-1.3: Each card shall have both upright and reversed meanings
- FR-1.4: Card data shall be accessible programmatically
- FR-1.5: System shall validate deck completeness on initialization

**Priority**: Critical
**Status**: Implemented

---

#### FR-2: Single Card Reading
**Description**: The system shall provide single card draw functionality for daily guidance.

**Requirements**:
- FR-2.1: System shall draw one random card from the 78-card deck
- FR-2.2: System shall randomly determine upright or reversed orientation
- FR-2.3: System shall accept optional personal seed for influenced randomness
- FR-2.4: System shall display card name, orientation, and meaning
- FR-2.5: System shall provide formatted text output

**Priority**: Critical
**Status**: Implemented

---

#### FR-3: Three-Card Spread
**Description**: The system shall provide 3-card spread readings for Past/Present/Future insights.

**Requirements**:
- FR-3.1: System shall draw three unique cards
- FR-3.2: System shall label positions as Past, Present, Future
- FR-3.3: System shall support personal seed integration
- FR-3.4: System shall ensure no duplicate cards in spread
- FR-3.5: System shall provide formatted spread output

**Priority**: High
**Status**: Implemented

---

#### FR-4: Celtic Cross Spread
**Description**: The system shall provide comprehensive 10-card Celtic Cross readings.

**Requirements**:
- FR-4.1: System shall draw 10 unique cards
- FR-4.2: System shall assign cards to 10 specific positions:
  - Present Situation
  - Challenge
  - Distant Past
  - Recent Past
  - Best Outcome
  - Immediate Future
  - Your Approach
  - External Influences
  - Hopes and Fears
  - Final Outcome
- FR-4.3: System shall support personal seed integration
- FR-4.4: System shall provide detailed formatted output
- FR-4.5: System shall include reading summary

**Priority**: High
**Status**: Implemented

---

#### FR-5: Random Drop Feature
**Description**: The system shall provide completely random card draws using time-based seeding.

**Requirements**:
- FR-5.1: System shall accept card count parameter (1-78)
- FR-5.2: System shall use time-based randomness
- FR-5.3: System shall perform multiple shuffle iterations
- FR-5.4: System shall validate card count range
- FR-5.5: System shall return unique cards only

**Priority**: Medium
**Status**: Implemented

---

#### FR-6: Personal Seed System
**Description**: The system shall support personal seed input for influenced randomness.

**Requirements**:
- FR-6.1: System shall accept arbitrary string seeds
- FR-6.2: System shall normalize seeds (case-insensitive, whitespace handling)
- FR-6.3: System shall combine personal seed with time-based randomness
- FR-6.4: System shall use SHA-256 hashing for seed processing
- FR-6.5: System shall support MBTI types, questions, and traits as seeds
- FR-6.6: Same seed at different times shall produce different results

**Priority**: High
**Status**: Implemented

---

#### FR-7: Command-Line Interface
**Description**: The system shall provide a CLI for interactive tarot readings.

**Requirements**:
- FR-7.1: System shall support `--type` parameter (single, three, celtic, drop)
- FR-7.2: System shall support `--seed` parameter for personal context
- FR-7.3: System shall support `--version` flag
- FR-7.4: System shall display formatted output to terminal
- FR-7.5: System shall handle invalid parameters gracefully

**Priority**: High
**Status**: Implemented

---

#### FR-8: Programmatic API
**Description**: The system shall provide Python functions for library integration.

**Requirements**:
- FR-8.1: System shall export `draw_single()` function
- FR-8.2: System shall export `draw_three()` function
- FR-8.3: System shall export `celtic_cross()` function
- FR-8.4: System shall export `random_drop()` function
- FR-8.5: All functions shall return JSON-serializable data structures
- FR-8.6: System shall provide text formatter functions

**Priority**: Critical
**Status**: Implemented

---

#### FR-9: REST API
**Description**: The system shall provide async HTTP endpoints for web integration.

**Requirements**:
- FR-9.1: System shall provide GET /api/v1/readings/{type} endpoint
- FR-9.2: System shall support query parameters for seed and customization
- FR-9.3: System shall return JSON responses
- FR-9.4: System shall include OpenAPI/Swagger documentation at /docs
- FR-9.5: System shall support CORS for browser access
- FR-9.6: System shall implement async request handling
- FR-9.7: System shall provide GET /api/v1/cards endpoint for deck info
- FR-9.8: System shall include health check endpoint

**Priority**: High
**Status**: Implemented (v0.0.5)

---

#### FR-10: Reading Journal (Planned)
**Description**: The system shall support saving and retrieving reading history.

**Requirements**:
- FR-10.1: System shall save readings with timestamps
- FR-10.2: System shall associate readings with optional user context
- FR-10.3: System shall export readings to JSON format
- FR-10.4: System shall provide reading retrieval by date range
- FR-10.5: System shall support reading search and filtering

**Priority**: Medium
**Status**: Planned (v0.1.0)

---

### 4. Non-Functional Requirements

#### NFR-1: Performance
- NFR-1.1: Single card draw shall complete in < 100ms
- NFR-1.2: Celtic Cross spread shall complete in < 1000ms
- NFR-1.3: Random drop of 10 cards shall complete in < 500ms
- NFR-1.4: API endpoint response time shall be < 200ms (p95)

**Priority**: High
**Status**: Implemented

---

#### NFR-2: Reliability
- NFR-2.1: System shall have 100% test coverage for core functionality
- NFR-2.2: System shall handle invalid inputs without crashing
- NFR-2.3: System shall validate all user inputs
- NFR-2.4: System shall provide meaningful error messages

**Priority**: Critical
**Status**: Implemented (42 tests, all passing)

---

#### NFR-3: Portability
- NFR-3.1: System shall run on Linux, macOS, Windows
- NFR-3.2: System shall support Python 3.8 through 3.12
- NFR-3.3: Core library shall have zero external dependencies
- NFR-3.4: System shall be installable via pip

**Priority**: Critical
**Status**: Implemented

---

#### NFR-4: Maintainability
- NFR-4.1: Code shall follow PEP 8 style guidelines
- NFR-4.2: All public functions shall have docstrings
- NFR-4.3: Code shall use type hints for function signatures
- NFR-4.4: System shall pass linting (ruff, black, mypy)

**Priority**: High
**Status**: Implemented

---

#### NFR-5: Usability
- NFR-5.1: CLI help text shall be clear and comprehensive
- NFR-5.2: Error messages shall be user-friendly
- NFR-5.3: Output formatting shall be readable and attractive
- NFR-5.4: API documentation shall be auto-generated and interactive

**Priority**: High
**Status**: Implemented

---

#### NFR-6: Security
- NFR-6.1: System shall not execute arbitrary code from user input
- NFR-6.2: System shall validate all file paths (if file I/O added)
- NFR-6.3: API shall implement rate limiting (when implemented)
- NFR-6.4: API shall sanitize all user inputs

**Priority**: High
**Status**: Implemented

---

#### NFR-7: Scalability
- NFR-7.1: API shall support concurrent requests (async)
- NFR-7.2: System shall handle 100+ requests per second
- NFR-7.3: Memory usage shall remain < 50MB per process

**Priority**: Medium
**Status**: Implemented

---

#### NFR-8: Legal
- NFR-8.1: System shall display entertainment disclaimer
- NFR-8.2: System shall be licensed under MIT License
- NFR-8.3: All card meanings shall be original or properly attributed

**Priority**: Critical
**Status**: Implemented

---

### 5. External Interface Requirements

#### 5.1 User Interfaces
- **CLI**: Terminal-based text interface with formatted output
- **API**: REST endpoints returning JSON (planned)
- **Docs**: Web-based API documentation at /docs (planned)

#### 5.2 Hardware Interfaces
- None (software-only package)

#### 5.3 Software Interfaces
- **Python Interpreter**: 3.8+
- **Operating System**: POSIX-compliant or Windows
- **Package Manager**: pip/PyPI
- **ASGI Server**: Uvicorn (for API)

#### 5.4 Communication Interfaces
- **HTTP/HTTPS**: REST API endpoints (planned)
- **JSON**: Data exchange format
- **stdin/stdout**: CLI interaction

---

### 6. System Features

#### 6.1 Feature: Tarot Reading Engine
**Priority**: Critical
**Status**: Implemented

**Functional Requirements**: FR-1, FR-2, FR-3, FR-4, FR-5, FR-6
**Non-Functional Requirements**: NFR-1, NFR-2, NFR-3

#### 6.2 Feature: Command-Line Interface
**Priority**: High
**Status**: Implemented

**Functional Requirements**: FR-7
**Non-Functional Requirements**: NFR-5

#### 6.3 Feature: REST API
**Priority**: High
**Status**: Implemented (v0.0.5)

**Functional Requirements**: FR-9
**Non-Functional Requirements**: NFR-1, NFR-4, NFR-5, NFR-6, NFR-7

#### 6.4 Feature: Reading Journal
**Priority**: Medium
**Status**: Planned (v0.1.0)

**Functional Requirements**: FR-10
**Non-Functional Requirements**: NFR-2, NFR-6

---

### 7. Other Requirements

#### 7.1 Database Requirements
- None for v0.0.4 (stateless)
- SQLite or JSON file storage for journal feature (v0.2.0)

#### 7.2 Internationalization
- English-only for v0.0.4
- Multi-language support planned for future versions

#### 7.3 Documentation
- README.md with usage examples
- Inline docstrings for all public functions
- OpenAPI/Swagger docs for REST API (planned)

---

### 8. Appendix

#### 8.1 Use Cases

**UC-1: Daily Tarot Reading**
- **Actor**: CLI User
- **Goal**: Get a single card for daily guidance
- **Steps**:
  1. User runs `tarot-reader --type single --seed "INFP"`
  2. System draws random card with personal influence
  3. System displays card with meaning
  4. User reflects on reading

**UC-2: Relationship Question Reading**
- **Actor**: CLI User
- **Goal**: Get insights about relationship
- **Steps**:
  1. User runs `tarot-reader --type three --seed "relationship concerns"`
  2. System performs 3-card spread
  3. System displays Past/Present/Future cards
  4. User interprets spread in context of question

**UC-3: API Integration for Chatbot**
- **Actor**: Developer
- **Goal**: Integrate tarot readings into Discord bot
- **Steps**:
  1. Developer installs `tarot-reader[api]`
  2. Developer makes GET request to `/api/v1/readings/single`
  3. API returns JSON with card data
  4. Bot displays reading to Discord user

**UC-4: Creative Writing Inspiration**
- **Actor**: Writer
- **Goal**: Generate story prompts
- **Steps**:
  1. Writer calls `random_drop(5)` in Python script
  2. System returns 5 random cards
  3. Writer uses card meanings as plot points
  4. Story develops based on card themes

#### 8.2 Glossary
- **Major Arcana**: 22 trump cards representing life's spiritual lessons
- **Minor Arcana**: 56 suit cards representing daily life situations
- **Wands**: Suit representing creativity, passion, action
- **Cups**: Suit representing emotions, relationships, feelings
- **Swords**: Suit representing thoughts, intellect, conflict
- **Pentacles**: Suit representing material world, finances, career
- **Spread**: Pattern in which tarot cards are laid out
- **Position**: Specific location in a spread with assigned meaning

---

### 9. Version History

| Version | Date | Changes |
|---------|------|---------|
| 0.0.4 | 2025-01 | Initial release on PyPI |
| 0.0.5 | 2025-10 | Added REST API with FastAPI, async support, complete documentation |
| 0.1.0 | TBD | Planned: Reading journal, history tracking |

---

### 10. Approval

**Document Status**: Draft
**Last Updated**: 2025-10-31
**Maintained By**: Tarot Reader Development Team

---

**For entertainment purposes only. Not intended for medical, legal, or financial advice.**
