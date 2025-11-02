# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.0.5] - 2025-11-01

### Added
- REST API with FastAPI support
  - Async REST API endpoints for all reading types
  - Automatic OpenAPI documentation (Swagger UI and ReDoc)
  - Health check and status endpoints
  - Card information endpoints (deck info, major/minor arcana, suit filtering)
  - Card search functionality
  - CORS middleware for browser-based clients
- Docker support for API deployment
  - Dockerfile for API server
  - Docker Compose configuration
- Python client examples for API consumption
- JavaScript/TypeScript client examples

### Changed
- Updated README with comprehensive API documentation
- Enhanced installation instructions with API extras
- Improved project structure to support API module

## [0.0.4] - 2024

### Changed
- Updated CI/CD pipeline configuration
- Improved build and release workflows

## [0.0.1] - 2024

### Added
- Initial public release
- Complete tarot deck (78 cards) with upright and reversed meanings
- Multiple spread types:
  - Single card reading
  - 3-Card spread (Past/Present/Future)
  - Celtic Cross (10-card spread)
- Personal seed system with time component for randomness
- Beautiful terminal display with emojis and formatting
- Core reading functions:
  - `draw_single()` - Single card draw
  - `draw_three()` - Three-card spread
  - `celtic_cross()` - Celtic Cross spread
- Text formatter functions:
  - `get_single_card_text()` - Formatted single card
  - `get_three_card_text()` - Formatted three-card spread
  - `get_celtic_cross_text()` - Formatted Celtic Cross
  - `get_random_cards_text()` - Random card generator (1-78 cards)
  - `get_reading_summary()` - Complete reading summaries
- Time-influenced randomness system
  - 156 unique outcomes (78 cards × 2 orientations)
  - Different results each reading, even with same personal info
  - Personal context incorporation
- Command-line interface (CLI)
- Comprehensive test suite
- MIT License
- Documentation and examples

### Features
- Pure Python implementation with no external dependencies (core library)
- Python 3.8+ support
- Entertainment-focused tarot reading experience
- Integration-ready for apps, chatbots, and terminal use

## [Unreleased]

### Planned
- Additional spread types
- Enhanced card interpretations
- Batch reading capabilities
- Reading history tracking
- Custom deck support

---

## Version History

- **0.0.5** - Current version with REST API support
- **0.0.4** - CI/CD improvements
- **0.0.1** - Initial public release

## Links

- [PyPI Package](https://pypi.org/project/tarot-reader/)
- [GitHub Repository](https://github.com/zafrem/tarot-reader)
- [Issue Tracker](https://github.com/zafrem/tarot-reader/issues)
