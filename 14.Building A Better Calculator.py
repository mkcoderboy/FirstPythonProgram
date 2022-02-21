
#We will create 3 variables to get input from the user.
#Variable 1 is the first number
#Variable 2 is the operator
#Variable 3 is the second number
#We have to add "float" to convert the string into a number because when the user inputs a number, python converts it into a string unless you specify  that we need a number.


num1 = float(input("Enter the first number: "))
operator = input("Enter the operator: ")
num2 = float(input("Enter the second number: "))

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(num1 / num2)
else:
    print("Operator in invalid")

