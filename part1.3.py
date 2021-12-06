import random

def initiateProgram():
    print("Welcome to the lottery!")
    moreData = "y"
    return moreData

def interactiveLoop(moreData):
    while moreData == "y":
        inputNum1 = int(input("\nEnter First Number (0-9): ")) 
        inputNum2 = int(input("Enter Second Number (0-9): "))
        inputNum3 = int(input("Enter Third Number (0-9): "))

        randomNum1 = random.randint(0,10)
        randomNum2 = random.randint(0,10)
        randomNum3 = random.randint(0,10)

        inputNumTotal = inputNum1 + inputNum2 + inputNum3
        randomNumTotal = randomNum1 + randomNum2 + randomNum3

        if inputNumTotal == randomNumTotal:
            print(f"Winner!")
        else:
            print(f"You loss, the winning lottery number is: {randomNum1}{randomNum2}{randomNum3}.")
        moreData = str(input("Try again? y/n: "))
    if moreData == "n":
        print("\nThank you for participating!")
        
moreData = initiateProgram()
interactiveLoop(moreData)