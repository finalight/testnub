from ..game import ALLOWED_SYMBOLS, COMMANDS

def test_allowed_symbols():
    expected = ["~", "^", "*", "@"]
    assert ALLOWED_SYMBOLS == expected

def test_commands():
    expected = ["L", "R", "D"]
    assert COMMANDS == expected