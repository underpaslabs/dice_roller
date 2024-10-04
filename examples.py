"""
Example usage of the dice rolling system
"""

from roller import DiceRoller, GameSimulator

def demonstrate_basic_rolls():
    """Demonstrate basic dice rolling functionality"""
    roller = DiceRoller()
    
    print("=== Basic Dice Rolls ===")
    
    # Single die roll
    result = roller.roll_single(20)
    print(f"Single d20 roll: {result}")
    
    # Multiple dice
    results = roller.roll_multiple(6, 3)
    print(f"3d6 roll: {results} (Total: {sum(results)})")
    
    # Standard RPG dice
    d20_result = roller.roll_standard('d20')
    print(f"d20 roll: {d20_result[0]}")
    
    # Multiple standard dice
    attack_roll = roller.roll_standard('d20', 2)
    print(f"2d20 attack roll: {attack_roll}")

def demonstrate_game_simulations():
    """Demonstrate game-specific simulations"""
    print("\n=== Game Simulations ===")
    
    # D&D ability score
    ability_score = GameSimulator.dnd_ability_roll()
    print(f"D&D Ability Roll: {ability_score['rolls']} "
          f"(dropped {ability_score['dropped']}) = {ability_score['total']}")
    
    # Yahtzee roll
    yahtzee = GameSimulator.yahtzee_roll()
    print(f"Yahtzee roll: {yahtzee}")
    
    # Shadowrun roll
    shadowrun = GameSimulator.shadowrun_roll(8, 5)
    print(f"Shadowrun roll (8 dice): {shadowrun['rolls']}")
    print(f"Successes: {shadowrun['successes']}, "
          f"Glitch: {shadowrun['is_glitch']}")

def demonstrate_advanced_features():
    """Demonstrate advanced features"""
    roller = DiceRoller()
    
    print("\n=== Advanced Features ===")
    
    # Multiple rolls with history
    for _ in range(3):
        roller.roll_standard('d6')
    
    history = roller.get_history()
    print(f"Roll history: {len(history)} rolls")
    for i, roll in enumerate(history, 1):
        print(f"  Roll {i}: {roll}")

if __name__ == "__main__":
    demonstrate_basic_rolls()
    demonstrate_game_simulations()
    demonstrate_advanced_features()