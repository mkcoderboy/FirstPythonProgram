
#Tuples are also like list, but we use parenthesis instead of straight brackets.
#Tuples are immutable(Can't be changed or modified, once they are made)
#Tuplues are used for data that will NEVER need to be modified after its creation.
#Tuplues are mostly used for data like coordinates, because coordinates don't need to be changed once you have them.
#Tuples are also indexed

coordinates = (4, 5)
print(coordinates[0])

#We can create a list of Tuples.

coordinates3 = [(1, 2), (3, 4), (5,6)]
print(coordinates3)


#we cannot change this once it is made. Python will give an error.
#Example:
coordinates2 = (6, 7)
coordinates[0] = 8
print(coordinates2)


