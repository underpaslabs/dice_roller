"""
Main script demonstrating the dice rolling system.
"""

from dice_roller import DiceRoller
from game_simulations import GameSimulations

def main():
    """Demonstrate various dice rolling capabilities."""
    
    print("=== Basic Dice Rolling ===")
    roller = DiceRoller()
    
    # Add some dice
    roller.add_dice(6, 2)  # 2d6
    roller.add_dice(20, 1) # 1d20
    roller.add_dice('D4', 3) # 3d4
    
    # Roll all dice
    results = roller.roll_all()
    for dice_type, result in results.items():
        print(f"{dice_type}: {result['rolls']} = {result['total']}")
    
    print("\n=== Single Roll ===")
    single_roll = roller.roll_single(8, 2)
    print(f"2d8: {single_roll['rolls']} = {single_roll['total']}")
    
    print("\n=== Game Simulations ===")
    
    # D&D Ability Roll
    ability_roll = GameSimulations.dnd_ability_roll()
    print(f"D&D Ability: {ability_roll['all_rolls']} -> {ability_roll['final_rolls']} = {ability_roll['total']} (dropped {ability_roll['dropped']})")
    
    # D&D Attack Roll with Advantage
    attack_roll = GameSimulations.dnd_attack_roll(advantage=True)
    print(f"D&D Attack (Advantage): {attack_roll['rolls']} -> {attack_roll['final_roll']}")
    
    # Shadowrun
    shadowrun_roll = GameSimulations.shadowrun_pool(5)
    print(f"Shadowrun (5 dice): {shadowrun_roll['rolls']} -> {shadowrun_roll['successes']} successes")
    
    # Warhammer
    warhammer_roll = GameSimulations.warhammer_roll(4, 4)
    print(f"Warhammer (4+ on 4 dice): {warhammer_roll['rolls']} -> {warhammer_roll['successes']} successes")

if __name__ == "__main__":
    main()