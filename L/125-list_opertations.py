capitals=["Montgomery","Juneau", "Phoenix"]
capitals.append("Sacramento")#adds to the end of capitals
capitals.insert(3, "LittleRock") #adds to a specific spot
capitals.remove("Juneau")#doesn't work go to 126 to find to the right way.
population=[200000, 32000,1600000]
capitals[3]="Little Rock"#makes changes
print(capitals)
#ex: in capitals.append(), capitals is the object (or "toolbox") and append is the method (or "tool"). period= the mechanism that lets you access the append method specifically from the capitals object. Methods are functions that are tied to a specific object and are invoked using the period notation. append adds an item to the end of a list, 