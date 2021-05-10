# Rock Paper Scissors

import random

# Book - List
# Chapter - Element
# Page number - Index value
choices = ["rock", "paper", "scissors"]

rounds = int(input("How many rounds do you want to play? "))
win_counter = 0

while rounds != 0:
    print("- Rock\n- Paper\n- Scissors") # \n - newline
    player = input("Enter your choice: ").lower()

    if player not in choices: # if player's choice is not in available choices
        print("Invalid choice!")
        continue

    computer = random.choice(choices)

    # Tie condition
    if player == computer:
        print("It's a tie!")

    # Rock: Paper loses, Scissors win
    if player == "rock":
        if computer == "paper":
            print("You have lost! Paper wraps rock.")
        if computer == "scissors":
            print("You have won! Rock smashes scissors.")
            win_counter = win_counter + 1

    # Paper: Scissors lose, Rock wins
    if player == "paper":
        if computer == "scissors":
            print("You have lost! Scissors cut paper.")
        if computer == "rock":
            print("You have won! Paper wraps rock.")
            win_counter = win_counter + 1

    # Scissors: Rock loses, Paper wins
    if player == "scissors":
        if computer == "rock":
            print("You have lost! Rock smashes scissors.")
        if computer == "paper":
            print("You have won! Scissors cut paper.")
            win_counter = win_counter + 1

    rounds = rounds - 1

print(f"You have won {win_counter} times!")
