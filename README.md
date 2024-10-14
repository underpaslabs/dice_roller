## Dice Rolling Simulator

A Python-based dice rolling simulator for various tabletop games with support for multiple dice types and game-specific rolling mechanics.

### Features

- **Multiple Dice Types**: Support for standard RPG dice (d4, d6, d8, d10, d12, d20, d100) and custom dice
- **Game Simulations**: Pre-built simulations for popular games:
  - D&D (4d6 drop lowest for ability scores)
  - Yahtzee (5d6)
  - Shadowrun (dice pool system with glitches)
- **Roll History**: Track your rolls with detailed history
- **Interactive Interface**: Command-line interface for easy use

### Installation & Requirements

No external dependencies required! Just Python 3.6+ with standard library.

### How to Use

#### Quick Start
Run the interactive application:
```bash
python main.py
```

#### Basic Usage Examples

**Interactive Mode:**
```bash
python main.py
```
Then use commands like:
- `roll d20` - Roll a 20-sided die
- `roll 3d6` - Roll three 6-sided dice
- `game dnd` - Simulate a D&D ability score roll
- `history` - View roll history
- `clear` - Clear history

**Programmatic Usage:**
```python
from roller import DiceRoller, GameSimulator

# Basic dice rolling
roller = DiceRoller()
result = roller.roll_standard('d20')  # Single d20
results = roller.roll_multiple(6, 3)  # Three d6

# Game simulations
dnd_roll = GameSimulator.dnd_ability_roll()
yahtzee_roll = GameSimulator.yahtzee_roll()
shadowrun_roll = GameSimulator.shadowrun_roll(8, 5)
```

#### File Structure
- `dice.py` - Core dice classes and dice pool functionality
- `roller.py` - Main rolling interface and game simulations
- `examples.py` - Demonstration of various features
- `main.py` - Interactive command-line application

#### Example Output
```
🎲 Dice Rolling Simulator 🎲
Commands: roll, game, history, clear, quit

> roll d20
Rolled d20: 17

> roll 3d6
Rolled 3d6: [4, 2, 6] = 12

> game dnd
D&D Ability Roll: [5, 3, 6, 2] (dropped 2) = 14

> history
Roll History (3 rolls):
  1. d20: 17
  2. 3d6: [4, 2, 6] (Total: 12)
  3. standard: 4d6: [5, 3, 6, 2] (Total: 14)
```

### Extending the System

You can easily add new game simulations by creating new methods in the `GameSimulator` class or extend the dice system by adding new dice types to the `StandardDice` class.

Enjoy your dice rolling adventures! 🎲