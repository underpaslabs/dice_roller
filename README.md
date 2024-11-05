# Dice Rolling Simulator

A Python-based dice rolling simulator for various tabletop RPGs and dice games.

## Files Overview

- **`dice.py`**: Contains the `Dice` class and predefined common dice types (D4, D6, D8, D10, D12, D20, D100)
- **`dice_roller.py`**: Main rolling functionality including multiple dice, D&D ability scores, advantage/disadvantage, and Fudge dice
- **`game_simulations.py`**: Game-specific simulations for D&D attacks, Yahtzee, and Shadowrun
- **`main.py`**: Demonstration script showing all functionality

## Usage

### Basic Usage

```python
from dice import D6, D20

# Roll a single die
print(D6.roll())  # Roll a D6
print(D20.roll()) # Roll a D20
```

### Multiple Dice

```python
from dice_roller import DiceRoller

# Roll multiple dice
result = DiceRoller.roll_multiple([D6, D6, D6])  # 3d6
print(f"Rolls: {result['rolls']}")
print(f"Total: {result['total']}")
```

### D&D Specific Rolls

```python
from dice_roller import DiceRoller

# D&D ability score (4d6 drop lowest)
ability = DiceRoller.roll_dnd_ability_score()

# Advantage/Disadvantage
advantage_roll = DiceRoller.roll_advantage()
disadvantage_roll = DiceRoller.roll_disadvantage()
```

### Game Simulations

```python
from game_simulations import GameSimulations

# D&D attack simulation
attack = GameSimulations.simulate_dnd_attack(attacker_bonus=5, target_ac=15)

# Yahtzee roll
yahtzee = GameSimulations.simulate_yahtzee_roll()

# Shadowrun test
shadowrun = GameSimulations.simulate_shadowrun_test(dice_pool=8, threshold=4)
```

## Running the Demo

To see all functionality in action:

```bash
python main.py
```

## Features

- **Multiple Dice Types**: Support for common RPG dice (D4, D6, D8, D10, D12, D20, D100)
- **Game Systems**: D&D 5e, Fudge/FATE, Shadowrun, Yahtzee
- **Special Mechanics**: Advantage/Disadvantage, dice pool systems, drop lowest
- **Extensible**: Easy to add new game systems or dice mechanics

## Customization

Create custom dice:
```python
from dice import Dice
custom_die = Dice(17)  # 17-sided die
```

The system is modular and easily extensible for additional game rules or dice mechanics.