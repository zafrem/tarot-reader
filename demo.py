#!/usr/bin/env python3
"""
Simple demo script for tarot-reader package
"""

from tarot_reader import *

def main():
    print("🔮 Welcome to Tarot Reader Demo!")
    print("=" * 40)

    # Get user input
    name = input("\nEnter your name or personal info (or press Enter for random): ").strip()

    if not name:
        name = None
        print("\n🎲 Using pure random mode...")
    else:
        print(f"\n🎯 Using personal seed: {name}")

    # Show different reading types
    print("\n1. Single Card Reading:")
    print("-" * 25)
    single_reading = get_reading_summary("single", "cui", name)
    print(single_reading)

    print("\n\n2. Three Card Reading:")
    print("-" * 25)
    three_reading = get_reading_summary("three", "cui", name)
    print(three_reading)

    print("\n\n3. Random Elements for Creativity:")
    print("-" * 35)
    elements = get_random_cards_text(3, "llm", name)
    print("Story/inspiration elements:")
    for line in elements.split('\n'):
        if '. ' in line:
            element = line.split(' - ')[1] if ' - ' in line else line
            print(f"  • {element}")

if __name__ == "__main__":
    main()