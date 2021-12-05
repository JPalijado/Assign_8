import random

def initiateProgram():
    print("Welcome to the lottery!")
    moreData = "y"
    return moreData

def interactiveLoop(moreData):
    while moreData == "y":
        inputNum1 = str(input("\nEnter First Number (0-9): ")) 
        inputNum2 = str(input("Enter Second Number (0-9): "))
        inputNum3 = str(input("Enter Third Number (0-9): "))

        randomNum1 = random.randint(0,10)
        randomNum2 = random.randint(0,10)
        randomNum3 = random.randint(0,10)

        strRandomNum1 = str(randomNum1)
        strRandomNum2 = str(randomNum2)
        strRandomNum3 = str(randomNum3)

        if (inputNum1 and inputNum2 and inputNum3) in (strRandomNum1 and strRandomNum2 and strRandomNum3):
            print(f"Winner!")
        else:
            print(f"You loss, the winning lottery number is: {randomNum1}{randomNum2}{randomNum3}.")
        moreData = str(input("Try again? y/n: "))
    if moreData == "n":
        print("\nThank you for participating!")
        
moreData = initiateProgram()
interactiveLoop(moreData)