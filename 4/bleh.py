#from getpass import getpass

#num1 = input("Enter a number: ")
#num2 = input("Enter another number: ")
#result = float(num1) + float(num2)
#print(result)


#color = input("Enter a color: ")
##celebrity = input("Enter a celebrity: ")

#print("rose are   " + color)
#print(plural_noun + " are blue")
#print("I love " + celebrity)
#coordinates = (4, 5)
#print(coordinates[0])

#my_num = -5
#print(pow(4, 6))

#number_grid = [
   # [1, 2, 3],
  #  [4, 5, 6],
#[7, 8, 9],
   # [0]
#
#for row in number_grid:
    #for col in row:
        #print(col)

#def translate(phrase):
   # translation = ""
   # for letter in phrase:
    #    if letter in "AEIOUaeiou":
         #   translation = translation + "g"
       # else:
        #    translation = translation + letter
    #return translation

#print(translate(input("Enter a phrase:)))



try:
    answer = 10/0
    number = int(input("Enter a number"))
    print(number)
except ZeroDivisionError as err:
    print("err")
except ValueError:
    print("invalid input")
