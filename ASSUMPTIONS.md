# Assumptions & Future Extensions

## Implementation Assumptions

### Game Mechanics

1. **Brick Placement**
   - Bricks always spawn at top, centered
   - Each turn, bricks auto-drop 1 row (if valid)
   - User can override with D (drop) to land immediately

2. **Matches**
   - Only detect exact 3+ consecutive matches
   - No diagonal matches
   - Horizontal and vertical checked separately
   - Cleared immediately after placement

3. **Game Ending**
   - Game ends when all bricks placed OR
   - New brick can't fit in starting position

4. **Input Limits**
   - Up to 2 commands per turn
   - Only L, R, D valid
   - Invalid commands block turn progression

### Symbol & Field Constraints

1. **Symbols**
   - Fixed set: ~, ^, *, @ (no customization in current version)
   - Each brick uses exactly 3 symbols
   - No special symbols or power-ups

2. **Field Size**
   - Minimum: 1×1
   - Maximum: Unlimited (but practical limit ~20×20)
   - Fixed throughout game (no resizing)

3. **Brick Count**
   - Exactly 1-5 bricks per game
   - Fixed at start (no dynamic brick generation)
   - All bricks placed sequentially

### Game State

1. **No Undo/Redo**
   - No ability to undo moves
   - No save/load state
   - One playthrough per session

2. **No Scoring**
   - No points tracked
   - No combo multipliers
   - No difficulty levels

3. **Terminal Only**
   - Text-based display
   - No graphics or animations
   - Simple ASCII rendering

## Future Extensions

### Short-term (Quick Wins)

1. **Score Tracking**
   ```python
   # Add to Game class
   self.score = 0
   
   # Increment on match
   # Points = number of cells cleared
   ```

2. **Better Display**
   - Color support for symbols
   - Clear screen between turns
   - Show current score
   - Display remaining bricks

3. **Move Limits**
   - Add turn counter
   - Limit moves per brick
   - Time-based challenges

### Medium-term (Core Features)

1. **Difficulty Levels**
   ```python
   class Difficulty:
       EASY = {"auto_drop_speed": 2}
       MEDIUM = {"auto_drop_speed": 1}
       HARD = {"auto_drop_speed": 0.5}
   ```

2. **Combo Detection**
   - Detect adjacent matches
   - Chain reactions
   - Bonus points for combos

3. **Save/Load**
   - Save game state to file
   - Resume previous games
   - High score storage

4. **Brick Preview**
   - Show next brick before it appears
   - Help with strategy

### Long-term (Major Features)

1. **Graphical UI**
   - Replace terminal with GUI (Pygame/Tkinter)
   - Animated brick dropping
   - Visual feedback for matches

2. **Advanced Mechanics**
   - Special bricks (wildcards, bombs)
   - Power-ups (extra width, slow motion)
   - Level progression
   - Boss levels

3. **Multiplayer**
   - Two-player mode
   - Shared field
   - Competitive mechanics

4. **AI Opponent**
   - Computer-controlled player
   - Different difficulty levels
   - Strategic placement

5. **Sound & Music**
   - Match sound effects
   - Background music
   - Win/loss notifications

## Testing Considerations

### Current Test Coverage
- 36 tests covering core mechanics ✅
- All validation tested
- All movements tested
- All match detection tested

### Future Test Additions
- Score calculation tests
- Combo detection tests
- Difficulty level tests
- Save/load tests
- UI interaction tests

## Known Limitations

1. **No Real-time Clock**
   - No time-based dropping
   - Manual turn-based only

2. **No Undo Mechanism**
   - Mistakes are permanent
   - Requires careful planning

3. **Single Difficulty**
   - No adaptation to player skill
   - Same rules for all players

4. **No Persistence**
   - Game data lost on exit
   - No statistics tracking

5. **Terminal Only**
   - Text-based limits visual appeal
   - No animations or smooth transitions

## Technical Debt / Refactoring Opportunities

1. **Configuration**
   - Extract constants to config file
   - Allow user customization
   - Support different symbol sets

2. **Error Handling**
   - More specific exceptions
   - Better error messages
   - Recovery mechanisms

3. **Code Organization**
   - Separate display logic
   - Create InputValidator class
   - CommandProcessor class

4. **Type Hints**
   - Add Python type annotations
   - Enable static type checking
   - Better IDE support

5. **Documentation**
   - Docstrings for all methods
   - Usage examples
   - API reference

## Dependency Upgrades

Current dependencies:
- Python 3.14+
- pytest 9.0.2+

Future considerations:
- Optional GUI library (Pygame/Tkinter)
- Optional database (SQLite for scores)
- Optional config parser (YAML/TOML)

## Implementation Priority

If adding new features, suggested order:

1. **Priority 1**: Score tracking, better display
2. **Priority 2**: Difficulty levels, move limits, combos
3. **Priority 3**: Save/load, preview next brick
4. **Priority 4**: GUI, multiplayer, AI
5. **Priority 5**: Advanced mechanics, sound

## Contributing Guidelines

For future contributors:
- Follow TDD methodology
- Maintain 100% test coverage
- Update documentation
- Keep code modular
- Write clear commit messages

See [README.md](README.md) for setup instructions.
