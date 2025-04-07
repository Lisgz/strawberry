coins = ('Bronze', 'Silver', 'Platinum', 'Gold')
scepter = True
for coin in coins:

    if coin == 'Platinum' and scepter == True:
        print('Congratulation! The platinum coin will move you to the next level!')
        continue
    print('You possess a', coin, 'coin.')