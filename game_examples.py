"""
Example game simulations using the dice roller.
"""

from dice_roller import DiceRoller

class GameExamples:
    """Example game simulations using dice rolls."""
    
    def __init__(self):
        self.roller = DiceRoller()
    
    def dnd_ability_roll(self):
        """
        Simulate D&D ability score roll (4d6 drop lowest).
        
        Returns:
            dict: Roll results
        """
        print("Rolling D&D Ability Score (4d6 drop lowest):")
        roll_result = self.roller.roll_multiple('d6', 4)
        results = sorted(roll_result['results'])
        dropped = results[0]
        final_results = results[1:]
        total = sum(final_results)
        
        return {
            'all_rolls': results,
            'dropped_lowest': dropped,
            'final_rolls': final_results,
            'ability_score': total
        }
    
    def advantage_roll(self):
        """
        Simulate D&D advantage roll (roll 2d20, take higher).
        
        Returns:
            dict: Roll results
        """
        print("Rolling with Advantage (2d20 take higher):")
        roll_result = self.roller.roll_multiple('d20', 2)
        results = roll_result['results']
        higher = max(results)
        
        return {
            'rolls': results,
            'result': higher,
            'type': 'advantage'
        }
    
    def disadvantage_roll(self):
        """
        Simulate D&D disadvantage roll (roll 2d20, take lower).
        
        Returns:
            dict: Roll results
        """
        print("Rolling with Disadvantage (2d20 take lower):")
        roll_result = self.roller.roll_multiple('d20', 2)
        results = roll_result['results']
        lower = min(results)
        
        return {
            'rolls': results,
            'result': lower,
            'type': 'disadvantage'
        }
    
    def damage_roll(self, dice_type='d6', count=2, modifier=0):
        """
        Simulate damage roll with modifier.
        
        Args:
            dice_type (str): Type of damage dice
            count (int): Number of dice
            modifier (int): Damage modifier
            
        Returns:
            dict: Damage roll results
        """
        print(f"Damage Roll: {count}{dice_type} + {modifier}")
        roll_result = self.roller.roll_multiple(dice_type, count)
        total_damage = roll_result['total'] + modifier
        
        return {
            'dice_rolls': roll_result['results'],
            'dice_total': roll_result['total'],
            'modifier': modifier,
            'total_damage': total_damage
        }

def run_examples():
    """Run all game examples."""
    examples = GameExamples()
    
    # D&D Ability Roll
    ability_result = examples.dnd_ability_roll()
    print(f"Rolls: {ability_result['all_rolls']}")
    print(f"Dropped: {ability_result['dropped_lowest']}")
    print(f"Final: {ability_result['final_rolls']}")
    print(f"Ability Score: {ability_result['ability_score']}\n")
    
    # Advantage Roll
    advantage_result = examples.advantage_roll()
    print(f"Rolls: {advantage_result['rolls']}")
    print(f"Result: {advantage_result['result']}\n")
    
    # Disadvantage Roll
    disadvantage_result = examples.disadvantage_roll()
    print(f"Rolls: {disadvantage_result['rolls']}")
    print(f"Result: {disadvantage_result['result']}\n")
    
    # Damage Roll
    damage_result = examples.damage_roll('d8', 3, 5)
    print(f"Dice Rolls: {damage_result['dice_rolls']}")
    print(f"Dice Total: {damage_result['dice_total']}")
    print(f"Modifier: +{damage_result['modifier']}")
    print(f"Total Damage: {damage_result['total_damage']}")

if __name__ == "__main__":
    run_examples()