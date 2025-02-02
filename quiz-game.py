print("Welcome to the quiz game!")
print("Answer the following questions to win!")
start = input("Do you want to start the quiz? (yes/no) ").lower()
if start == "yes":
    print("Great! Let's start!")
    score = 0
    answer = input("What does CPU stand for?").lower()
    if answer == "central processing unit":
        score += 1
    answer = input(
        "Which part of the computer is responsible for long-term storage?"
    ).lower()
    if answer == "hard drive":
        score += 1
    answer = input("What does RAM stand for?").lower()
    if answer == "random access memory":
        score += 1
    answer = input("What does GPU stand for?").lower()
    if answer == "graphics processing unit":
        score += 1
    answer = input("What does PSU stand for?").lower()
    if answer == "power supply unit":
        score += 1
    print("Your total score: " + str(score))
    print("You got " + str((score / 5) * 100) + "%")
    print("Thanks for playing!")
else:
    print("Okay, maybe next time!")
