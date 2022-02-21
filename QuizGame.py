
print("Welcome To The Game")

game = input("Would you like to play the game? ")


if game.lower() != "yes":
    quit()

score = 0


print("Lets start the game! ")


answer = input("What is a CPU? ")
if answer.lower() == "central processing unit":
    print("Correct! ")
    score += 1
else:
    print("Incorrect! ")

answer = input("What is a GPU")
if answer.lower() == "graphics processing unit":
    print("Correct! ")
    score += 1
else:
    print("Incorrect! ")

answer = input("What is RAM? ")

if answer.lower() == "random access memory":
    print("Correct! ")
    score += 1
else:
    print("Incorrect! ")

print("Your score is " + str(score/3 * 100) + " out of 3 questions")




