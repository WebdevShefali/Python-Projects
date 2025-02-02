import random

options = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0


while True:
    user_input = input("Choose between rock, paper and scissors or type Q to quit: ")
    computer_choice = random.choice(options)
    if user_input.lower() == "q":
        print("You quit the game!")
        break
    if user_input.lower() not in options:
        print("Invalid input. Please choose rock, paper, or scissors.")
        continue
    if user_input.lower() == computer_choice:
        print("It's a draw!")
    elif (
        (user_input.lower() == "paper" and computer_choice == "rock")
        or (user_input.lower() == "scissors" and computer_choice == "paper")
        or (user_input.lower() == "rock" and computer_choice == "scissors")
    ):
        print("You won!")
        user_score += 1
    else:
        print("You lose!")
        computer_score += 1


print("Your score: " + str(user_score))
print("Computer score: " + str(computer_score))
