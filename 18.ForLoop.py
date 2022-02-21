
#We loop through all the letters inside of the string.
#We can use for loops to loop through a collection of anything we have 1. Strings 2. Arrays
#Every iteration will pick up one letter in sequence.
#first iteration will pick up G
#Second iteration will pick up i and so on and so forth.

for letter in "Giraffe Academy":
    print(letter)

#This not only works with strings, but also works with Arrays.
#For each name inside of the friends arrays, I want to  print out the name.

friends = ["Jim", "Karen", "Kevin"]

for names in friends:
    print(names)

#We can use range to also loop through an array

for index in range(len(friends)):
    print(friends[index])


#We can also do this for numbers
#This will print out all the numbers from 0 to 10 but not including 10
for index in range(10):
    print(index)

#This will print numbers between 3 and 10 but not including 10
for index in range(3, 10):
    print(index)


#Can also include if statments in for loops

for index in range(5):
    if index == 0:
        print("first iteration")
    else:
        print("Not first")
