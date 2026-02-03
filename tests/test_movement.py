from ..game import Game, Brick

def test_move_left():
    bricks = [Brick('H', ['~', '^', '*'])]
    game = Game(5, 8, bricks)
    initial_col = game.active_brick.col
    game.move_left()
    assert game.active_brick.col == initial_col - 1

def test_move_left_blocked():
    bricks = [Brick('H', ['~', '^', '*'])]
    game = Game(5, 8, bricks)
    game.active_brick.col = 0  # already at left
    initial_col = game.active_brick.col
    game.move_left()
    assert game.active_brick.col == initial_col  # no change

def test_move_right():
    bricks = [Brick('H', ['~', '^', '*'])]
    game = Game(5, 8, bricks)
    initial_col = game.active_brick.col
    game.move_right()
    assert game.active_brick.col == initial_col + 1

def test_drop():
    bricks = [Brick('H', ['~', '^', '*'])]
    game = Game(5, 8, bricks)
    game.drop()
    assert game.active_brick.row == 7  # bottom for 8 height, row 0-7, horizontal at row 7