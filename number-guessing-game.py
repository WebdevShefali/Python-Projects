import random
import math

random_number = math.floor(random.random() * 100)
score = 0
while True:
    user_input = input("Guess a number between 0 and 100: ")
    if user_input.isdigit():
        user_input = int(user_input)
        if random_number == user_input:
            print("You guessed it right!")
            print("You guessed it in " + str(score) + " attempts!")
            break
        else:
            if user_input > random_number:
                print("You were above the number!")
            else:
                print("You were below the number!")
            score += 1
    else:
        print("Please enter a valid number")
