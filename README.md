# Match-3 Take-Home Assignment (v3)

Welcome to the Match-3 game assignment! You will implement a falling bricks game.
In this game, you will control "bricks” made up of three blocks, each marked with
a special symbol. Bricks can be horizontal or vertical, and you can move or drop
them using simple commands. The goal is to place all bricks and clear as many
matches as possible.

## Initialization

- On startup, prompt the user:
> Please enter field size (width and height) and up to 5 bricks set:
>
> Example: 5 8 H^^* V*@^"
- The first two numbers are the field width and height.
- Each brick is defined by an orientation ('H' for horizontaly, 'V' for vertical)
followed by three symbols (e.g., ~H^^*’).
- Allowed symbols: "~", "^", "*", "@".
- Up to 5 bricks can be provided.

## Game Loop

1. The first brick appears at the top of the field:
- Horizontal: centered in the top rows
- Vertical: c`entered in the top three_rows.
- If the starting position is blocked, the game ends immediately.

2. Each frame:
- Display the current field and active brick.
- Prompt the user:
> Enter up to 2 commands.to process before moving to the next frame (valid
commands are L,R,D)
- Only the first two walid commands are processed per frame.
- Commands:
- "L": Move the. brick left by one column (if possible)
- "R’: Move the brick right by one column (if possible)
- "D": Drop the brick as far down as possible, stopping above any existing
brick or at the bottom
- After commands, the brick always drops by one row automatically.
- If a command would move the brick out of bounds or into another brick, it is
ignored.
- If the brick cannot move further, it becomes stationary.
- When a brick becomes stationary:
- Check for any horizontal or vertical line of 3 or more matching symbols and
remove them.
- Removed cells become empty; gravity is not applied.
- All matches can be removed at once.
- The next brick appears at the top. If it cannot be placed, the game ends.

3. Repeat until all bricks are used or no more can be placed.

## Game End

- After the game ends, prompt:
> Enter S to start over or Q to quit:
> - "S": Restart the game from initialization.
> - "Q": Exit the game.
- Display a thank-you message upon exiting:
> Thank you for playing Match-3!