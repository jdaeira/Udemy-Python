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

def pig_latin(sentence):
    pass


# Count Vowels - Enter a string and the program counts the number of vowels in the text. 
# For added complexity have it report a sum of each vowel found.

letter_list = []

def vowels_found(phrase):
    count = 0
    for letter in phrase:
        letter_list.append(letter)
    for letters in letter_list:
        if letters.lower() in 'aeiou':
            count += 1
    print(f"You have {count} vowels in the string!")

def vowels_count():

    acount = 0
    ecount = 0
    icount = 0
    ocount = 0
    ucount = 0
    for vowel in letter_list:
        if vowel.lower() == "a":
            acount += 1
        elif vowel.lower() == "e":
            ecount += 1
        elif vowel.lower() == "i":
            icount += 1   
        elif vowel.lower() == "o":
            ocount += 1
        elif vowel.lower() == "u":
            ucount += 1
    # Calls the function to print how many of each vowel
    print_count(acount, ecount, icount, ocount, ucount)


def print_count(a, e, i, o, u):
    if a > 0:
        print(f"a - {a}")
    if e > 0:
        print(f"e - {e}")
    if i > 0:
        print(f"i - {i}")
    if o > 0:
        print(f"o - {o}")
    if u > 0:
        print(f"u - {u}")


vowels_found("I am a Owl")
vowels_count()


# Check if Palindrome - Checks if the string entered by the user is a palindrome. 
# That is that it reads the same forwards as backwards like “racecar”

def palindrome(word):
    if word[::-1] == word:
        print("The word you entered is a palindrome!")
    else:
        print("The word you entered is not a palindrome")

palindrome("racecar")


# Count Words in a String - Counts the number of individual words in a string. 
# For added complexity read these strings in from a text file and generate a summary.

def number_words(sentence):
    word_count = sentence.split()
    print(f"There are {len(word_count)} words in the sentence!")

number_words("This is not a test!")

