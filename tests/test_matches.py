from ..game import GameField, Brick

def test_find_matches_horizontal():
    field = GameField(5, 8)
    # Place three ^ in a row
    field.grid[0][0] = '^'
    field.grid[0][1] = '^'
    field.grid[0][2] = '^'
    matches = field.find_matches()
    expected = [(0,0), (0,1), (0,2)]
    assert matches == expected

def test_find_matches_vertical():
    field = GameField(5, 8)
    field.grid[0][0] = '*'
    field.grid[1][0] = '*'
    field.grid[2][0] = '*'
    matches = field.find_matches()
    expected = [(0,0), (1,0), (2,0)]
    assert matches == expected

def test_find_matches_none():
    field = GameField(5, 8)
    field.grid[0][0] = '^'
    field.grid[0][1] = '*'
    matches = field.find_matches()
    assert matches == []

def test_clear_matches():
    field = GameField(5, 8)
    field.grid[0][0] = '^'
    field.grid[0][1] = '^'
    field.grid[0][2] = '^'
    matches = [(0,0), (0,1), (0,2)]
    field.clear_matches(matches)
    assert field.grid[0][0] is None
    assert field.grid[0][1] is None
    assert field.grid[0][2] is None