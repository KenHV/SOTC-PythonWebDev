# Rock Paper Scissors

import random

while True: # Infinite loop
    print("- Rock\n- Paper\n- Scissors") # \n - newline
    player = input("Enter your choice: ").lower()

    # Book - List
    # Chapter - Element
    # Page number - Index value
    choices = ["rock", "paper", "scissors"]
    computer = random.choice(choices)

    # Rock: Paper loses, Scissors win
    if player == "rock":
        if computer == "paper":
            print("You have lost! Paper wraps rock.")
        if computer == "scissors":
            print("You have won! Rock smashes scissors.")

    # Paper: Scissors lose, Rock wins
    if player == "paper":
        if computer == "scissors":
            print("You have lost! Scissors cut paper.")
        if computer == "rock":
            print("You have won! Paper wraps rock.")

    # Scissors: Rock loses, Paper wins
    if player == "scissors":
        if computer == "rock":
            print("You have lost! Rock smashes scissors.")
        if computer == "paper":
            print("You have won! Scissors cut paper.")

    play_again = input("Do you want to play again? (y/n) ").lower()
    if play_again == "y":
        continue
    if play_again == "n":
        break
