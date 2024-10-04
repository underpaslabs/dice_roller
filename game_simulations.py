"""
Game-specific dice rolling simulations for common tabletop games.
"""

from dice_roller import DiceRoller

class GameSimulations:
    """Pre-configured dice simulations for various games."""
    
    @staticmethod
    def dnd_ability_roll():
        """
        Simulate D&D ability score roll (4d6 drop lowest).
        
        Returns:
            dict: Roll results with dropped value
        """
        roller = DiceRoller()
        roller.add_dice(6, 4)
        result = roller.roll_all()['D6']
        
        # Drop the lowest roll for D&D ability scores
        rolls = result['rolls']
        min_roll = min(rolls)
        final_rolls = [r for r in rolls if r != min_roll] or [min_roll]
        
        return {
            'all_rolls': rolls,
            'final_rolls': final_rolls,
            'dropped': min_roll,
            'total': sum(final_rolls)
        }
    
    @staticmethod
    def dnd_attack_roll(advantage=False, disadvantage=False):
        """
        Simulate D&D attack roll (d20 with optional advantage/disadvantage).
        
        Args:
            advantage (bool): Roll with advantage
            disadvantage (bool): Roll with disadvantage
            
        Returns:
            dict: Attack roll results
        """
        roller = DiceRoller()
        
        if advantage and disadvantage:
            # Cancel each other out
            roller.add_dice(20, 1)
        elif advantage:
            roller.add_dice(20, 2)
        elif disadvantage:
            roller.add_dice(20, 2)
        else:
            roller.add_dice(20, 1)
        
        result = roller.roll_all()['D20']
        rolls = result['rolls']
        
        if len(rolls) == 2:
            if advantage:
                final_roll = max(rolls)
            else:  # disadvantage
                final_roll = min(rolls)
        else:
            final_roll = rolls[0]
        
        return {
            'rolls': rolls,
            'final_roll': final_roll,
            'advantage': advantage,
            'disadvantage': disadvantage
        }
    
    @staticmethod
    def shadowrun_pool(dice_pool):
        """
        Simulate Shadowrun dice pool (count successes on d6, 5-6 = success).
        
        Args:
            dice_pool (int): Number of d6 to roll
            
        Returns:
            dict: Success count and individual rolls
        """
        roller = DiceRoller()
        roller.add_dice(6, dice_pool)
        result = roller.roll_all()['D6']
        
        successes = sum(1 for roll in result['rolls'] if roll >= 5)
        
        return {
            'rolls': result['rolls'],
            'successes': successes,
            'dice_pool': dice_pool,
            'success_threshold': 5
        }
    
    @staticmethod
    def warhammer_roll(dice_count, target_number):
        """
        Simulate Warhammer-style roll (count successes above target number).
        
        Args:
            dice_count (int): Number of d6 to roll
            target_number (int): Minimum number for success
            
        Returns:
            dict: Success results
        """
        roller = DiceRoller()
        roller.add_dice(6, dice_count)
        result = roller.roll_all()['D6']
        
        successes = sum(1 for roll in result['rolls'] if roll >= target_number)
        
        return {
            'rolls': result['rolls'],
            'successes': successes,
            'target_number': target_number,
            'dice_count': dice_count
        }