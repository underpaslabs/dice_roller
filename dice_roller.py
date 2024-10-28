"""
Main dice roller module with game-specific rolling functions
"""

from dice import Dice, D4, D6, D8, D10, D12, D20, D100
import random

class DiceRoller:
    """Handles dice rolling operations for various games"""
    
    @staticmethod
    def roll_multiple(dice_list):
        """
        Roll multiple dice and return individual results and total
        
        Args:
            dice_list (list): List of Dice objects or integers (sides)
            
        Returns:
            dict: Dictionary with individual rolls and total
        """
        results = []
        total = 0
        
        for dice in dice_list:
            if isinstance(dice, Dice):
                roll = dice.roll()
            elif isinstance(dice, int):
                roll = random.randint(1, dice)
            else:
                raise ValueError("Dice must be Dice object or integer")
                
            results.append(roll)
            total += roll
        
        return {
            'rolls': results,
            'total': total,
            'dice_used': [str(dice) if isinstance(dice, Dice) else f"D{dice}" 
                         for dice in dice_list]
        }
    
    @staticmethod
    def roll_dnd_ability_score():
        """
        Roll 4d6 and drop the lowest (D&D ability score method)
        
        Returns:
            dict: Roll results including dropped die
        """
        rolls = [D6.roll() for _ in range(4)]
        sorted_rolls = sorted(rolls, reverse=True)
        total = sum(sorted_rolls[:3])
        
        return {
            'rolls': rolls,
            'kept_rolls': sorted_rolls[:3],
            'dropped_roll': sorted_rolls[3],
            'total': total
        }
    
    @staticmethod
    def roll_fudge_dice(count=4):
        """
        Roll Fudge/FATE dice (-1, 0, +1 results)
        
        Args:
            count (int): Number of Fudge dice to roll
            
        Returns:
            dict: Roll results with total
        """
        results = []
        for _ in range(count):
            roll = random.randint(1, 3)  # 1=-1, 2=0, 3=+1
            if roll == 1:
                results.append(-1)
            elif roll == 2:
                results.append(0)
            else:
                results.append(1)
        
        return {
            'rolls': results,
            'total': sum(results)
        }
    
    @staticmethod
    def roll_advantage():
        """
        Roll with advantage (D&D 5e) - roll 2d20, take higher
        
        Returns:
            dict: Both rolls and the result used
        """
        roll1 = D20.roll()
        roll2 = D20.roll()
        result = max(roll1, roll2)
        
        return {
            'rolls': [roll1, roll2],
            'result': result,
            'type': 'advantage'
        }
    
    @staticmethod
    def roll_disadvantage():
        """
        Roll with disadvantage (D&D 5e) - roll 2d20, take lower
        
        Returns:
            dict: Both rolls and the result used
        """
        roll1 = D20.roll()
        roll2 = D20.roll()
        result = min(roll1, roll2)
        
        return {
            'rolls': [roll1, roll2],
            'result': result,
            'type': 'disadvantage'
        }