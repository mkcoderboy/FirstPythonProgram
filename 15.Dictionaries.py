
#Dictionaries allows us to store information in a kay-value pairs.
#Normal dictionaries have a word(Key) and a definition(Value) of the word, same way here the word is the key and the definition is the value the key opens.
#Create a program that converts a 3 digit month name into the full month name.
#Example: jan -> January
#Cannot have duplicate keys.
#Keys do not have to be strings, we can also use numbers

month_convertions = {
    "jan": "January",
    "feb": "Feburary ",
    "mar": "March",
    "apr": "April",
    "may": "May",
    "jun": "June",
    "jul": "July",
    "aug": "August",
    "sep": "September",
    "oct": "October",
    "nov": "November",
    "dec": "December"
}

#We can use a key to get the value of any of these in the dictionary
#Multiple ways of getting it from the dictionaries
#1.
print(month_convertions["feb"])
#2.This method allows us to pass in a default value to get printed out if the key is wrong
print(month_convertions.get("mar", "This is not a valid key"))
print(month_convertions.get("luv", "This is not a valid key"))

#Using numbers as keys in a dictionaries

month_convertions = {
    1: "January",
    2: "Feburary ",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}

