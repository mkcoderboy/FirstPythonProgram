
# To make a list we use  a regular Variable, but have to use straight brackets. This makes it a list.
# List are also indexed. 0,1,2,3 etc.

Numbers = [1,2,3,4,5,6,7,8,9,10]
Friends = ["kevin", "Karen", "Jim", "Oscar", "Toby"]

print(Numbers)
print(Friends)
print(Friends[1])

#Using a negative index starts the string from the end.

print(Friends[-1])
print(Friends[-2])
print(Friends[-3])

# We can also grab the elements in the list starting onwards from which ever index you want.
# [1:] This will grab the index 1 and onwards. So should give us Karena and Jim for this example
print(Friends[1:])

# We can also grab only a range of the elements (stop it at a specific element)
# # [1:3] This will grab index 1 and onwards, but will end it at index 3 which in this example will be OSCAR.
# This is read as, Grab elements upto but not inlcuding 3.
print(Friends[1:3])


# We can also modify an element(Change the name from kevin to Michael Scott)

FriendsList = ["kevin", "Karen", "Jim", "Oscar", "Toby"]

FriendsList[0] = "Michael Scott"
print(FriendsList)

#We can modify multiple elements at the same time

Kids_Names = ["Ayaan", "Alizay", "Shazain", "Inayah", "Nayel", "Aahil"]

Kids_Names[0:] = "Kirli", "Bia Majh", "Poopalot", "Chuaril", "Babu Khachra", "Popolopolo"
print(Kids_Names)
