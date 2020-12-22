# Day 2 - Lab 1
# Richard Farr


# Let's convert a numerical score into a letter grade, using if and elif statements and comparisons.

# 1. Have the user enter a number representing the score (0-100)
grade = input("Please Enter a number between 0 and 100: ")
grade = float(grade)
print(grade)



# 2. Convert the score to a letter grade A - F

# 90-100: A
# 80-89: B
# 70-79: C
# 60-69: D
# 0-59: F

if grade >= 90:
    l_grade = "A"
elif grade >= 80:
    l_grade = "B"
elif grade >= 70:
    l_grade = "C"
elif grade >= 60:
    l_grade = "D"
else:
    l_grade = "F"

# 3. Print the output (extra)
print(f'Your grade is {l_grade}')


# Advanced

# 1. Use randint() from the random module to determine the user's rival's score. 
import random
rival_score = random.randint(0, 100)
print(f'Your rival scored a {rival_score}')

# 2. Let the user know if they did better than their rival.
if grade > rival_score:
    print("You did better than your rival")
else:
    print("Your rival did better than you")