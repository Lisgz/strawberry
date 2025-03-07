#In arithmetic, the order of operations dictates that multiplication occurs before addition.

base = 4000
rank = 3
bonus = 500

total_score = base + bonus * rank
print(total_score)
# t: 5500 needs to be 13500 
#math doesn't always go left to right

#how to fix it
base = 4000
rank = 3
bonus = 500

total_score = (base + bonus) * rank
print(total_score)
#t:13500