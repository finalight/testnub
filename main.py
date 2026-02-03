from utils import parse_input, validate_input, display_field
from game import Game

def initialize_game():
    while True:
        try:
            input_str = input("Please enter field size (width and height) and up to 5 bricks:\nExample: 5 8 H^^* V*@^\"\n")
            width, height, bricks = parse_input(input_str)
            if validate_input(width, height, bricks):
                return Game(width, height, bricks)
            else:
                print("Invalid input. Please check width/height > 0, up to 5 bricks, valid orientations and symbols.")
        except (ValueError, IndexError):
            print("Invalid input format. Please try again.")

def game_loop(game):
    while game.active_brick:
        print(display_field(game.field, game.active_brick))
        commands = input("Enter up to 2 commands (L,R,D): ").strip().upper()
        # Process up to 2 commands
        for cmd in commands[:2]:
            if cmd == 'L':
                game.move_left()
            elif cmd == 'R':
                game.move_right()
            elif cmd == 'D':
                game.drop()
        # Auto drop by 1
        if game.field.is_valid_position(game.active_brick, game.active_brick.row + 1, game.active_brick.col):
            game.active_brick.row += 1
        else:
            # Place the brick
            game.field.place_brick(game.active_brick)
            # Check and clear matches
            matches = game.field.find_matches()
            if matches:
                game.field.clear_matches(matches)
            # Next brick
            game.current_brick_index += 1
            if game.current_brick_index < len(game.brick_queue):
                game.active_brick = game.brick_queue[game.current_brick_index]
                game._position_active_brick()
                if not game.field.is_valid_position(game.active_brick, game.active_brick.row, game.active_brick.col):
                    game.active_brick = None  # Game over
            else:
                game.active_brick = None  # All bricks used
    # Final display after game ends
    print(display_field(game.field))

def main():
    while True:
        game = initialize_game()
        game_loop(game)
        print("Game Over!")
        choice = input("Enter S to start over or Q to quit: ").strip().upper()
        if choice == 'Q':
            print("Thank you for playing Match-3!")
            break

if __name__ == "__main__":
    main()
