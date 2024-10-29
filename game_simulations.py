"""
Game-specific simulation functions
"""

from dice_roller import DiceRoller
from dice import D6, D20

class GameSimulations:
    """Simulate common game scenarios"""
    
    @staticmethod
    def simulate_dnd_attack(attacker_bonus=5, target_ac=15, advantage=False, disadvantage=False):
        """
        Simulate a D&D attack roll
        
        Args:
            attacker_bonus (int): Attacker's attack bonus
            target_ac (int): Target's Armor Class
            advantage (bool): Roll with advantage
            disadvantage (bool): Roll with disadvantage
            
        Returns:
            dict: Attack result details
        """
        if advantage and disadvantage:
            # Cancel each other out
            attack_roll = D20.roll()
        elif advantage:
            result = DiceRoller.roll_advantage()
            attack_roll = result['result']
        elif disadvantage:
            result = DiceRoller.roll_disadvantage()
            attack_roll = result['result']
        else:
            attack_roll = D20.roll()
        
        total_attack = attack_roll + attacker_bonus
        hit = total_attack >= target_ac
        critical_hit = attack_roll == 20
        critical_miss = attack_roll == 1
        
        return {
            'attack_roll': attack_roll,
            'bonus': attacker_bonus,
            'total_attack': total_attack,
            'target_ac': target_ac,
            'hit': hit,
            'critical_hit': critical_hit,
            'critical_miss': critical_miss
        }
    
    @staticmethod
    def simulate_yahtzee_roll(dice_count=5):
        """
        Simulate a Yahtzee dice roll
        
        Args:
            dice_count (int): Number of dice to roll
            
        Returns:
            dict: Roll results with analysis
        """
        rolls = [D6.roll() for _ in range(dice_count)]
        
        # Analyze the roll
        counts = {}
        for roll in rolls:
            counts[roll] = counts.get(roll, 0) + 1
        
        max_count = max(counts.values())
        is_yahtzee = max_count == dice_count  # All dice same
        is_full_house = sorted(counts.values()) == [2, 3] and len(counts) == 2
        is_large_straight = sorted(rolls) in [[1,2,3,4,5], [2,3,4,5,6]]
        is_small_straight = any(
            all(num in rolls for num in seq) 
            for seq in [[1,2,3,4], [2,3,4,5], [3,4,5,6]]
        )
        
        return {
            'rolls': rolls,
            'total': sum(rolls),
            'counts': counts,
            'is_yahtzee': is_yahtzee,
            'is_full_house': is_full_house,
            'is_large_straight': is_large_straight,
            'is_small_straight': is_small_straight
        }
    
    @staticmethod
    def simulate_shadowrun_test(dice_pool=6, threshold=4):
        """
        Simulate a Shadowrun dice pool test
        
        Args:
            dice_pool (int): Number of D6 to roll
            threshold (int): Target number for successes (5 or 6)
            
        Returns:
            dict: Test results
        """
        rolls = [D6.roll() for _ in range(dice_pool)]
        successes = sum(1 for roll in rolls if roll >= 5)
        glitch = rolls.count(1) > len(rolls) / 2  # More than half are 1s
        critical_glitch = glitch and successes == 0
        
        passed = successes >= threshold
        
        return {
            'rolls': rolls,
            'successes': successes,
            'threshold': threshold,
            'passed': passed,
            'glitch': glitch,
            'critical_glitch': critical_glitch
        }