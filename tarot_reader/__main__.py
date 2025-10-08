"""
Command-line interface for tarot-reader.
"""

import argparse
from . import __version__
from .text_formatter import (
    get_single_card_text,
    get_three_card_text,
    get_celtic_cross_text,
)


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Tarot Reader - Generate tarot readings",
        prog="tarot-reader",
    )
    parser.add_argument(
        "--version", action="version", version=f"tarot-reader {__version__}"
    )
    parser.add_argument(
        "--type",
        "-t",
        choices=["single", "three", "celtic"],
        default="single",
        help="Type of reading (default: single)",
    )
    parser.add_argument(
        "--seed",
        "-s",
        type=str,
        help="Personal seed for reproducible readings (e.g., MBTI, blood type)",
    )

    args = parser.parse_args()

    # Generate reading based on type
    if args.type == "single":
        result = get_single_card_text(args.seed)
    elif args.type == "three":
        result = get_three_card_text(args.seed)
    elif args.type == "celtic":
        result = get_celtic_cross_text(args.seed)

    print(result)


if __name__ == "__main__":
    main()
