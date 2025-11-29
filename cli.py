#!/usr/bin/env python3
"""
Enhanced CLI for tarot-reader package with personalized readings and card search.
"""

from src import *

def get_user_info():
    """Collect comprehensive user information for personalized readings."""
    print("For personalized readings, please provide some information about yourself.")
    print("This will be used as a seed to create readings tailored to your energy.")
    print("\nExamples of good seeds:")
    print("  • Name + MBTI: 'Sarah ENFP'")
    print("  • Name + Personality: 'Alex creative introvert'")
    print("  • Name + Traits: 'Jordan analytical perfectionist'")
    print("  • Name + Current state: 'Kim stressed about career'")
    print("-" * 50)
    
    # Get personal seed
    seed_input = input("\nEnter your personal seed (name, MBTI, personality, etc.) or press Enter for random: ").strip()
    
    if not seed_input:
        return None, None
    
    # Get purpose/question
    print("\nWhat's the purpose of this reading? What guidance are you seeking?")
    print("Examples:")
    print("  • 'Career guidance for job change'")
    print("  • 'Relationship advice'")
    print("  • 'Personal growth insights'")
    print("  • 'Creative inspiration'")
    print("  • 'Daily guidance'")
    
    purpose = input("\nEnter your purpose/question (optional): ").strip()
    
    return seed_input, purpose if purpose else None

def display_purpose_header(purpose):
    """Display the purpose/question prominently."""
    if purpose:
        print("\n" + "=" * 60)
        print(f"🎯 PURPOSE: {purpose}")
        print("=" * 60)

def search_mode():
    """Enter a loop to search for cards."""
    print("\n🔍 Search for a card by name, number, or alias (e.g., 'The Fool', 's1', 'w10').")
    print("Type 'exit' or 'quit' to return to the main menu.")
    print("-" * 60)
    
    while True:
        query = input("Enter your search query: ").strip()
        
        if query.lower() in ["exit", "quit"]:
            break
            
        results = search_cards(query)
        
        if not results:
            print("No cards found for your query.")
        else:
            for card in results:
                print("\n" + "=" * 60)
                print(f"🃏 {card['name']}")
                if 'number' in card:
                    print(f"Number: {card['number']}")
                print("-" * 60)
                print(f"⬆️ Upright: {card['upright']}")
                print(f"⬇️ Reversed: {card['reversed']}")
                print("=" * 60)

def reading_mode():
    """Perform a tarot reading."""
    # Get user information
    personal_seed, purpose = get_user_info()
    
    if personal_seed:
        print(f"\n🌟 Personal Seed: {personal_seed}")
    else:
        print("\n🎲 Using pure random mode...")
    
    # Display purpose if provided
    display_purpose_header(purpose)
    
    # Show different reading types
    print("\n📋 READING RESULTS:")
    print("=" * 50)
    
    print("\n1. 🃏 Single Card Reading (Daily Guidance):")
    print("-" * 45)
    single_reading = get_reading_summary("single", personal_seed)
    print(single_reading)

    print("\n\n2. 🃏🃏🃏 Three Card Reading (Past-Present-Future):")
    print("-" * 50)
    three_reading = get_reading_summary("three", personal_seed)
    print(three_reading)

    print("\n\n3. ✨ Creative Elements (Inspiration & Insights):")
    print("-" * 50)
    elements = get_random_cards_text(3, personal_seed)
    print("Key themes and energies for reflection:")
    for line in elements.split('\n'):
        if '. ' in line:
            element = line.split(' - ')[1] if ' - ' in line else line
            print(f"  💫 {element}")
    
    # Summary based on purpose
    if purpose:
        print(f"\n🔮 GUIDANCE SUMMARY for '{purpose}':")
        print("-" * 60)
        print("Consider how these cards relate to your specific question.")
        print("Look for patterns, themes, and messages that resonate with your situation.")
        print("Trust your intuition as you interpret these symbols in your context.")

def main():
    print("🔮 Welcome to Tarot Reader CLI!")
    print("=" * 50)
    
    while True:
        print("\nChoose an option:")
        print("1. Search for a card")
        print("2. Shuffle cards for a reading")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ").strip()
        
        if choice == '1':
            search_mode()
        elif choice == '2':
            reading_mode()
            # After a reading, break the loop to exit, or offer to go back to the main menu.
            # For now, let's just print the exit message.
            break
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

    print("\n" + "=" * 60)
    print("✨ Thank you for using Tarot Reader CLI! ✨")
    print("Remember: Tarot is a tool for reflection and self-discovery.")
    print("=" * 60)

if __name__ == "__main__":
    main()