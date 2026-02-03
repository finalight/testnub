# Constants
ALLOWED_SYMBOLS = ["~", "^", "*", "@"]
COMMANDS = ["L", "R", "D"]

class Brick:
    def __init__(self, orientation, symbols):
        self.orientation = orientation
        self.symbols = symbols
        self.row = 0
        self.col = 0

class GameField:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[None for _ in range(width)] for _ in range(height)]

    def is_valid_position(self, brick, row, col):
        if brick.orientation == 'H':
            # Horizontal: 3 cells in a row
            if col < 0 or col + 3 > self.width or row < 0 or row >= self.height:
                return False
            for i in range(3):
                if self.grid[row][col + i] is not None:
                    return False
        elif brick.orientation == 'V':
            # Vertical: 3 cells in a column
            if col < 0 or col >= self.width or row < 0 or row + 3 > self.height:
                return False
            for i in range(3):
                if self.grid[row + i][col] is not None:
                    return False
        return True

    def place_brick(self, brick):
        if brick.orientation == 'H':
            for i in range(3):
                self.grid[brick.row][brick.col + i] = brick.symbols[i]
        elif brick.orientation == 'V':
            for i in range(3):
                self.grid[brick.row + i][brick.col] = brick.symbols[i]

    def find_matches(self):
        matches = set()
        # Check rows
        for r in range(self.height):
            for c in range(self.width - 2):
                if (self.grid[r][c] == self.grid[r][c+1] == self.grid[r][c+2] and self.grid[r][c] is not None):
                    matches.add((r, c))
                    matches.add((r, c+1))
                    matches.add((r, c+2))
        # Check columns
        for c in range(self.width):
            for r in range(self.height - 2):
                if (self.grid[r][c] == self.grid[r+1][c] == self.grid[r+2][c] and self.grid[r][c] is not None):
                    matches.add((r, c))
                    matches.add((r+1, c))
                    matches.add((r+2, c))
        return sorted(list(matches))

    def clear_matches(self, positions):
        for r, c in positions:
            self.grid[r][c] = None

    def apply_gravity(self):
        for c in range(self.width):
            # Collect non-None cells in column
            cells = [self.grid[r][c] for r in range(self.height) if self.grid[r][c] is not None]
            # Place from bottom up
            for r in range(self.height - 1, -1, -1):
                if cells:
                    self.grid[r][c] = cells.pop()
                else:
                    self.grid[r][c] = None

class Game:
    def __init__(self, width, height, bricks):
        self.field = GameField(width, height)
        self.brick_queue = bricks
        self.current_brick_index = 0
        if bricks:
            self.active_brick = bricks[0]
            self._position_active_brick()
        else:
            self.active_brick = None

    def _position_active_brick(self):
        if self.active_brick.orientation == 'H':
            # Centered in top row
            self.active_brick.col = (self.field.width - 3) // 2
            self.active_brick.row = 0
        elif self.active_brick.orientation == 'V':
            # Centered in top three rows
            self.active_brick.col = (self.field.width - 1) // 2
            self.active_brick.row = 0

    def move_left(self):
        if self.field.is_valid_position(self.active_brick, self.active_brick.row, self.active_brick.col - 1):
            self.active_brick.col -= 1

    def move_right(self):
        if self.field.is_valid_position(self.active_brick, self.active_brick.row, self.active_brick.col + 1):
            self.active_brick.col += 1

    def drop(self):
        # Drop to the lowest possible row
        while self.field.is_valid_position(self.active_brick, self.active_brick.row + 1, self.active_brick.col):
            self.active_brick.row += 1