"""
Things we can do with Strings

1) \n = Adding a line between the string
2) create a String Variable
3) concatenation. We can attach(append) two strings together
4) Functions
4.1) .lower()
4.2) check if a string is totally upper case or if its not. It will give a True or False
4.3) combine functions togather
4.4) length of a string
4.5) individual letters from within the strings
4.6) index function
4.7) replace a letter or a word within a string
"""



# \n = Adding a line between the string

print("This is\nAahil")
print("This is\nAdeel")

# \" = Adds a quotation mark literally to the string
print("This is\"chota sa baby aahil\"")

# We can create a String Variable
phrase ="Baby Aahil"
print(phrase)


phrase2 = "Baby Aahil is super cool"
print(phrase2)

# We can also do concatenation. We can attach(append) two strings together.
print(phrase + " is ghanda bacha")

#We also have functions, which are block of codes we can run and it will perform a specific operation for us.
#Function allow us to modify our strings and get information about our strings
# .lower() will convert the string to lower case
print(phrase.lower())
#print(phrase.upper())

#We can also check if a string is totally upper case or if its not. It will give a True or False
print(phrase.isupper())

#We can also combine functions togather
print(phrase.upper().isupper())

#We can also figure out length of a string
print(len(phrase))

#We can also get individual letters from within the strings. Where a specific character is in the string?
#Within the brackets enter the index value of the string. Starts from 0.
print(phrase[0])

#We can also use index function. This allows us to find out where a specific character is in a string
print(phrase.index("b"))
print(phrase.index("Aah"))

#We can also replace a letter or a word within a string
print(phrase.replace("Baby", "Chota"))



Greetings = ("Hello World")

print(Greetings.isupper())
print(Greetings.islower())
print(Greetings.lower())

