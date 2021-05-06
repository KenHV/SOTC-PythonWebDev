# Rock Paper Scissors

## Rules

- Rock wins against scissors.
- Scissors win against paper.
- Paper wins against rock.

## Logic

Player and computer choose an object randomly and the game determines who's the winner using conditions written from the rules.

The objects are stored in a sequence called list, which is a collection of elements. We use the `choice()` function from `random` module to choose a random object from this list.

`while` is a loop which keeps running the block of code inside it till the given condition evaluates to `False`. We use `while True` to make the loop infinite.

We ask the player if they want to play again after each win/lose. If they want to, we continue the loop using `continue`. If not, we break out from the loop using `break`.

## Assignment

- Add a condition to handle a tie if the player and computer both choose the same object.
- Add a condition to handle invalid choices by the player.
