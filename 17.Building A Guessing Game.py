

secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False


while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

#Once the code comes out of the loop, the values that have changed for the variables remain changed and hold true for the next lins of code.
# The values do not reset after the loop ends.

if guess_count < guess_limit:
    print("You win!")
else:
    print("Out of guesses, you lost!")

#Another way to do the samething.

# if out_of_guesses:
#     print("Out of guesses, you lost!")
# else:
#     print("You win!")

