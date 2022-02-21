
#We can specify a few different lines of code and then we can put that code inside of a "WhileLoop" and it would basically loop through that code executing it repeatedly
# until a certain condition is false.

#We will create a variable that is an integer(number)
#Syntax-> While condition

i = 1

#     Condition
while i <= 10:
    print(i)
    i = i + 1

print("Done with loop")
#We will keep looping through the code inside the while loop as long as the condition (i <= 10) is true.
#Every time it loops, it will add 1 to it because we told it to add 1 every time(i = i + 1)
#First time it loops, i will become 2 and when it loops again it will check if the condition is still true, 2 is < 10 so it will loop again and add 1 so i will become 3. This way
# it will keep looping until i becomes 11 and then the condition will become false because 11 is > 10 so then the loop will stop.