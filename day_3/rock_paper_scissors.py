# Richard Farr
# December 23rd, 2020
# Programming 101
# Day 3
# Exercise 1 - Rock, Paper, Scissors

# import the modules I will need
import random

# 1. Ask the user to pick rock, paper, or scissors by typing in the words
user_choice = input("Choose rock, paper, or scissors by typing in the word: ")
user_choice = user_choice.lower()
print(" ")
print(f"user choice is: {user_choice}") # optional step: display the choice

# 2. have the computer pick rock, paper, or scissors
choice = ["rock", "paper", "scissors"]
computer_choice = random.choice(choice).lower()
print(f"computer choice is: {computer_choice}") # optional step: display the choice
print(" ") # print a blank line


# 3. Logic to do comparisons to see who wins & print who the winner is

if computer_choice == user_choice:
    print("It's a tie")
elif computer_choice == "rock" and user_choice == "paper":
    print("User wins")
elif computer_choice == "rock" and user_choice == "scissors":
    print("Computer wins")
elif computer_choice == "paper" and user_choice == "rock":
    print("Computer wins")
elif computer_choice == "paper" and user_choice == "scissors":
    print("User wins")
elif computer_choice == "scissors" and user_choice == "rock":
    print("User wins")
elif computer_choice == "scissors" and user_choice == "paper":
    print("Computer wins")
else:
    print("please enter the words rock paper or scissors next time")

# print a blank line
print(" ")