# Importing math (Module) allows us to use many functions in python such as------------------------------------------------------
# sqrt, ceil, floor,

from math import*
#sqrt will get you the square root of the number
print(sqrt(36))
#floor function will round down the number
print(floor(3.9))
#ceil will round up the number
print(ceil(3.9))

#Absolute value function (Don't need to import math for the following functions)
my_Num = -5
print(abs(my_Num))
#Power function (This will raise the first number to the power of second number)
print(pow(3, 2))
print(pow(5, 9))
#Max function (It will return the larger of the two numbers we pass it)
print(max(5, 20))
#Min function (It will return the lower of the two numbers we pass it)
print(min(5, 20))
#Rounding function

#Python can print out all sorts of numbers unlike in java where we need a different object for different numbers--------
#Integer
print(2)
#Decimal
print(2.0326)
#Negative number
print(-2)

#Python can also do basic arithmetics-----------------------------------------------------------------------------------
#Addition
print(3+4)
#Subtraction
print(3-4)
#Division
print(10/2)
#Multiplication
print(10*2)

#Python Also follows rules of order of operations----------------------------------------------------------------------
#PEMDAS Parentheses, Exponents, Multiplication and Division (from left to right), Addition and Subtraction (from left to right)

print(3 * 2 +(2 * 5))

#Modulus Operator (Returns the remainder number)
#This is read as 10 mod 3. It divides first number by the second number and give us the remainder
print(10 % 3)

#Convert number into a string. This is helpful when we want to print out numbers along side strings
My_Number = 5
print(str(My_Number) + " This is a crazy number")

#Summary----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
from math import*

print(sqrt(25))
print(floor(3.9))
print(ceil(3.9))

print(abs(-10))
print(pow(5, 8))
print(max(3, 8))
print(min(3, 8))

print(10 % 5.1)

myNumber = 25

print(str(myNumber) + " Now this is a string instead of a number")
print(str(myNumber) + " What what what")

print(3 + 5)
print(3 - 5)
print(3 / 5)
print(3 * 5)
print(3 * 5 + (5 + 3))
