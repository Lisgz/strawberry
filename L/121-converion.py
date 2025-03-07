#rating is supposed to be a whole number
rating = float(input("Enter a rating between 1 and 5"))
points = int(rating) * 100 #add int so it comes back a whole number(my note)
print("You have " + str(points) + " to start.")
#an error messsage will pop up if you combine an interger with a string (my note)

#review: converting data types is necessary to make data usable in a situation.
#Data captured via inputs are strings of fata, so if we use input data in numeric calculations, the data needs to be converted to a number.
#finally, python cannot convert what is not possible such as a string, entered as a float to an integar, at least not through the int function.