from ..utils import validate_input

def test_validate_input_valid():
    bricks = []  # mock bricks
    assert validate_input(5, 8, bricks) == True

def test_validate_input_invalid_width():
    bricks = []
    assert validate_input(0, 8, bricks) == False
    assert validate_input(-1, 8, bricks) == False

def test_validate_input_invalid_height():
    bricks = []
    assert validate_input(5, 0, bricks) == False

def test_validate_input_too_many_bricks():
    bricks = [None] * 6  # 6 bricks
    assert validate_input(5, 8, bricks) == False

def test_validate_input_valid_bricks():
    from ..game import Brick
    bricks = [Brick('H', ['~', '^', '*']), Brick('V', ['*', '@', '~'])]
    assert validate_input(5, 8, bricks) == True

def test_validate_input_invalid_orientation():
    from ..game import Brick
    bricks = [Brick('X', ['~', '^', '*'])]  # invalid orientation
    assert validate_input(5, 8, bricks) == False

def test_validate_input_invalid_symbols():
    from ..game import Brick
    bricks = [Brick('H', ['~', '^', 'X'])]  # invalid symbol
    assert validate_input(5, 8, bricks) == False