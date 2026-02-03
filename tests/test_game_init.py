from ..game import Game, Brick
import pytest
from ..main import initialize_game

def test_initialize_game_valid_input(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda prompt: "5 8 H^^* V*@^")
    game = initialize_game()
    assert game.field.width == 5
    assert game.field.height == 8
    assert len(game.brick_queue) == 2

def test_initialize_game_invalid_then_valid(monkeypatch):
    inputs = iter(["0 8", "5 8 H^^*"])
    monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))
    game = initialize_game()
    assert game.field.width == 5