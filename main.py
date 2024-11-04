import random

# Mapping numbers to choices
options = {1: "rock", 2: "paper", 3: "scissors"}

while True:
    # Display options to the user
    print("\nChoose an option:")
    print("1: Rock")
    print("2: Paper")
    print("3: Scissors")
    print("Enter '0' to quit")

    # Get user choice
    try:
        user_choice = int(input("Your choice (1/2/3): "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    # Handle quitting the game
    if user_choice == 0:
        print("Thanks for playing!")
        break

    # Validate user choice
    if user_choice not in options:
        print("Invalid choice. Please choose 1, 2, or 3.")
        continue

    # Random choice for computer
    computer_choice = random.randint(1, 3)
    print(f"\nYou chose {options[user_choice]}")
    print(f"Computer chose {options[computer_choice]}")

    # Determine the outcome
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 1 and computer_choice == 3) or \
         (user_choice == 2 and computer_choice == 1) or \
         (user_choice == 3 and computer_choice == 2):
        print("You win!")
    else:
        print("You lose!")

"""
This program allows the user to play the game of Rock, Paper, Scissors against the computer.
The user is prompted to choose an option (rock, paper, or scissors) by entering a number.
The computer then randomly selects an option.
The program determines the outcome of the game and displays the result to the user.
The game continues until the user chooses to quit by entering '0'.
"""
