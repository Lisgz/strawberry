coins = ('Bronze', 'Silver', 'Platatinum', 'Gold')
for coin in coins:
    print ('You possess a', coin, 'coin.')
    if coin == 'Platinum':
        print('Congratulations! You move to the next level!')
        break #once platinum is possed it will move on to the  next level other cions dont matter
    #break ends a loop 