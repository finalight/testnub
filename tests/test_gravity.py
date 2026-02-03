from ..game import GameField

def test_apply_gravity_no_gaps():
    field = GameField(3, 3)
    field.grid[0] = ['A', 'B', 'C']
    field.grid[1] = ['D', 'E', 'F']
    field.grid[2] = ['G', 'H', 'I']
    field.apply_gravity()
    assert field.grid[0] == ['A', 'B', 'C']
    assert field.grid[1] == ['D', 'E', 'F']
    assert field.grid[2] == ['G', 'H', 'I']

def test_apply_gravity_with_gaps():
    field = GameField(3, 3)
    field.grid[0] = ['A', None, 'C']
    field.grid[1] = [None, 'E', 'F']
    field.grid[2] = ['G', 'H', 'I']
    field.apply_gravity()
    expected = [
        [None, None, 'C'],
        ['A', 'E', 'F'],
        ['G', 'H', 'I']
    ]
    field.apply_gravity()
    assert field.grid == expected