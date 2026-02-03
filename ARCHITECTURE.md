# Architecture & Design

## Project Structure

```
testnub/
├── main.py                 # Game loop and initialization
├── game.py                 # Core game classes
├── utils.py                # Utilities (parse, validate, display)
├── __init__.py
├── pyproject.toml
├── README.md               # Overview
├── ARCHITECTURE.md         # This file
├── ASSUMPTIONS.md          # Assumptions & future work
└── tests/                  # 36 comprehensive tests
    ├── test_validation.py
    ├── test_command_validation.py
    ├── test_game_init.py
    ├── test_game_field.py
    ├── test_brick.py
    ├── test_matches.py
    ├── test_movement.py
    ├── test_place_brick.py
    ├── test_utils.py
    └── test_constants.py
```

## Core Classes

### Brick
Represents a falling brick with orientation and 3 symbols.

**Attributes:**
- `orientation`: 'H' (horizontal) or 'V' (vertical)
- `symbols`: List of 3 symbols (`~`, `^`, `*`, `@`)
- `row`, `col`: Current position

**Usage:**
```python
brick = Brick('H', ['^', '^', '*'])
```

### GameField
Manages the game field, brick placement, and match detection.

**Attributes:**
- `width`, `height`: Field dimensions
- `grid`: 2D list of placed symbols (None = empty)

**Key Methods:**
- `is_valid_position(brick, row, col)` - Check if brick can be placed
- `place_brick(brick)` - Place brick symbols on grid
- `find_matches()` - Detect 3+ symbol matches
- `clear_matches(positions)` - Remove matched symbols

### Game
Main game controller managing state and brick queue.

**Attributes:**
- `field`: GameField instance
- `brick_queue`: List of bricks to place
- `current_brick_index`: Current brick index
- `active_brick`: Currently falling brick

**Key Methods:**
- `move_left()` - Move active brick left
- `move_right()` - Move active brick right
- `drop()` - Drop brick to lowest position

## Utilities

### parse_input(input_str)
Parses "WIDTH HEIGHT BRICK1 BRICK2..." into components.

### validate_input(width, height, bricks)
Validates:
- Width and height > 0
- At least 1 brick (max 5)
- Valid orientations (H/V)
- Exactly 3 symbols per brick
- Valid symbols (~, ^, *, @)

### display_field(field, active_brick=None)
Renders game field as string for display.

## Game Flow

1. **Initialize**: User enters field size and bricks
2. **Validate**: Input validation (dimensions, bricks, symbols)
3. **Game Loop**:
   - Display field with active brick
   - Get user commands (max 2)
   - Validate commands (only L, R, D)
   - Execute valid commands
   - Auto-drop brick by 1 row
   - Check if brick can drop:
     - If yes: Continue
     - If no: Place brick, check matches, load next brick
4. **Game Over**: No more bricks or can't place new brick

## Input Validation

### Field Size
- Width, height must be > 0

### Bricks
- At least 1, maximum 5 bricks
- Orientation: H (horizontal) or V (vertical)
- Exactly 3 symbols per brick
- Symbols from: ~, ^, *, @

### Commands
- Only L, R, D allowed
- Invalid commands: Show error, don't drop brick, re-prompt

## Data Structures

### Grid Representation
2D list where:
- `None` = empty cell
- Character = placed symbol

```python
grid = [
    [None, '^', None],
    ['~', '^', '*'],
    [None, '@', None]
]
```

### Brick Positioning
- **Horizontal**: Spans 3 columns in 1 row
- **Vertical**: Spans 1 column across 3 rows

```
Horizontal:  Vertical:
[^][^][*]    [^]
             [*]
             [@]
```

## Design Patterns

### Separation of Concerns
- `game.py`: Game logic
- `main.py`: User interaction
- `utils.py`: Input/output

### Test-Driven Development
All features tested before implementation:
1. Write tests (red)
2. Implement code (green)
3. Verify all tests pass

### Validation Strategy
Two-level validation:
1. Input validation (field/bricks setup)
2. Command validation (gameplay)

## Test Coverage

**36 total tests** across 10 test files:
- ✅ Input validation (no bricks, dimensions, symbols)
- ✅ Command validation (L, R, D only)
- ✅ Brick movement
- ✅ Brick placement
- ✅ Match detection/clearing
- ✅ Game initialization
- ✅ Field rendering

## Constants

```python
ALLOWED_SYMBOLS = ["~", "^", "*", "@"]
COMMANDS = ["L", "R", "D"]
```

## Performance

- Match detection: O(width × height) per turn
- Brick movement: O(1) per direction
- Field validation: O(brick_size) per position
- Suitable for interactive terminal gameplay

