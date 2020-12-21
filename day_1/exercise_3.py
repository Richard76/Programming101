""" 
Using one or more string methods:

3.1
Capitalize a word

word: bicycle
output: Bicycle

word: guitar
output: Guitar

word: enveleope
output: Envelope

3.2
Display a word in all capital letters and all lowercase letters

word: vIoLiN
output: VIOLIN violin
3.3
Exchange all instances of a letter within a word with a different

word: Mississippi

...exchange 's' for 'z'...

output: Mizzizzippi
"""

# 1
print("bicycle".capitalize())

# 2
print("vIoLiN".upper() + " " + "vIoLiN".lower())

# 3
print("Mississippi".replace("s", "z"))

