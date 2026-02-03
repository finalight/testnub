from utils import validate_input


def test_validate_input_valid():
    from game import Brick

    bricks = [Brick("H", ["~", "^", "*"])]
    assert validate_input(5, 8, bricks)


def test_validate_input_no_bricks():
    bricks = []  # no bricks provided
    assert not validate_input(5, 8, bricks)


def test_validate_input_invalid_width():
    from game import Brick

    bricks = [Brick("H", ["~", "^", "*"])]
    assert not validate_input(0, 8, bricks)
    assert not validate_input(-1, 8, bricks)


def test_validate_input_invalid_height():
    from game import Brick

    bricks = [Brick("H", ["~", "^", "*"])]
    assert not validate_input(5, 0, bricks)


def test_validate_input_too_many_bricks():
    from game import Brick

    bricks = [Brick("H", ["~", "^", "*"])] * 6  # 6 bricks
    assert not validate_input(5, 8, bricks)


def test_validate_input_valid_bricks():
    from game import Brick

    bricks = [Brick("H", ["~", "^", "*"]), Brick("V", ["*", "@", "~"])]
    assert validate_input(5, 8, bricks)


def test_validate_input_invalid_orientation():
    from game import Brick

    bricks = [Brick("X", ["~", "^", "*"])]  # invalid orientation
    assert not validate_input(5, 8, bricks)


def test_validate_input_invalid_symbols():
    from game import Brick

    bricks = [Brick("H", ["~", "^", "X"])]  # invalid symbol
    assert not validate_input(5, 8, bricks)
