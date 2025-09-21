"""
Tarot deck data containing all 78 cards with upright and reversed meanings.
"""

MAJOR_ARCANA = [
    {
        "name": "The Fool",
        "number": 0,
        "upright": "New beginnings, innocence, spontaneity, free spirit",
        "reversed": "Recklessness, lack of direction, poor judgment, folly"
    },
    {
        "name": "The Magician",
        "number": 1,
        "upright": "Willpower, manifestation, resourcefulness, power",
        "reversed": "Manipulation, poor planning, untapped talents"
    },
    {
        "name": "The High Priestess",
        "number": 2,
        "upright": "Intuition, sacred knowledge, divine feminine, subconscious",
        "reversed": "Secrets, disconnected from intuition, withdrawal"
    },
    {
        "name": "The Empress",
        "number": 3,
        "upright": "Fertility, femininity, beauty, nature, abundance",
        "reversed": "Creative block, dependence on others"
    },
    {
        "name": "The Emperor",
        "number": 4,
        "upright": "Authority, establishment, structure, father figure",
        "reversed": "Domination, excessive control, lack of discipline"
    },
    {
        "name": "The Hierophant",
        "number": 5,
        "upright": "Spiritual wisdom, religious beliefs, conformity, tradition",
        "reversed": "Personal beliefs, freedom, challenging the status quo"
    },
    {
        "name": "The Lovers",
        "number": 6,
        "upright": "Love, harmony, relationships, values alignment",
        "reversed": "Self-love, disharmony, imbalance, misalignment"
    },
    {
        "name": "The Chariot",
        "number": 7,
        "upright": "Control, willpower, success, determination",
        "reversed": "Self-discipline, opposition, lack of direction"
    },
    {
        "name": "Strength",
        "number": 8,
        "upright": "Strength, courage, persuasion, influence, compassion",
        "reversed": "Self doubt, low energy, raw emotion"
    },
    {
        "name": "The Hermit",
        "number": 9,
        "upright": "Soul searching, introspection, being alone, inner guidance",
        "reversed": "Isolation, loneliness, withdrawal"
    },
    {
        "name": "Wheel of Fortune",
        "number": 10,
        "upright": "Good luck, karma, life cycles, destiny, a turning point",
        "reversed": "Bad luck, lack of control, clinging to control"
    },
    {
        "name": "Justice",
        "number": 11,
        "upright": "Justice, fairness, truth, cause and effect, law",
        "reversed": "Unfairness, lack of accountability, dishonesty"
    },
    {
        "name": "The Hanged Man",
        "number": 12,
        "upright": "Suspension, restriction, letting go, sacrifice",
        "reversed": "Delays, resistance, stalling, indecision"
    },
    {
        "name": "Death",
        "number": 13,
        "upright": "Endings, beginnings, change, transformation, transition",
        "reversed": "Resistance to change, personal transformation, inner purging"
    },
    {
        "name": "Temperance",
        "number": 14,
        "upright": "Balance, moderation, patience, purpose",
        "reversed": "Imbalance, excess, self-healing, re-alignment"
    },
    {
        "name": "The Devil",
        "number": 15,
        "upright": "Bondage, addiction, sexuality, materialism",
        "reversed": "Releasing limiting beliefs, exploring dark thoughts, detachment"
    },
    {
        "name": "The Tower",
        "number": 16,
        "upright": "Sudden change, upheaval, chaos, revelation, awakening",
        "reversed": "Personal transformation, fear of change, averting disaster"
    },
    {
        "name": "The Star",
        "number": 17,
        "upright": "Hope, faith, purpose, renewal, spirituality",
        "reversed": "Lack of faith, despair, self-trust, disconnection"
    },
    {
        "name": "The Moon",
        "number": 18,
        "upright": "Illusion, fear, anxiety, subconscious, intuition",
        "reversed": "Release of fear, repressed emotion, inner confusion"
    },
    {
        "name": "The Sun",
        "number": 19,
        "upright": "Positivity, fun, warmth, success, vitality",
        "reversed": "Inner child, feeling down, overly optimistic"
    },
    {
        "name": "Judgement",
        "number": 20,
        "upright": "Judgement, rebirth, inner calling, absolution",
        "reversed": "Self-doubt, inner critic, ignoring the call"
    },
    {
        "name": "The World",
        "number": 21,
        "upright": "Completion, integration, accomplishment, travel",
        "reversed": "Seeking personal closure, short-cut to success"
    }
]

