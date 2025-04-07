coins = ['Bronze', 'Silver', 'Gold', 'Platinum'] #this line is a tuple cannot be edited
coin = 'Bronze'
score = 10000

if score > 10000:
    if coin in ('Gold', 'Platinum'):
        print("You have reached level 3")
    else:
        print("You have reached level 2")
elif score > 5000 and coin in coins:
    print("You have reached level 1. keep going")
else: 
    print("Increasse your score and collect coins to move up")
#T:you have reached level 1. keep going

#5-9 is a nested if - an if inside an if
#if you have a condition that leads to checking for anotehr condition, you have a need for a nested if.
