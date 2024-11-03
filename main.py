"""
Main script to demonstrate dice rolling functionality
"""

from dice_roller import DiceRoller
from game_simulations import GameSimulations
from dice import D4, D6, D8, D10, D12, D20, D100

def main():
    """Demonstrate various dice rolling functionalities"""
    
    print("=== DICE ROLLING SIMULATOR ===\n")
    
    # Basic dice rolls
    print("1. BASIC DICE ROLLS")
    print(f"Single D20 roll: {D20.roll()}")
    print(f"Single D6 roll: {D6.roll()}")
    
    # Multiple dice
    multi_result = DiceRoller.roll_multiple([D6, D6, D6])  # 3d6
    print(f"\n3d6 roll: {multi_result['rolls']} = {multi_result['total']}")
    
    # D&D ability score
    ability_result = DiceRoller.roll_dnd_ability_score()
    print(f"\nD&D Ability Score: {ability_result['rolls']}")
    print(f"Kept: {ability_result['kept_rolls']}, Dropped: {ability_result['dropped_roll']}")
    print(f"Total: {ability_result['total']}")
    
    # Advantage/Disadvantage
    adv_result = DiceRoller.roll_advantage()
    print(f"\nAdvantage roll: {adv_result['rolls']} -> {adv_result['result']}")
    
    # Fudge dice
    fudge_result = DiceRoller.roll_fudge_dice()
    print(f"\nFudge dice: {fudge_result['rolls']} = {fudge_result['total']}")
    
    # Game simulations
    print("\n2. GAME SIMULATIONS")
    
    # D&D Attack
    attack_result = GameSimulations.simulate_dnd_attack()
    print(f"\nD&D Attack: Roll {attack_result['attack_roll']} + {attack_result['bonus']} = {attack_result['total_attack']}")
    print(f"vs AC {attack_result['target_ac']}: {'HIT!' if attack_result['hit'] else 'MISS'}")
    if attack_result['critical_hit']:
        print("CRITICAL HIT!")
    if attack_result['critical_miss']:
        print("CRITICAL MISS!")
    
    # Yahtzee
    yahtzee_result = GameSimulations.simulate_yahtzee_roll()
    print(f"\nYahtzee roll: {yahtzee_result['rolls']} = {yahtzee_result['total']}")
    if yahtzee_result['is_yahtzee']:
        print("YAHTZEE!")
    elif yahtzee_result['is_full_house']:
        print("Full House!")
    elif yahtzee_result['is_large_straight']:
        print("Large Straight!")
    elif yahtzee_result['is_small_straight']:
        print("Small Straight!")
    
    # Shadowrun
    shadowrun_result = GameSimulations.simulate_shadowrun_test()
    print(f"\nShadowrun test: {shadowrun_result['rolls']}")
    print(f"Successes: {shadowrun_result['successes']}/{shadowrun_result['threshold']} - {'PASS' if shadowrun_result['passed'] else 'FAIL'}")
    if shadowrun_result['glitch']:
        print("GLITCH!")
    if shadowrun_result['critical_glitch']:
        print("CRITICAL GLITCH!")

if __name__ == "__main__":
    main()