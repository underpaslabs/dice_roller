"""
Main dice roller module for handling multiple dice and game simulations.
"""

from dice import Dice

class DiceRoller:
    """Handles rolling multiple dice and calculating results."""
    
    def __init__(self):
        """Initialize an empty dice collection."""
        self.dice_collection = {}
    
    def add_dice(self, dice_type, count=1):
        """
        Add dice to the collection.
        
        Args:
            dice_type (int or str): Number of sides or dice notation (e.g., 'D6', 'D20')
            count (int): Number of dice to add (default: 1)
        """
        if isinstance(dice_type, str) and dice_type.upper().startswith('D'):
            sides = int(dice_type[1:])
        else:
            sides = int(dice_type)
        
        dice_key = f"D{sides}"
        if dice_key not in self.dice_collection:
            self.dice_collection[dice_key] = []
        
        for _ in range(count):
            self.dice_collection[dice_key].append(Dice(sides))
    
    def roll_all(self):
        """
        Roll all dice in the collection.
        
        Returns:
            dict: Results organized by dice type with individual rolls and totals
        """
        results = {}
        
        for dice_type, dice_list in self.dice_collection.items():
            rolls = [dice.roll() for dice in dice_list]
            results[dice_type] = {
                'rolls': rolls,
                'total': sum(rolls),
                'count': len(rolls)
            }
        
        return results
    
    def roll_single(self, dice_type, count=1):
        """
        Roll specific dice type without adding to collection.
        
        Args:
            dice_type (int or str): Dice type to roll
            count (int): Number of dice to roll
            
        Returns:
            dict: Roll results
        """
        if isinstance(dice_type, str) and dice_type.upper().startswith('D'):
            sides = int(dice_type[1:])
        else:
            sides = int(dice_type)
        
        rolls = [Dice(sides).roll() for _ in range(count)]
        
        return {
            'rolls': rolls,
            'total': sum(rolls),
            'count': count,
            'dice_type': f"D{sides}"
        }
    
    def clear_dice(self):
        """Clear all dice from the collection."""
        self.dice_collection.clear()