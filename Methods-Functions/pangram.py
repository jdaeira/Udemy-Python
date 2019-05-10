# Hard:

# Write a Python function to check whether a string is pangram or not.

# Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
# For example : "The quick brown fox jumps over the lazy dog"

# Hint: Look at the string module
import string

def ispangram(str1, alphabet=string.ascii_lowercase):
    nospaces = str1.replace(" ", "")
    letters_in = set()
    for letter in nospaces.lower():
        if letter in alphabet:
            letters_in.add(letter)

    sort_letters = sorted(letters_in)
    new_letters = "".join((str(s) for s in sort_letters))
    if new_letters == alphabet:
        return True
    else:
        return False

print(ispangram("The quick brown fox jumps over the lazy dog"))
print(ispangram("John da Eira"))

# True

# string.ascii_lowercase

# 'abcdefghijklmnopqrstuvwxyz'

# Great Job!

