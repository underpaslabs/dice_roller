"""
Main script for interactive dice rolling.
"""

from dice_roller import DiceRoller
from game_examples import GameExamples

def display_menu():
    """Display the main menu options."""
    print("\n=== Dice Roller ===")
    print("1. Roll single dice")
    print("2. Roll multiple dice")
    print("3. Roll custom dice")
    print("4. D&D Ability Roll (4d6 drop lowest)")
    print("5. Advantage/Disadvantage Roll")
    print("6. Damage Roll")
    print("7. Show available dice")
    print("8. Exit")
    print("===================")

def main():
    """Main interactive dice rolling program."""
    roller = DiceRoller()
    examples = GameExamples()
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-8): ").strip()
        
        if choice == '1':
            # Roll single dice
            dice_type = input("Enter dice type (e.g., d6, d20): ").strip().lower()
            try:
                dice_type, result = roller.roll_single(dice_type)
                print(f"Rolled {dice_type}: {result}")
            except ValueError as e:
                print(f"Error: {e}")
        
        elif choice == '2':
            # Roll multiple dice
            dice_type = input("Enter dice type (e.g., d6, d20): ").strip().lower()
            try:
                count = int(input("Enter number of dice: "))
                result = roller.roll_multiple(dice_type, count)
                print(f"Rolled {count}{dice_type}: {result['results']}")
                print(f"Total: {result['total']}")
            except (ValueError, TypeError) as e:
                print(f"Error: {e}")
        
        elif choice == '3':
            # Roll custom dice
            try:
                sides = int(input("Enter number of sides: "))
                count = int(input("Enter number of dice: "))
                result = roller.roll_custom_dice(sides, count)
                print(f"Rolled {count}d{sides}: {result['results']}")
                print(f"Total: {result['total']}")
            except (ValueError, TypeError) as e:
                print(f"Error: {e}")
        
        elif choice == '4':
            # D&D Ability Roll
            result = examples.dnd_ability_roll()
            print(f"Rolls: {result['all_rolls']}")
            print(f"Dropped lowest: {result['dropped_lowest']}")
            print(f"Final rolls: {result['final_rolls']}")
            print(f"Ability Score: {result['ability_score']}")
        
        elif choice == '5':
            # Advantage/Disadvantage
            adv_choice = input("(A)dvantage or (D)isadvantage? ").strip().upper()
            if adv_choice == 'A':
                result = examples.advantage_roll()
            elif adv_choice == 'D':
                result = examples.disadvantage_roll()
            else:
                print("Invalid choice")
                continue
            print(f"Rolls: {result['rolls']}")
            print(f"Result: {result['result']}")
        
        elif choice == '6':
            # Damage Roll
            try:
                dice_type = input("Enter damage dice (e.g., d6, d8): ").strip().lower()
                count = int(input("Enter number of dice: "))
                modifier = int(input("Enter damage modifier: "))
                result = examples.damage_roll(dice_type, count, modifier)
                print(f"Dice Rolls: {result['dice_rolls']}")
                print(f"Dice Total: {result['dice_total']}")
                print(f"Modifier: +{result['modifier']}")
                print(f"Total Damage: {result['total_damage']}")
            except (ValueError, TypeError) as e:
                print(f"Error: {e}")
        
        elif choice == '7':
            # Show available dice
            dice_list = roller.get_available_dice()
            print("Available dice types:")
            for dice in dice_list:
                print(f"  - {dice}")
        
        elif choice == '8':
            print("Thanks for using Dice Roller!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()