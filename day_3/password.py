# Richard Farr
# December 23rd, 2020
# Programming 101
# Day 3
# Exercise 2 - Pasword Generator

# import the modules that I will need later in the code
import string
import random

# Ask user how long to make the password
password_length = input("How many characters do you want your password to be? (minimum 3) ")

# Check to see length is at least 3... if it isnt then make it 10 & tell the user
if int(password_length) > 3:
     password_length = int(password_length)
     print("Good, you picked a password of length 3 or longer")
else:
    password_length = 10
    print("Sorry, you needed to pick 3 or greater, we are going to make it 10 characters long")

# Create a list of "letters" to create the password from
letters = string.ascii_letters + string.digits + string.punctuation
# print(letters)

# Create the variables that I will need to generate the password
count = 0 # starting length of password
chars = password_length # final length of password
word = "" # password before adding any characters

# Generate the password
while count < chars:
    word = word + random.choice(letters)
    count = count + 1

# Tell the user how long the new password is and what it is    
print(f"Your new password is: {password_length} characters long")
print(f"Your new password is: {word}")

