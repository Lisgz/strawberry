#dictionary example
coins = {
    "gold":100,
    "silver":50,
    "bronze":25,
}
print(coins)

#set example
regions = {"north", "south","east"}
regions.add("west")
print(regions)

#tuple example
char1_name=("Humphrey", 'cat')
char1_name=[1]="Dog" #will not work because their not immutable (my note)
#tuples are good for list that should not have their items changed.(notes)