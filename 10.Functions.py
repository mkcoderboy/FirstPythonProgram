
#Functions is a collection of code that perfromes a specific task
#So we can take a bunch of line of code that are doing one thing and put them inside a function and when I wanted to do that task, I can call upon that function instead of writing the
# entire code again and again whenever I need that function performed.

#Key word to write a function in python is "def"

def say_hi():
    print("Hello User")

say_hi()

#We can give these functions information and  these are called parameters.
          #Parameter
def say_hi2(name):
    print(name)
#So now when we call this function, we will need to tell it what name to give it

say_hi2("Aahil")

#We can pass multiple parameters in a single function
def say_hi3(name, age, height):
    print("Hello " + name + " You are " + age + " Year old " + "And " + height + " inches tall.")

say_hi3("Aahil", "1", "30")

#IF you want to pass numbers for the parameters, add str(string) to that parameter when you print it.
def say_hi3(name, age, height):
    print("Hello " + name + " You are " + str(age) + " Year old " + "And " + height + " inches tall.")

say_hi3("Aahil", 1 , "30")


