# Dice simulator

import random

dice_choices = [1, 2, 3, 4, 5, 6]

while True:
    choice = random.choice(dice_choices)
    print(f"The result of dice throw is: {choice}")
    play_again = input("Do you want to play again? (y/n) ").lower()
    if play_again == "n":
        break
