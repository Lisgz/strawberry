import random

number = random.randint(1,100)
guess = 10,
guess_count = 0,
guess_limit = 10,

while guess != number:
       if guess_count >= guess_limit:
              print("too many tries")
              break
       
while guess != number:
        guess = int(input("Enter Guess: "))
        if (guess < number):
                print("too low go higher")
        elif (guess > number):
                print("too high go lower")
        else:
            print("Guess right you win!!!!")
