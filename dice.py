"""
Dice module containing dice classes and roll functionality
"""

import random
from typing import List, Union

class Dice:
    """Base dice class"""
    
    def __init__(self, sides: int = 6):
        """
        Initialize a dice with specified number of sides
        
        Args:
            sides (int): Number of sides on the dice (default: 6)
        """
        if sides < 2:
            raise ValueError("Dice must have at least 2 sides")
        self.sides = sides
    
    def roll(self) -> int:
        """
        Roll the dice once
        
        Returns:
            int: Random number between 1 and number of sides
        """
        return random.randint(1, self.sides)
    
    def __str__(self) -> str:
        return f"d{self.sides}"

class StandardDice(Dice):
    """Standard polyhedral dice used in RPGs"""
    
    @classmethod
    def d4(cls):
        return cls(4)
    
    @classmethod
    def d6(cls):
        return cls(6)
    
    @classmethod
    def d8(cls):
        return cls(8)
    
    @classmethod
    def d10(cls):
        return cls(10)
    
    @classmethod
    def d12(cls):
        return cls(12)
    
    @classmethod
    def d20(cls):
        return cls(20)
    
    @classmethod
    def d100(cls):
        return cls(100)

class DicePool:
    """Collection of dice to roll together"""
    
    def __init__(self, dice: List[Dice]):
        """
        Initialize a pool of dice
        
        Args:
            dice (List[Dice]): List of Dice objects
        """
        self.dice = dice
    
    def roll(self) -> List[int]:
        """
        Roll all dice in the pool
        
        Returns:
            List[int]: Results of all dice rolls
        """
        return [die.roll() for die in self.dice]
    
    def sum(self) -> int:
        """
        Roll all dice and return the sum
        
        Returns:
            int: Sum of all dice rolls
        """
        return sum(self.roll())
    
    def count_successes(self, target: int) -> int:
        """
        Count how many dice meet or exceed target number
        
        Args:
            target (int): Minimum value to count as success
            
        Returns:
            int: Number of successful rolls
        """
        results = self.roll()
        return sum(1 for result in results if result >= target)