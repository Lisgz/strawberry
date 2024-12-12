import random

number = random.randint(1,100)
print(number)
userInput = None
Attempts = 10
currentAttempt = 0


while userInput != number:
        while currentAttempt < Attempts:
            userInput = int(input("Enter Guess: "))
            if (userInput < number):
               print(currentAttempt)
               print("too low go higher")
               currentAttempt = currentAttempt+1
            elif (userInput > number):
                print(currentAttempt)
                print("too high go lower")
                currentAttempt = currentAttempt+1
            if currentAttempt >= Attempts:
                print("you lose")
                break
