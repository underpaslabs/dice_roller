"""
Game-specific dice rolling presets for popular games.
"""

from dice import DiceRoller

class GamePresets:
    """Contains preset dice configurations for various games."""
    
    @staticmethod
    def dnd_ability_roll() -> dict:
        """
        Roll 4d6 and drop the lowest (D&D ability score generation).
        
        Returns:
            dict: Roll results including dropped die
        """
        roller = DiceRoller()
        rolls = [roller.roll_single(6) for _ in range(4)]
        sorted_rolls = sorted(rolls, reverse=True)
        result = {
            'all_rolls': rolls,
            'kept_rolls': sorted_rolls[:3],
            'dropped': sorted_rolls[3],
            'total': sum(sorted_rolls[:3])
        }
        return result
    
    @staticmethod
    def dnd_attack_roll(with_advantage: bool = False, with_disadvantage: bool = False) -> dict:
        """
        Standard D&D attack roll (d20).
        
        Args:
            with_advantage (bool): Roll with advantage
            with_disadvantage (bool): Roll with disadvantage
            
        Returns:
            dict: Attack roll result
        """
        roller = DiceRoller()
        
        if with_advantage:
            return roller.roll_advantage(20)
        elif with_disadvantage:
            return roller.roll_disadvantage(20)
        else:
            roll = roller.roll_single(20)
            return {
                'roll': roll,
                'type': 'normal'
            }
    
    @staticmethod
    def shadowrun_skill_test(dice_pool: int) -> dict:
        """
        Shadowrun skill test (count successes on d6, 5-6 = success).
        
        Args:
            dice_pool (int): Number of d6 to roll
            
        Returns:
            dict: Test results with success count
        """
        roller = DiceRoller()
        rolls = [roller.roll_single(6) for _ in range(dice_pool)]
        successes = sum(1 for roll in rolls if roll >= 5)
        
        return {
            'rolls': rolls,
            'successes': successes,
            'dice_pool': dice_pool,
            'glitch': len([r for r in rolls if r == 1]) > len(rolls) / 2 and successes == 0
        }
    
    @staticmethod
    def warhammer_attack(attacks: int, weapon_strength: int, target_toughness: int) -> dict:
        """
        Warhammer 40k attack sequence.
        
        Args:
            attacks (int): Number of attack dice (usually d6)
            weapon_strength (int): Weapon strength
            target_toughness (int): Target toughness
            
        Returns:
            dict: Attack sequence results
        """
        roller = DiceRoller()
        
        # Roll to hit (usually 3+ for space marines)
        hit_rolls = [roller.roll_single(6) for _ in range(attacks)]
        hits = sum(1 for roll in hit_rolls if roll >= 3)
        
        # Roll to wound
        wound_roll_needed = 4  # Default
        if weapon_strength >= target_toughness * 2:
            wound_roll_needed = 2
        elif weapon_strength > target_toughness:
            wound_roll_needed = 3
        elif weapon_strength == target_toughness:
            wound_roll_needed = 4
        else:
            wound_roll_needed = 5
        
        wound_rolls = [roller.roll_single(6) for _ in range(hits)]
        wounds = sum(1 for roll in wound_rolls if roll >= wound_roll_needed)
        
        return {
            'hit_rolls': hit_rolls,
            'hits': hits,
            'wound_rolls': wound_rolls,
            'wounds': wounds,
            'wound_roll_needed': wound_roll_needed
        }
    
    @staticmethod
    def fate_dice_roll() -> dict:
        """
        FATE/FUDGE dice roll (4dF: -, 0, + results).
        
        Returns:
            dict: FATE dice results
        """
        roller = DiceRoller()
        fate_dice_results = []
        total = 0
        
        for _ in range(4):
            roll = roller.roll_single(3) - 2  # Convert 1-3 to -1, 0, +1
            fate_dice_results.append(roll)
            total += roll
        
        # Convert to symbols for display
        symbols = ['-' if r == -1 else '0' if r == 0 else '+' for r in fate_dice_results]
        
        return {
            'numeric_results': fate_dice_results,
            'symbol_results': symbols,
            'total': total
        }