from ..game import GameField, Brick

def test_place_brick_horizontal():
    field = GameField(5, 8)
    brick = Brick('H', ['~', '^', '*'])
    brick.row = 0
    brick.col = 1
    field.place_brick(brick)
    assert field.grid[0][1] == '~'
    assert field.grid[0][2] == '^'
    assert field.grid[0][3] == '*'
    assert field.grid[0][0] is None
    assert field.grid[0][4] is None

def test_place_brick_vertical():
    field = GameField(5, 8)
    brick = Brick('V', ['*', '@', '~'])
    brick.row = 0
    brick.col = 2
    field.place_brick(brick)
    assert field.grid[0][2] == '*'
    assert field.grid[1][2] == '@'
    assert field.grid[2][2] == '~'
    assert field.grid[0][1] is None