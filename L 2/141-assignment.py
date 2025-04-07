score = 300 # - simple assignment
#t:True

score += 10 # - compound assignment (changes the value of a variable using an arithmetic operator)
print(score)
#t:310

score -= 20 
print(score)
#t:290

score *= 5
print(score)
#t:1450

#score /= 10
#print(score)
#t:145.0

score %= 4 # - modulus (which is the remainder of two numbers divided by each other) used to see if their are eany points left over
print(score)
#t:1.0

score = 300
score //=11 # - floor division
print(score)
# t:27

#exponents are done wiht 2 asterisks
score **=2
print(score)
#t:729

#operators are assessed from right to left

x = y = 2 
#first 2 is assigned to y and then y which is now 2 is assigned to x 
y = 2
#x = y += 2 
# which becomes 4 so now 4 = y