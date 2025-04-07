#something is wrong
player1_score = 300 
player2_score = 400
player3_score = 300

print(player1_score == player2_score) #have to use 2 eqaul signs, cuz using only 1 assigns variable value
print(player1_score < player3_score)
print(player1_score > player2_score)

#t: false
#t: false
#t: false

#how to fix it

player1_score = 300 
player2_score = 400
player3_score = 300

print(player1_score != player2_score) 
print(player1_score <= player3_score) 
print(player1_score >= player2_score)

#t: true
#t: true
#t: true