# Functions and Methods Homework

# Complete the following questions:

# Write a function that computes the volume of a sphere given its radius.

# The volume of a sphere is given as
# 43π𝑟3

def vol(rad):
    return (4 * 3.14) * (rad ** 3) / 3


print(vol(2))

# 33.49333333333333

# Write a function that checks whether a number is in a given range (inclusive of high and low)

def ran_check(num,low,high):
    if low < num < high:
        return "{} is in the range between {} and {}".format(num, low, high)
    else:
        return "{} in not in the range between {} and {}".format(num, low, high)
    

# Check

print(ran_check(5,2,7))

# 5 is in the range between 2 and 7

# If you only wanted to return a boolean:

def ran_bool(num,low,high):
    return low < num < high    

print(ran_bool(3,1,10))

# True

# Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.

# Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
# Expected Output : 
# No. of Upper case characters : 4
# No. of Lower case Characters : 33

# HINT: Two string methods that might prove useful: .isupper() and .islower()

# If you feel ambitious, explore the Collections module to solve this problem!

def up_low(s):
    uppers = 0
    lowers = 0

    for letter in s:
        if letter.isupper():
            uppers += 1
        elif letter.islower():
            lowers += 1
    
    print("No. of Upper case characters : " + str(uppers))
    print("No. of Lower case Characters : " + str(lowers))
    

s = 'Hello Mr. Rogers, how are you this fine Tuesday?'

up_low(s)

# Original String :  Hello Mr. Rogers, how are you this fine Tuesday?
# No. of Upper case characters :  4
# No. of Lower case Characters :  33


# Write a Python function that takes a list and returns a new list with unique elements of the first list.

# Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]

def unique_list(lst):
    return list(set(lst))

print(unique_list([1,1,1,1,2,2,3,3,3,3,4,5]))

# [1, 2, 3, 4, 5]


# Write a Python function to multiply all the numbers in a list.

# Sample List : [1, 2, 3, -4]
# Expected Output : -24

def multiply(numbers):  
    total = numbers[0]
    
    for num in range(1, len(numbers)):
        total *= numbers[num]
    
    return total

print(multiply([1,2,3,-4]))

# -24


# Write a Python function that checks whether a passed in string is palindrome or not.

# Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.

def palindrome(s):
    backword = s[::-1]
    if backword == s:
        return True
    else:
        return False
    

print(palindrome('helleh'))

# True

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

