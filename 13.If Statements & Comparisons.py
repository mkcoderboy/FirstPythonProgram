
#We will use comparison operators ==, !=, <, >, <=, >=,
#This allows us to compare the numbers we provide and give us an answer to our query about those numbers.
#We can compare all different types of DataTypes. Numbers, Strings, booleans.
#Write a program that returns the maximum number from the numbers the user will input.

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(1, 20, 300))

#We can compare strings as well

def list_of_animals(word1, word2, word3):
    if word1 == word2 or word1 == word3:
        return "Both strings are same"
    else:
        return "Strings are different"

print(list_of_animals("dog", "cat", "fish"))


