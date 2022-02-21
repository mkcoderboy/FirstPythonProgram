
lucky_numbers = [4, 8, 45, 16, 3, 42]
friends = ["Kevin", "Karen", "Jim", "Jim", "Jim", "Oscar", "Toby"]

#There are many functions that we can do with lists
#List of functions
# 1. Extend
# 2. Add
# 3. Insert
# 4. Remove anywhere from list
# 5. Remove last element
# 6. Element present or not
# 7. Count
# 8. Sort
# 9. Reverse
# 10. Copy
# 11. Clear
# --------------------------------------------------------------------------------------------------------------------------------------

#1. Extend the list (We can extend the list by adding a second list onto it)

# friends.extend(lucky_numbers)
# print(friends)

#2. Add an element to the end of a list if we don't want to add an entire list.

friends.append("Creed")
print(friends)

#3. Insert an element anywhere in the list

friends.insert(1, "Kelly")
print(friends)

#4. Remove an element anywhere from the list
friends.remove("Toby")
print(friends)

#5. Remove the last element from the list
friends.pop()
print(friends)

#6. Check if an element is present in the list (If element not present, it will give an error).

print(friends.index("Oscar"))
#print(friends.index("Popolopolo"))

#7. Check how many times a single element is present in the list
print(friends.count("Jim"))

#8. Sort out the list alphabetically or numerically(If you have numbers and strings in the same list, this wont work. They need to be separate)
friends.sort()
print(friends)

lucky_numbers.sort()
print(lucky_numbers)

#9. Reverse the list
friends.reverse()
print(friends)

#10. Copy a list to make it 2 lists.

friends2 = friends.copy()
print(friends2)


#11. Clearing an entire list
friends.clear()
print(friends)






