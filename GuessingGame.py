/*Generate random number and tracking how many times it takes the user to guess the number

import random

top_of_range = input("type a number: ")

/*When user inputs the number, python will return it as a string, so we have to convert it to an int.*/
/* isdigit fuction checks if the input is a digit or not. itwill return TRUE or FALSE because its a boolean function*/

if top_of_range.isdigit():
	top_of_range = int(top_of_range)
	
/*Now we will check if input is larger then zero or not.
if top_of_range < 0:
	print("Enter a number larger then 0")
	quit()

else: 
	print("Please enter a number next time: ")
	quit()

random_number = random.randint(0, top_of_range)
print(random_number)

/* Now we need to keep asking user to asking number until corrrect

guesses = 0


while True:				
	guesses += 1
	user_guess = input("Make a guess: ")
	
	if user_guess.isdigit():
		user_guess = int(user_guess)
	
	else: 
		print("Enter a number next time! ")
	
	/*Continue brings us back to the top of the loop and run again   	   
		continue 
	
	if user_guess == random_number:
	 	print("Correct! ")
	
	break
	
	/*This will tell the user if their guess was higher or lower then the random number. 
	
	elif user_guess > random_number:
		print("You were above the number")
	
	else:
		print("You were below the number")
			 
		


print("You got it in " + str(user_guesses) + "tries!")



NOTES
-----------------------------------------------------------------
					//Bottom of range and Top of range (-0, 10)
r = random.randrange(-5, 11)

print(r)
/* When you run this, it will produce a random number every time between -5 and 11 but not including these two numbers. 

r = random.randint(-5, 11)
print(r)
/*This will do the samething, but will inclde the -5 and 11. 
 



						
