# Fizz Buzz - Write a program that prints the numbers from 1 to 100. 
# But for multiples of three print “Fizz” instead of the number and for 
# the multiples of five print “Buzz”. For numbers which are multiples of 
# both three and five print “FizzBuzz”.

def fizz_buzz(end):
    for num in range(1, end + 1):
        if (num % 3 == 0) and (num % 5 == 0):
            print(f"Fizz-Buzz for {num}")
        elif (num % 3 == 0):
            print(f"Fizz for {num}")
        elif (num % 5 == 0):
            print(f"Buzz for {num}")
        else:
            print(num) 

fizz_buzz(100)

# Reverse a String - Enter a string and the program will reverse it and print it out.
def reverse_word(word):
    return word[::-1]

reverse = input("Enter a word or phrase to reverse: ")

print(reverse_word(reverse))

# Pig Latin - Pig Latin is a game of alterations played on the English language game. 
# To create the Pig Latin form of an English word the initial consonant sound is transposed 
# to the end of the word and an ay is affixed (Ex.: "banana" would yield anana-bay). 
# Read Wikipedia for more information on rules.


# Count Vowels - Enter a string and the program counts the number of vowels in the text. 
# For added complexity have it report a sum of each vowel found.


# Check if Palindrome - Checks if the string entered by the user is a palindrome. 
# That is that it reads the same forwards as backwards like “racecar”


# Count Words in a String - Counts the number of individual words in a string. 
# For added complexity read these strings in from a text file and generate a summary.