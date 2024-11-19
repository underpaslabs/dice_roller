# Dice Roller Simulator

A Python-based dice rolling simulator for various tabletop games with support for multiple dice types and game-specific rolling mechanics.

## Files Overview

- **`dice.py`**: Contains the `Dice` class for individual dice operations
- **`dice_roller.py`**: Main roller class for handling multiple dice rolls
- **`game_examples.py`**: Pre-built game simulations (D&D ability rolls, advantage/disadvantage, damage rolls)
- **`main.py`**: Interactive command-line interface for rolling dice

## Installation & Requirements

No external dependencies required! Just ensure you have Python 3.6+ installed.

## Usage

### Quick Start

Run the interactive program:
```bash
python main.py
```

### Using Individual Components

**Basic Dice Rolling:**
```python
from dice_roller import DiceRoller

roller = DiceRoller()

# Roll a single d20
result = roller.roll_single('d20')
print(f"Rolled: {result}")

# Roll 3d6
result = roller.roll_multiple('d6', 3)
print(f"Rolls: {result['results']}, Total: {result['total']}")
```

**Game Examples:**
```python
from game_examples import GameExamples

examples = GameExamples()

# D&D ability score (4d6 drop lowest)
ability = examples.dnd_ability_roll()

# Advantage roll (2d20 take higher)
advantage = examples.advantage_roll()

# Damage roll with modifier
damage = examples.damage_roll('d8', 2, 5)
```

### Available Dice Types

The simulator includes these standard dice:
- d4, d6, d8, d10, d12, d20, d100

You can also create custom dice with any number of sides.

## Features

- ✅ Multiple dice types support
- ✅ Roll multiple dice at once
- ✅ Custom dice creation
- ✅ Game-specific rolling mechanics
- ✅ Interactive command-line interface
- ✅ D&D advantage/disadvantage system
- ✅ Damage rolls with modifiers
- ✅ D&D ability score generation

## Example Game Simulations

The system includes built-in simulations for:
- **D&D Ability Scores**: 4d6 drop lowest
- **Advantage/Disadvantage**: Roll 2d20, take higher/lower
- **Damage Rolls**: Multiple dice with modifiers
- **Custom Dice**: Any number of sides

## Extending

You can easily add new game mechanics by:
1. Creating new methods in `GameExamples` class
2. Adding new dice types to `DiceRoller.dice_types`
3. Extending the `Dice` class for specialized dice

Enjoy rolling! 🎲