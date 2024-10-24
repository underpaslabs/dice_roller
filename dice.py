"""
Dice module containing Dice class and dice type definitions
"""

class Dice:
    """Represents a dice with a specific number of sides"""
    
    def __init__(self, sides=6):
        """
        Initialize a dice
        
        Args:
            sides (int): Number of sides on the dice (default: 6)
        """
        if sides < 2:
            raise ValueError("Dice must have at least 2 sides")
        self.sides = sides
    
    def roll(self):
        """
        Roll the dice once
        
        Returns:
            int: Random number between 1 and number of sides
        """
        import random
        return random.randint(1, self.sides)
    
    def __str__(self):
        return f"D{self.sides}"

# Common dice types
D4 = Dice(4)
D6 = Dice(6)
D8 = Dice(8)
D10 = Dice(10)
D12 = Dice(12)
D20 = Dice(20)
D100 = Dice(100)