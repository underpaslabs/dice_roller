"""
Dice module containing Dice and DiceRoller classes for simulating dice rolls.
"""

import random
from typing import List, Union, Dict

class Dice:
    """Represents a single die with configurable sides."""
    
    def __init__(self, sides: int = 6):
        """
        Initialize a die with specified number of sides.
        
        Args:
            sides (int): Number of sides on the die (default: 6)
        """
        if sides < 2:
            raise ValueError("Dice must have at least 2 sides")
        self.sides = sides
    
    def roll(self) -> int:
        """Roll the die and return the result."""
        return random.randint(1, self.sides)
    
    def __str__(self) -> str:
        return f"d{self.sides}"
    
    def __repr__(self) -> str:
        return f"Dice(sides={self.sides})"

class DiceRoller:
    """Handles rolling multiple dice and calculating results."""
    
    def __init__(self):
        """Initialize the dice roller."""
        self.roll_history = []
    
    def roll_single(self, sides: int) -> int:
        """
        Roll a single die with specified sides.
        
        Args:
            sides (int): Number of sides on the die
            
        Returns:
            int: Roll result
        """
        die = Dice(sides)
        result = die.roll()
        self.roll_history.append({
            'type': f'd{sides}',
            'result': result,
            'timestamp': len(self.roll_history) + 1
        })
        return result
    
    def roll_multiple(self, dice_config: Dict[str, int]) -> Dict[str, Union[int, List[int]]]:
        """
        Roll multiple dice based on configuration.
        
        Args:
            dice_config (dict): Dictionary with die types as keys and quantities as values
                Example: {'d6': 2, 'd20': 1}
                
        Returns:
            dict: Results including individual rolls and total
        """
        individual_rolls = {}
        total = 0
        
        for die_type, quantity in dice_config.items():
            sides = int(die_type[1:])  # Extract number from 'd6', 'd20', etc.
            rolls = [self.roll_single(sides) for _ in range(quantity)]
            individual_rolls[die_type] = rolls
            total += sum(rolls)
        
        result = {
            'individual_rolls': individual_rolls,
            'total': total,
            'config': dice_config
        }
        
        self.roll_history.append({
            'type': 'multiple',
            'result': result,
            'timestamp': len(self.roll_history) + 1
        })
        
        return result
    
    def roll_advantage(self, sides: int = 20) -> Dict[str, int]:
        """
        Roll with advantage (take higher of two rolls).
        
        Args:
            sides (int): Number of sides (default: 20 for D&D)
            
        Returns:
            dict: Both rolls and the selected result
        """
        roll1 = self.roll_single(sides)
        roll2 = self.roll_single(sides)
        
        result = {
            'rolls': [roll1, roll2],
            'selected': max(roll1, roll2),
            'type': 'advantage'
        }
        
        return result
    
    def roll_disadvantage(self, sides: int = 20) -> Dict[str, int]:
        """
        Roll with disadvantage (take lower of two rolls).
        
        Args:
            sides (int): Number of sides (default: 20 for D&D)
            
        Returns:
            dict: Both rolls and the selected result
        """
        roll1 = self.roll_single(sides)
        roll2 = self.roll_single(sides)
        
        result = {
            'rolls': [roll1, roll2],
            'selected': min(roll1, roll2),
            'type': 'disadvantage'
        }
        
        return result
    
    def get_history(self, limit: int = None) -> List[Dict]:
        """
        Get roll history.
        
        Args:
            limit (int, optional): Number of recent rolls to return
            
        Returns:
            list: Roll history
        """
        if limit:
            return self.roll_history[-limit:]
        return self.roll_history
    
    def clear_history(self):
        """Clear the roll history."""
        self.roll_history.clear()