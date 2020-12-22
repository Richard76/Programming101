# PDX Code
# 101 - Day 2 - Lab 2
# Richard Farr
# December 22nd, 2020


'''
Magic 8 Ball

Let's write a program to simulate the classic "Magic Eight Ball"
'''

# Print a welcome screen to the user.
print(" ")
print("Welcome to the amazing Magic 8 Ball!")

# Prompt the user to ask the 8-ball a question.
print(" ")
input("What is your question?")

# Use the random module's random.choice() to choose a prediction.
predictions = [
    "prediction 1",
    "prediction 2",
    "prediction 3", 
    "Sorry, it is highly unlikely :("
]
import random

random_prediction = random.choice(predictions)

# Print Searching my magic globe...
print(" ")
print("Searching my magic globe...")


# Display the result of the prediction.
print(random_prediction)
print(" ")



# Advanced version 1
# Let the user choose if they want to ask a second question.
second_question = input("Do you want to ask a second question? (Y/N) ")

if second_question == "Y" or second_question == "yes" or second_question == "Yes":
    input("What is your second and final question? ")
    print("Searching magic globe...")
    print("")
    answer = random.choice(predictions)
    print(answer)
    print("talk soon")
else:
    print("cool, thanks for playing")
    print(" ")


# Advanced version 2
# Ask the user if they want to ask another question, using a while loop.