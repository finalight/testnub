from game import Brick, GameField
from utils import display_field, parse_input


def test_parse_input():
    input_str = "5 8 H^^* V*@^"
    width, height, bricks = parse_input(input_str)
    assert width == 5
    assert height == 8
    assert len(bricks) == 2
    assert bricks[0].orientation == "H"
    assert bricks[0].symbols == ["^", "^", "*"]
    assert bricks[1].orientation == "V"
    assert bricks[1].symbols == ["*", "@", "^"]


def test_display_field_empty():
    field = GameField(3, 2)
    output = display_field(field)
    expected = "| . . . |\n| . . . |"
    assert output == expected


def test_display_field_with_active_brick():
    field = GameField(5, 8)
    brick = Brick("H", ["~", "^", "*"])
    brick.row = 0
    brick.col = 1
    output = display_field(field, brick)
    # Should show ~ ^ * at positions 1,2,3 in row 0
    lines = output.split("\n")
    assert lines[0] == "| . ~ ^ * . |"
