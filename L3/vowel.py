vowel_count = (input("Enter string: ")) #user inputs the string to count
count = 0 #letter count
Aa = 0  #count for Aa
Ee = 0  #count for Ee
Ii = 0  #count for Ii
Oo = 0  #count for Oo
Uu = 0  #count for Uu
for owel in vowel_count:
    if (owel in "aeiouAEIOU"):
        count += 1
for letters in vowel_count:
    if (letters in 'Aa'):
        Aa += 1
for vowels in vowel_count:
    if (vowels in "Ee"):
        Ee += 1
for vowel in vowel_count:
    if (vowel in "Uu"):
        Uu += 1
for vowls in vowel_count:
    if (vowls in "Ii"):
        Ii += 1        
for vwels in vowel_count:   
    if (vwels in "Oo"):
        Oo += 1

print("Number of vowels", count) #outputs vowel count
print("a = ", Aa) #outputs Aa count 
print("e = ", Ee) #outputs Ee count 
print("i = ", Ii) #outputs Ii count 
print("u = ", Uu) #outputs Uu count 
print("o = ", Oo) #outputs Oo count 
#4/16/25