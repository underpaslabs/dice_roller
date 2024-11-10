"""
Main dice roller module for simulating multiple dice rolls.
"""

from dice import Dice

class DiceRoller:
    """A class to handle rolling multiple dice of various types."""
    
    def __init__(self):
        """Initialize the dice roller with common dice types."""
        self.dice_types = {
            'd4': Dice(4),
            'd6': Dice(6),
            'd8': Dice(8),
            'd10': Dice(10),
            'd12': Dice(12),
            'd20': Dice(20),
            'd100': Dice(100)
        }
    
    def roll_single(self, dice_type='d6'):
        """
        Roll a single dice of specified type.
        
        Args:
            dice_type (str): Type of dice (e.g., 'd6', 'd20')
            
        Returns:
            tuple: (dice_type, result)
        """
        if dice_type not in self.dice_types:
            raise ValueError(f"Unknown dice type: {dice_type}")
        
        dice = self.dice_types[dice_type]
        result = dice.roll()
        return dice_type, result
    
    def roll_multiple(self, dice_type='d6', count=1):
        """
        Roll multiple dice of the same type.
        
        Args:
            dice_type (str): Type of dice to roll
            count (int): Number of dice to roll
            
        Returns:
            dict: Dictionary with results and total
        """
        if count < 1:
            raise ValueError("Must roll at least 1 dice")
        
        results = []
        for _ in range(count):
            _, result = self.roll_single(dice_type)
            results.append(result)
        
        return {
            'dice_type': dice_type,
            'results': results,
            'total': sum(results),
            'count': count
        }
    
    def roll_custom_dice(self, sides, count=1):
        """
        Roll custom dice with specified number of sides.
        
        Args:
            sides (int): Number of sides for custom dice
            count (int): Number of dice to roll
            
        Returns:
            dict: Dictionary with results and total
        """
        custom_dice = Dice(sides)
        results = [custom_dice.roll() for _ in range(count)]
        
        return {
            'dice_type': f'd{sides}',
            'results': results,
            'total': sum(results),
            'count': count
        }
    
    def get_available_dice(self):
        """Return list of available dice types."""
        return list(self.dice_types.keys())