'''
data = input("What's your favorite color? ")
print("You said " + data)

print("What's your favorite color? ")
data = input()
print("You said " + data)
'''

# Making decisions - Conditional Statements
# Example bellow
'''
if some_condition is True:
    do_something
elif some_other_condition is True:
    do_something
else:
    do_something
'''

'''
name = input("What's the name? ")
if name == "Arya Stark":
    print("Valar Morghulis")
elif name == "John Snow":
    print("You know nothing")
else:
    print("Carry on")

# NO TOUCHING PLEASE---------------
from random import randint
choice = randint(1,10)
# NO TOUCHING PLEASE---------------

# YOUR CODE GOES HERE:
if choice == 7:
    print("lucky")
else:
    print("unlucky")
'''

'''
color = input("What is your fave color? ")
if color == "purple":
    print("excelent choice!")
elif color == "teal":
    print("not bad")
elif color == "seafoam":
    print("quite good")
elif color == "pure darkness":
    print("I like the way you think")
else:
    print("You MONSTER!")
'''

'''
animal = input("Enter your favorite animal: ")

if animal:
    print(f"{animal} is my favorite too!")
else:
    print("You didn't say anything.")
'''

city = input("Where do you live? ")

if city == "Los Angeles" or city == "los angeles":
    print("You live in California")
else:
    print("You live somewhere else.")