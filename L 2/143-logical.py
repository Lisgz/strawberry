#something is wrong
gases = ('hydrogen', 'Helium' , 'Nitrogen' , 'Oxygen')
number_of_gases = 11
number_of_liquids = 2

print('Sodium' in gases and number_of_liquids < number_of_gases)

print('Hydrogen' in gases or 'Helium' in gases and number_of_liquids == 4) #after the and is false

#t: false
#t: true

#Logical operators involve using the keywords and, or, and not to compare two or more conditions 
# when using 'or' only one side of the statement has to be true to be considered true in the terminal

#fix it 
gases = ('hydrogen', 'Helium' , 'Nitrogen' , 'Oxygen')
number_of_gases = 11
number_of_liquids = 2

print('Sodium' not in gases and number_of_liquids < number_of_gases)

print(('Hydrogen' in gases or 'Helium' in gases) and number_of_liquids == 4)

#t: true
#t: false