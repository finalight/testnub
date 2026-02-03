from game import Brick, GameField


def test_game_field_initialization():
    field = GameField(5, 8)
    assert len(field.grid) == 8  # height
    assert len(field.grid[0]) == 5  # width
    assert all(cell is None for row in field.grid for cell in row)


def test_is_valid_position_empty_field():
    field = GameField(5, 8)
    brick = Brick("H", ["~", "^", "*"])
    # Horizontal brick
    assert field.is_valid_position(brick, 0, 1)  # valid position
    assert field.is_valid_position(brick, 0, 0)  # valid, fits
    assert not field.is_valid_position(brick, 0, 3)  # too right, 3+3=6 >5


def test_is_valid_position_vertical():
    field = GameField(5, 8)
    brick = Brick("V", ["*", "@", "~"])
    assert field.is_valid_position(brick, 0, 2)  # col 2, rows 0-2
    assert not field.is_valid_position(brick, 6, 2)  # too low
