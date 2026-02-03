from game import Brick, ALLOWED_SYMBOLS

def parse_input(input_str):
    parts = input_str.split()
    width = int(parts[0])
    height = int(parts[1])
    bricks = []
    i = 2
    while i < len(parts):
        orientation = parts[i][0]
        symbols = list(parts[i][1:])
        bricks.append(Brick(orientation, symbols))
        i += 1
    return width, height, bricks

def display_field(field, active_brick=None):
    lines = []
    for r in range(field.height):
        row_cells = []
        for c in range(field.width):
            cell = field.grid[r][c]
            if active_brick and active_brick.row <= r < active_brick.row + (3 if active_brick.orientation == 'V' else 1) and \
               ((active_brick.orientation == 'H' and active_brick.col <= c < active_brick.col + 3) or \
                (active_brick.orientation == 'V' and c == active_brick.col)):
                # Calculate index in brick symbols
                if active_brick.orientation == 'H':
                    idx = c - active_brick.col
                else:
                    idx = r - active_brick.row
                cell = active_brick.symbols[idx] if cell is None else cell  # show brick symbol if empty, but if occupied, show grid?
            row_cells.append(cell if cell is not None else '.')
        line = ' '.join(row_cells)
        lines.append(f"| {line} |")
    return '\n'.join(lines)

def validate_input(width, height, bricks):
    if width <= 0 or height <= 0:
        return False
    if len(bricks) > 5:
        return False
    for brick in bricks:
        if brick.orientation not in ['H', 'V']:
            return False
        if len(brick.symbols) != 3:
            return False
        if not all(symbol in ALLOWED_SYMBOLS for symbol in brick.symbols):
            return False
    return True