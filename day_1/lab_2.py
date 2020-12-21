'''
Write a simple program that prompts the user for several inputs then prints a Mad Lib as the result.

It can be a little tricky to find a plain-text Mad Lib that's easy to copy and paste. Instead, choose some song lyrics, a poem or quote, or create your own story.

Instructions
Choose some text to act as your Mad Lib
Ask the user for each word you'll put in your Mad Lib
Use an f-string to put each word into the Mad Lib

Example:
Give me an antonym for 'data': nonmaterial
Tell me an adjective: Bearded
Give me a sciency buzzword: half-stack
A type of animal (plural): parrots
Some Sciency thing: warp drive
Another sciency thing: Trilithium crystals
Sciency adjective: biochemical

Nonmaterial Scientist Job Description:

Seeking a bearded engineer, able to work on half-stack projects with a team of parrots.

Key responsibilities:
    - Extract patterns from non-material
    - Optimize warp drive
    - Transform trilithium crystals into biochemical material.
'''
# 1. Choose some text to act as your Mad Lib
# My favorite animal is a {animal}. My favorite person is {person}. My favorite hobby is {hobby}.

# 2. Ask the user for each word you'll put in your Mad Lib
animal = input("What animal is your favorite? ")
person = input("Who is your favorite famous person? ")
hobby = input("What do you like to do for fun? ")

# 2. Use an f-string to put each word into the Mad Lib
print(f'My favorite animal is a {animal}. My favorite person is {person}. My favorite hobby is {hobby}.')



'''
Advanced
Make a functional solution that utilizes lists. For example, ask the user for 3 adjectives, separated by commas,
 then use the .split() function to store each adjective and later use it in your story.
Add randomness! Use the random module, rather than selecting which adjective goes where in the story.
'''



'''
Super Advanced
Make it a repeatable game. Once you're done prompting the user for words, prompt them for whether they'd like to hear the story.
 Use a while loop to keep asking if they'd like to hear the story again until the answer is 'no'. You could then ask them if they'd like to make another story, and so on.
'''
