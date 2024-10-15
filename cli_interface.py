"""
Command-line interface for the dice rolling system.
"""

import argparse
from dice import DiceRoller
from game_presets import GamePresets

class DiceCLI:
    """Command-line interface for dice rolling."""
    
    def __init__(self):
        self.roller = DiceRoller()
    
    def print_result(self, result, description="Roll result"):
        """Print roll results in a formatted way."""
        print(f"\n=== {description} ===")
        
        if isinstance(result, dict):
            for key, value in result.items():
                if isinstance(value, list):
                    print(f"{key}: {value} (sum: {sum(value)})")
                else:
                    print(f"{key}: {value}")
        else:
            print(f"Result: {result}")
        print()
    
    def handle_single_roll(self, sides):
        """Handle single die roll."""
        result = self.roller.roll_single(sides)
        self.print_result(result, f"d{sides} Roll")
    
    def handle_multiple_roll(self, dice_args):
        """Handle multiple dice roll."""
        config = {}
        for arg in dice_args:
            try:
                count, sides = map(int, arg.split('d'))
                config[f'd{sides}'] = count
            except ValueError:
                print(f"Invalid dice format: {arg}. Use format like '2d6'")
                return
        
        result = self.roller.roll_multiple(config)
        self.print_result(result, "Multiple Dice Roll")
    
    def handle_game_preset(self, game, *args):
        """Handle game-specific preset rolls."""
        game = game.lower()
        
        if game == 'dnd-ability':
            result = GamePresets.dnd_ability_roll()
            self.print_result(result, "D&D Ability Roll (4d6 drop lowest)")
        
        elif game == 'dnd-attack':
            advantage = 'advantage' in args
            disadvantage = 'disadvantage' in args
            result = GamePresets.dnd_attack_roll(advantage, disadvantage)
            self.print_result(result, "D&D Attack Roll")
        
        elif game == 'shadowrun':
            if not args:
                print("Please specify dice pool: shadowrun <dice_pool>")
                return
            try:
                dice_pool = int(args[0])
                result = GamePresets.shadowrun_skill_test(dice_pool)
                self.print_result(result, f"Shadowrun Skill Test ({dice_pool}d6)")
            except ValueError:
                print("Dice pool must be a number")
        
        elif game == 'warhammer':
            if len(args) < 3:
                print("Usage: warhammer <attacks> <weapon_strength> <target_toughness>")
                return
            try:
                attacks, weapon_str, toughness = map(int, args[:3])
                result = GamePresets.warhammer_attack(attacks, weapon_str, toughness)
                self.print_result(result, "Warhammer 40k Attack")
            except ValueError:
                print("All parameters must be numbers")
        
        elif game == 'fate':
            result = GamePresets.fate_dice_roll()
            self.print_result(result, "FATE Dice Roll")
        
        else:
            print(f"Unknown game preset: {game}")
            print("Available presets: dnd-ability, dnd-attack, shadowrun, warhammer, fate")
    
    def show_history(self, limit=10):
        """Show roll history."""
        history = self.roller.get_history(limit)
        if not history:
            print("No roll history")
            return
        
        print(f"\n=== Last {len(history)} Rolls ===")
        for i, roll in enumerate(history, 1):
            print(f"{i}. {roll['type']}: {roll['result']}")
        print()
    
    def run(self):
        """Main CLI loop."""
        parser = argparse.ArgumentParser(description='Dice Rolling Simulator')
        parser.add_argument('--single', type=int, help='Roll a single die (e.g., --single 20)')
        parser.add_argument('--multiple', nargs='+', help='Roll multiple dice (e.g., --multiple 2d6 1d20)')
        parser.add_argument('--game', nargs='+', help='Use game preset (e.g., --game dnd-ability)')
        parser.add_argument('--history', type=int, nargs='?', const=10, 
                          help='Show roll history (optional: number of rolls to show)')
        
        args = parser.parse_args()
        
        if args.single:
            self.handle_single_roll(args.single)
        
        elif args.multiple:
            self.handle_multiple_roll(args.multiple)
        
        elif args.game:
            self.handle_game_preset(args.game[0], *args.game[1:])
        
        elif args.history:
            self.show_history(args.history)
        
        else:
            # Interactive mode
            self.interactive_mode()
    
    def interactive_mode(self):
        """Run in interactive mode."""
        print("=== Dice Rolling Simulator ===")
        print("Commands:")
        print("  single <sides>    - Roll a single die")
        print("  multiple <dice>   - Roll multiple dice (e.g., 2d6 1d20)")
        print("  game <preset>     - Use game preset")
        print("  history [limit]   - Show roll history")
        print("  clear             - Clear history")
        print("  quit              - Exit")
        print()
        
        while True:
            try:
                command = input("dice> ").strip().split()
                if not command:
                    continue
                
                cmd = command[0].lower()
                
                if cmd == 'quit':
                    break
                elif cmd == 'single' and len(command) > 1:
                    self.handle_single_roll(int(command[1]))
                elif cmd == 'multiple' and len(command) > 1:
                    self.handle_multiple_roll(command[1:])
                elif cmd == 'game' and len(command) > 1:
                    self.handle_game_preset(command[1], *command[2:])
                elif cmd == 'history':
                    limit = int(command[1]) if len(command) > 1 else 10
                    self.show_history(limit)
                elif cmd == 'clear':
                    self.roller.clear_history()
                    print("History cleared")
                else:
                    print("Unknown command")
                    
            except (ValueError, IndexError):
                print("Invalid command syntax")
            except KeyboardInterrupt:
                print("\nGoodbye!")
                break

if __name__ == "__main__":
    cli = DiceCLI()
    cli.run()