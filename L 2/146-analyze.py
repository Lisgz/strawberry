x = 500
y = 200
z = (1,2,3,5,8)
print(x % 6) #what will this result be? 2

x *= 3 
print(x) # what will this result be? 1500

print(x > y and x in z) #what will this result be? false

print(x/5 > y or y not in z) #what will this result be? true
#not takes precedence over or