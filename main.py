"""
Main entry point for the dice rolling application
"""

import sys
from roller import DiceRoller, GameSimulator

def main():
    """Main interactive dice rolling application"""
    roller = DiceRoller()
    
    print("🎲 Dice Rolling Simulator 🎲")
    print("Commands: roll, game, history, clear, quit")
    print("Roll examples: 'roll d20', 'roll 3d6', 'roll 2d8+5'")
    print("Game examples: 'game dnd', 'game yahtzee', 'game shadowrun'")
    
    while True:
        try:
            command = input("\n> ").strip().lower()
            
            if command in ['quit', 'exit', 'q']:
                print("Thanks for rolling!")
                break
            
            elif command == 'history':
                history = roller.get_history()
                if not history:
                    print("No rolls in history")
                else:
                    print(f"Roll History ({len(history)} rolls):")
                    for i, roll in enumerate(history, 1):
                        if roll['type'] == 'single':
                            print(f"  {i}. d{roll['sides']}: {roll['result']}")
                        else:
                            print(f"  {i}. {roll['count']}d{roll.get('sides', roll.get('dice_type', '?'))}: "
                                  f"{roll['results']} (Total: {roll['total']})")
            
            elif command == 'clear':
                roller.clear_history()
                print("History cleared")
            
            elif command.startswith('roll '):
                parts = command[5:].strip()
                handle_roll_command(roller, parts)
            
            elif command.startswith('game '):
                game_type = command[5:].strip()
                handle_game_command(game_type)
            
            elif command == 'help':
                print("Available commands:")
                print("  roll [dice] - Roll dice (e.g., 'roll d20', 'roll 3d6')")
                print("  game [type] - Game simulation (dnd, yahtzee, shadowrun)")
                print("  history - Show roll history")
                print("  clear - Clear history")
                print("  quit - Exit program")
            
            else:
                print("Unknown command. Type 'help' for available commands.")
                
        except (ValueError, IndexError) as e:
            print(f"Error: {e}")
        except KeyboardInterrupt:
            print("\nThanks for rolling!")
            break
        except Exception as e:
            print(f"Unexpected error: {e}")

def handle_roll_command(roller: DiceRoller, dice_spec: str):
    """Handle roll commands"""
    if dice_spec.startswith('d'):
        # Standard dice like d20, 2d6, etc.
        if 'd' in dice_spec and dice_spec.count('d') == 1:
            parts = dice_spec.split('d')
            if len(parts) == 2:
                count = int(parts[0]) if parts[0] else 1
                sides = parts[1]
                results = roller.roll_standard(f"d{sides}", count)
                total = sum(results)
                print(f"Rolled {dice_spec}: {results} = {total}")
            else:
                raise ValueError("Invalid dice specification")
        else:
            # Single standard die
            results = roller.roll_standard(dice_spec)
            print(f"Rolled {dice_spec}: {results[0]}")
    else:
        # Custom dice like 3d6
        if 'd' in dice_spec:
            count, sides = map(int, dice_spec.split('d'))
            results = roller.roll_multiple(sides, count)
            total = sum(results)
            print(f"Rolled {dice_spec}: {results} = {total}")
        else:
            # Single custom die
            sides = int(dice_spec)
            result = roller.roll_single(sides)
            print(f"Rolled d{sides}: {result}")

def handle_game_command(game_type: str):
    """Handle game simulation commands"""
    if game_type == 'dnd':
        result = GameSimulator.dnd_ability_roll()
        print(f"D&D Ability Roll: {result['rolls']} "
              f"(dropped {result['dropped']}) = {result['total']}")
    
    elif game_type == 'yahtzee':
        result = GameSimulator.yahtzee_roll()
        print(f"Yahtzee roll: {result}")
    
    elif game_type == 'shadowrun':
        # Simulate a typical shadowrun roll
        result = GameSimulator.shadowrun_roll(6, 5)
        print(f"Shadowrun roll: {result['rolls']}")
        print(f"Successes: {result['successes']}")
        if result['is_glitch']:
            print("⚠️  GLITCH!")
        if result['critical_glitch']:
            print("💥 CRITICAL GLITCH!")
    
    else:
        print(f"Unknown game type: {game_type}")
        print("Available games: dnd, yahtzee, shadowrun")

if __name__ == "__main__":
    main()