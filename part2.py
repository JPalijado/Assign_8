import random

def guessTheNumber():
    randomNum = random.randint(0, 101)
    inputNum = int(input("Guess the number (0-100): "))
    while inputNum != randomNum:
        if inputNum < randomNum:
            print("Greater than")
        else:
            print("Lower than")
        inputNum = int(input("Guess again: "))
    else:
        print("Correct!")

guessTheNumber()