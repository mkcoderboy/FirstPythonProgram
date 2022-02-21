
#First lets create a boolean variable

is_male = True

#We can use an if statement to check what the value of this variable is. IF its TRUE, it will print what we write in there, if not it wont.

if is_male:
    print("You are a male")


#So we have to other "else" statment in there as well, beacuse if condition is not true, then it should print something for us to let us know the condition is not true.
is_male = False

if is_male:
    print("You are a male")
else:
    print("You are not a male")


#We can make this more complex with multiple boolean variables.
#With multiple boolean variables, we will have to use the keywords "and" "or" "not" in the if statement.

is_male = False
is_tall = True

if is_male and is_tall:
    print("You are a tall male")
else:
    print("You are either not a male or not tall or both")


#Both conditions True
is_male = True
is_tall = True

if is_male or is_tall:
    print("You are either a male or are tall or both")
else:
    print("You are neither male nor tall")

#Both conditions False

is_male = False
is_tall = False

if is_male or is_tall:
    print("You are either a male or are tall")
else:
    print("You are either not a male or not tall or both")


#

is_male = True
is_tall = False

if is_male and is_tall:
    print("You are either a male or are tall")
else:
    print("You are either not a male or not tall")


#What if we want to check if they are male and not tall. We can use another condition called (else if "elif")

is_male = True
is_tall = False

if is_male and is_tall:
   print("You are either a male or are tall")


elif is_male and not(is_tall):
   print("You are a male but not tall (short male)")

elif not(is_male) and is_tall:
    print("You are tall but not a male")

else:
    print("You are not a male or tall")