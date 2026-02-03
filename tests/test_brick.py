from ..game import Brick

def test_brick_creation():
    brick = Brick('H', ['~', '^', '*'])
    assert brick.orientation == 'H'
    assert brick.symbols == ['~', '^', '*']
    assert brick.row == 0
    assert brick.col == 0

def test_brick_vertical():
    brick = Brick('V', ['*', '@', '~'])
    assert brick.orientation == 'V'
    assert brick.symbols == ['*', '@', '~']