
print("Welcome To The Dundies Award Game! ")

game = input("Would you like to play the game? ")

if game.lower() != "yes":
    quit()

score = 0

question_answer = input("Who started the dundies award game? ")
if question_answer.lower() == "michael scott":
    print("Correct! ")
    score += 1
else:
    print("Incorect! ")

question_answer = input("Who won the dont go in after me award? ")
if question_answer.lower() == "kevin malone":
    print("Correct! ")
    score += 1
else:
    print("Incorrect! ")

question_answer = input("Who won the spicy curry award? ")
if question_answer.lower() == "kelly kapoor":
    print("Correct! ")
    score += 1
else:
    print("Incorrect! ")

question_answer = input("Who won the whitest sneakers award? ")
if question_answer == "pam beesley":
    print("Correct! ")
    score += 1
else:
    print("Incorrect! ")

print("Your total score is " + str(score/4 * 100) + "%" " out of 100%. ")




