coins = ['Bronze', 'Silver', 'Gold', 'Platinum']
coin = 'gold'
score = 10000

if score > 10000:
    if coin in ('Gold', 'Platinum'):
        print("You have reached level 3") #expected
    else:
        print("You have reached level 2")
elif score > 5000 and coin in coins:
    print("You have reached level 1. keep going")
else: 
    print("Increasse your score and collect coins to move up")

#t:You have reached level 1. keep going
#T:increase your score and collect coins to move up
#something needs to be fixed to print line 7



coins = ['Bronze', 'Silver', 'Gold', 'Platinum'] 
coin = 'Gold' #have to make sure they match
score = 10000

if score >= 10000: #add = sign
    if coin in ('Gold', 'Platinum'):
        print("You have reached level 3")
    else:
        print("You have reached level 2")
elif score > 5000 and coin in coins:
    print("You have reached level 1. keep going")
else: 
    print("Increasse your score and collect coins to move up")

#T: You have reached level 2 not what we want 
#t: You have reached level 3 