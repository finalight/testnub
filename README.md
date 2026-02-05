# Match-3 Puzzle Game

A terminal-based Match-3 puzzle game where players place falling bricks and create matches of three or more identical symbols.

## Quick Start

```bash
uv sync
uv run python src/main.py
```

Enter field size and bricks:
```
5 8 H^^* V*@^
```

Use **L** (left), **R** (right), **D** (drop) commands during gameplay.

## Features

- ✅ Customizable game field size
- ✅ Up to 5 bricks per game
- ✅ 4 symbol types: `~`, `^`, `*`, `@`
- ✅ Horizontal & vertical brick placement
- ✅ Match detection (3+ symbols in row/column)
- ✅ Input & command validation
- ✅ 36 passing tests with TDD

## Documentation

- **[Architecture & Design](ARCHITECTURE.md)** - Project structure, classes, and design patterns
- **[Assumptions & Future Extensions](ASSUMPTIONS.md)** - Implementation assumptions and roadmap

## Running Tests

```bash
uv run pytest tests/ -v
```

All 36 tests pass ✅

## Code Quality

```bash
uv run ruff check .       # Check code quality
uv run ruff format .      # Format code
```

Ruff linting passing ✅