MINOR_ARCANA = {
    "Wands": [
        {
            "name": "Ace of Wands",
            "upright": "Inspiration, new opportunities, growth",
            "reversed": "An emerging idea, lack of direction, distractions"
        },
        {
            "name": "Two of Wands",
            "upright": "Future planning, making decisions, leaving comfort zone",
            "reversed": "Fear of unknown, lack of planning, bad decisions"
        },
        {
            "name": "Three of Wands",
            "upright": "Expansion, foresight, overseas opportunities",
            "reversed": "Playing small, lack of foresight, unexpected delays"
        },
        {
            "name": "Four of Wands",
            "upright": "Celebration, joy, harmony, relaxation, homecoming",
            "reversed": "Personal celebration, inner harmony, conflict with others"
        },
        {
            "name": "Five of Wands",
            "upright": "Conflict, disagreements, competition, tension",
            "reversed": "Inner conflict, conflict avoidance, tension release"
        },
        {
            "name": "Six of Wands",
            "upright": "Success, public recognition, progress, self-confidence",
            "reversed": "Private achievement, personal definition of success, fall from grace"
        },
        {
            "name": "Seven of Wands",
            "upright": "Challenge, competition, protection, perseverance",
            "reversed": "Exhaustion, giving up, overwhelmed"
        },
        {
            "name": "Eight of Wands",
            "upright": "Swiftness, speed, progress, movement, quick decisions",
            "reversed": "Delays, frustration, resisting change, internal alignment"
        },
        {
            "name": "Nine of Wands",
            "upright": "Resilience, courage, persistence, test of faith, boundaries",
            "reversed": "Inner resources, struggle, overwhelm, defensive, paranoia"
        },
        {
            "name": "Ten of Wands",
            "upright": "Burden, extra responsibility, hard work, completion",
            "reversed": "Doing it all, carrying the burden, delegation, release"
        },
        {
            "name": "Page of Wands",
            "upright": "Inspiration, ideas, discovery, limitless potential, free spirit",
            "reversed": "Newly-formed ideas, redirecting energy, self-limiting beliefs"
        },
        {
            "name": "Knight of Wands",
            "upright": "Energy, passion, inspired action, adventure, impulsiveness",
            "reversed": "Passion project, haste, scattered energy, delays, frustration"
        },
        {
            "name": "Queen of Wands",
            "upright": "Courage, confidence, independence, social butterfly, determination",
            "reversed": "Self-respect, self-confidence, introverted, re-establish sense of self"
        },
        {
            "name": "King of Wands",
            "upright": "Natural leader, vision, entrepreneur, honour",
            "reversed": "Impulsiveness, haste, ruthless, high expectations"
        }
    ],
    "Cups": [
        {
            "name": "Ace of Cups",
            "upright": "Love, new relationships, compassion, creativity",
            "reversed": "Self-love, intuition, repressed emotions"
        },
        {
            "name": "Two of Cups",
            "upright": "Unified love, partnership, mutual attraction",
            "reversed": "Self-love, break-ups, disharmony, distrust"
        },
        {
            "name": "Three of Cups",
            "upright": "Celebration, friendship, creativity, collaborations",
            "reversed": "Independence, alone time, hardcore partying, 'three's a crowd'"
        },
        {
            "name": "Four of Cups",
            "upright": "Meditation, contemplation, apathy, reevaluation",
            "reversed": "Retreat, withdrawal, checking in for answers"
        },
        {
            "name": "Five of Cups",
            "upright": "Regret, failure, disappointment, pessimism",
            "reversed": "Personal setbacks, self-forgiveness, moving on"
        },
        {
            "name": "Six of Cups",
            "upright": "Revisiting the past, childhood memories, innocence, joy",
            "reversed": "Living in the past, forgiveness, lacking playfulness"
        },
        {
            "name": "Seven of Cups",
            "upright": "Opportunities, choices, wishful thinking, illusion",
            "reversed": "Alignment, personal values, overwhelmed by choices"
        },
        {
            "name": "Eight of Cups",
            "upright": "Disappointment, abandonment, withdrawal, escapism",
            "reversed": "Trying one more time, indecision, aimless drifting"
        },
        {
            "name": "Nine of Cups",
            "upright": "Contentment, satisfaction, gratitude, wish come true",
            "reversed": "Inner happiness, materialism, dissatisfaction, indulgence"
        },
        {
            "name": "Ten of Cups",
            "upright": "Divine love, blissful relationships, harmony, alignment",
            "reversed": "Disconnection, misaligned values, struggling relationships"
        },
        {
            "name": "Page of Cups",
            "upright": "Creative opportunities, intuitive messages, curiosity, possibility",
            "reversed": "New ideas, doubting intuition, creative blocks, emotional immaturity"
        },
        {
            "name": "Knight of Cups",
            "upright": "Creativity, romance, bringing or receiving a message, investment",
            "reversed": "Moodiness, disappointment, withdrawing"
        },
        {
            "name": "Queen of Cups",
            "upright": "Compassionate, caring, emotionally stable, intuitive, in flow",
            "reversed": "Inner compassion, self-care, co-dependency, martyrdom"
        },
        {
            "name": "King of Cups",
            "upright": "Emotionally balanced, compassionate, diplomatic",
            "reversed": "Self-compassion, inner feelings, moodiness, emotionally manipulative"
        }
    ],
    "Swords": [
        {
            "name": "Ace of Swords",
            "upright": "Breakthroughs, new ideas, mental clarity, success",
            "reversed": "Inner clarity, re-thinking an idea, clouded judgement"
        },
        {
            "name": "Two of Swords",
            "upright": "Difficult decisions, weighing up options, an impasse, avoidance",
            "reversed": "Indecision, confusion, information overload, stalemate"
        },
        {
            "name": "Three of Swords",
            "upright": "Heartbreak, emotional pain, sorrow, grief, hurt",
            "reversed": "Negative self-talk, releasing pain, optimism, forgiveness"
        },
        {
            "name": "Four of Swords",
            "upright": "Rest, relaxation, meditation, contemplation, recuperation",
            "reversed": "Exhaustion, burn-out, deep contemplation, stagnation"
        },
        {
            "name": "Five of Swords",
            "upright": "Conflict, disagreements, competition, defeat, winning at all costs",
            "reversed": "Reconciliation, making amends, past resentment"
        },
        {
            "name": "Six of Swords",
            "upright": "Transition, change, rite of passage, releasing baggage",
            "reversed": "Personal transition, resistance to change, unfinished business"
        },
        {
            "name": "Seven of Swords",
            "upright": "Betrayal, deception, getting away with something, acting strategically",
            "reversed": "Imposter syndrome, self-deceit, keeping secrets"
        },
        {
            "name": "Eight of Swords",
            "upright": "Negative thoughts, self-imposed restriction, imprisonment, victim mentality",
            "reversed": "Self-limiting beliefs, inner critic, releasing negative thoughts, open to new perspectives"
        },
        {
            "name": "Nine of Swords",
            "upright": "Anxiety, worry, fear, depression, nightmares",
            "reversed": "Inner turmoil, deep-seated fears, secrets, releasing worry"
        },
        {
            "name": "Ten of Swords",
            "upright": "Painful endings, deep wounds, betrayal, loss, crisis",
            "reversed": "Recovery, regeneration, resisting an inevitable end"
        },
        {
            "name": "Page of Swords",
            "upright": "New ideas, curiosity, thirst for knowledge, new ways of communicating",
            "reversed": "Self-expression, all talk and no action, haphazard action, haste"
        },
        {
            "name": "Knight of Swords",
            "upright": "Ambitious, action-oriented, driven to succeed, fast-thinking",
            "reversed": "Restless, unfocused, impulsive, burn-out"
        },
        {
            "name": "Queen of Swords",
            "upright": "Independent, unbiased judgement, clear boundaries, direct communication",
            "reversed": "Overly-emotional, easily influenced, bitchy, cold-hearted"
        },
        {
            "name": "King of Swords",
            "upright": "Mental clarity, intellectual power, authority, truth",
            "reversed": "Quiet power, inner truth, misuse of power, manipulation"
        }
    ],
    "Pentacles": [
        {
            "name": "Ace of Pentacles",
            "upright": "A new financial or career opportunity, manifestation, abundance",
            "reversed": "Lost opportunity, lack of planning and foresight"
        },
        {
            "name": "Two of Pentacles",
            "upright": "Multiple priorities, time management, prioritisation, adaptability",
            "reversed": "Over-committed, disorganisation, reprioritisation"
        },
        {
            "name": "Three of Pentacles",
            "upright": "Collaboration, learning, implementation",
            "reversed": "Disharmony, misalignment, working alone"
        },
        {
            "name": "Four of Pentacles",
            "upright": "Saving money, security, conservatism, scarcity, control",
            "reversed": "Over-spending, greed, self-protection"
        },
        {
            "name": "Five of Pentacles",
            "upright": "Financial loss, poverty, lack mindset, isolation, worry",
            "reversed": "Recovery from financial loss, spiritual poverty"
        },
        {
            "name": "Six of Pentacles",
            "upright": "Giving, receiving, sharing wealth, generosity, charity",
            "reversed": "Self-care, unpaid debts, one-sided charity"
        },
        {
            "name": "Seven of Pentacles",
            "upright": "Harvest, rewards, results, growth, progress, perseverance, patience",
            "reversed": "Lack of rewards, impatience, lack of growth"
        },
        {
            "name": "Eight of Pentacles",
            "upright": "Apprenticeship, repetitive tasks, mastery, skill development",
            "reversed": "Perfectionism, misdirected activity, skill development"
        },
        {
            "name": "Nine of Pentacles",
            "upright": "Abundance, luxury, self-sufficiency, financial independence",
            "reversed": "Self-worth, over-investment in work, hustling"
        },
        {
            "name": "Ten of Pentacles",
            "upright": "Wealth, financial security, family, long-term success, contribution",
            "reversed": "The dark side of wealth, financial failure or loss"
        },
        {
            "name": "Page of Pentacles",
            "upright": "Manifestation, financial opportunity, skill development",
            "reversed": "Lack of progress, procrastination, learn from failure"
        },
        {
            "name": "Knight of Pentacles",
            "upright": "Hard work, productivity, routine, conservatism",
            "reversed": "Self-discipline, boredom, frustration, obstacles"
        },
        {
            "name": "Queen of Pentacles",
            "upright": "Nurturing, practical, providing financially, a working parent",
            "reversed": "Financial independence, self-care, work-home conflict"
        },
        {
            "name": "King of Pentacles",
            "upright": "Financial abundance, business, leadership, security, discipline, abundance",
            "reversed": "Financially inept, obsessed with wealth and status, stubborn"
        }
    ]
}

def get_all_cards():
    """Return a list of all 78 tarot cards."""
    all_cards = []

    # Add Major Arcana
    all_cards.extend(MAJOR_ARCANA)

    # Add Minor Arcana
    for suit, cards in MINOR_ARCANA.items():
        all_cards.extend(cards)

    return all_cards