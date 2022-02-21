
#Using return statement in functions
#Return statement is used when you have a function and you call upon that function and you want to get some information from that function.

#Let's create a function that cubes a number. (power of 3)

def cube(num1):
    num1*num1*num1

print(cube(2))
#So this is not giving us anything back. We are not getting any information from the function.

#In order to get the value back to us when we call the function, we need to use return key word.
#once we write the return statement, we can no longer write anymore code in that function. Return statement breaks us out of the function.

def cube(num1):
    return num1*num1*num1

print(cube(3))


#We can also create a variable(result) that will store the value that get returned from the function.
#So the function will run and calculate the cube and then the answer will get stored in the variable and we can print the variable to get the value the function calculated.

def cube(num1):
    return num1*num1*num1

result = cube(4)

print(result)



