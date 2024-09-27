"""
Dice module containing Dice class for handling individual dice rolls.
"""

import random

class Dice:
    """Represents a single die with configurable sides."""
    
    def __init__(self, sides=6):
        """
        Initialize a dice with specified number of sides.
        
        Args:
            sides (int): Number of sides on the dice (default: 6)
        """
        if sides < 2:
            raise ValueError("Dice must have at least 2 sides")
        self.sides = sides
    
    def roll(self):
        """
        Roll the dice and return the result.
        
        Returns:
            int: Random number between 1 and number of sides
        """
        return random.randint(1, self.sides)
    
    def __str__(self):
        return f"D{self.sides}"
    
    def __repr__(self):
        return f"Dice(sides={self.sides})"