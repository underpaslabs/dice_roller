"""
Main dice rolling interface and game simulations
"""

from dice import Dice, StandardDice, DicePool
from typing import List, Dict, Any

class DiceRoller:
    """Main class for dice rolling operations"""
    
    def __init__(self):
        self.roll_history = []
    
    def roll_single(self, sides: int) -> int:
        """
        Roll a single die with specified sides
        
        Args:
            sides (int): Number of sides on the die
            
        Returns:
            int: Roll result
        """
        die = Dice(sides)
        result = die.roll()
        self.roll_history.append({
            'type': 'single',
            'sides': sides,
            'result': result
        })
        return result
    
    def roll_multiple(self, sides: int, count: int) -> List[int]:
        """
        Roll multiple dice of the same type
        
        Args:
            sides (int): Number of sides on each die
            count (int): Number of dice to roll
            
        Returns:
            List[int]: List of roll results
        """
        dice = [Dice(sides) for _ in range(count)]
        pool = DicePool(dice)
        results = pool.roll()
        
        self.roll_history.append({
            'type': 'multiple',
            'sides': sides,
            'count': count,
            'results': results,
            'total': sum(results)
        })
        
        return results
    
    def roll_standard(self, dice_type: str, count: int = 1) -> List[int]:
        """
        Roll standard RPG dice (d4, d6, d8, d10, d12, d20, d100)
        
        Args:
            dice_type (str): Type of dice ('d4', 'd6', etc.)
            count (int): Number of dice to roll
            
        Returns:
            List[int]: List of roll results
        """
        dice_map = {
            'd4': StandardDice.d4,
            'd6': StandardDice.d6,
            'd8': StandardDice.d8,
            'd10': StandardDice.d10,
            'd12': StandardDice.d12,
            'd20': StandardDice.d20,
            'd100': StandardDice.d100
        }
        
        if dice_type not in dice_map:
            raise ValueError(f"Unknown dice type: {dice_type}")
        
        dice = [dice_map[dice_type]() for _ in range(count)]
        pool = DicePool(dice)
        results = pool.roll()
        
        self.roll_history.append({
            'type': 'standard',
            'dice_type': dice_type,
            'count': count,
            'results': results,
            'total': sum(results)
        })
        
        return results
    
    def get_history(self) -> List[Dict[str, Any]]:
        """
        Get roll history
        
        Returns:
            List[Dict]: List of previous rolls with details
        """
        return self.roll_history.copy()
    
    def clear_history(self):
        """Clear roll history"""
        self.roll_history.clear()

class GameSimulator:
    """Simulate dice rolls for various games"""
    
    @staticmethod
    def dnd_ability_roll() -> Dict[str, Any]:
        """
        Simulate D&D ability score roll (4d6 drop lowest)
        
        Returns:
            Dict: Roll details including dropped die and total
        """
        rolls = [StandardDice.d6().roll() for _ in range(4)]
        total = sum(rolls) - min(rolls)
        
        return {
            'rolls': rolls,
            'dropped': min(rolls),
            'total': total
        }
    
    @staticmethod
    def yahtzee_roll(dice_count: int = 5) -> List[int]:
        """
        Simulate Yahtzee dice roll
        
        Args:
            dice_count (int): Number of dice to roll (default: 5)
            
        Returns:
            List[int]: Results of dice rolls
        """
        return [StandardDice.d6().roll() for _ in range(dice_count)]
    
    @staticmethod
    def shadowrun_roll(dice_pool: int, target_number: int = 5) -> Dict[str, Any]:
        """
        Simulate Shadowrun dice pool roll
        
        Args:
            dice_pool (int): Number of d6 to roll
            target_number (int): Minimum value for success (default: 5)
            
        Returns:
            Dict: Roll results including successes and individual rolls
        """
        rolls = [StandardDice.d6().roll() for _ in range(dice_pool)]
        successes = sum(1 for roll in rolls if roll >= target_number)
        glitches = sum(1 for roll in rolls if roll == 1)
        is_glitch = glitches > len(rolls) / 2
        
        return {
            'rolls': rolls,
            'successes': successes,
            'glitches': glitches,
            'is_glitch': is_glitch,
            'critical_glitch': is_glitch and successes == 0
        }