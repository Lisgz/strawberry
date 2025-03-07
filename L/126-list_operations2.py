capitals=["Montgomery", "Juneau", "Phoenix"]
capitals.append("Sacramento")
capitals.insert(3,"LittleRock")
capitals.remove("Juneau") #when juneau is removed it goes Montgomery, Phoenix, LittleRock, Sacramento
population=[200000,32000,1600000]
capitals[3]="Little Rock"
capitals.reverse()#used to print the list backwards  (my notes)
capitals.sort()#prints the list back in abc order (my notes)
#capitals.sort(reverse=True) print the list backwards (my notes)
print(capitals.pop()) #empty remove sacramento 0 removes montgomery (my notes)
print(capitals)
print(max(population))#or min
print(len(capitals))#len=length
#every method in programming languages uses () (my notes)