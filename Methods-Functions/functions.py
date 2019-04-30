
def hello():
    print("Hello World!")

def hello_name(name = "NAME"): # This is a default va;lue in case nothing is provided. Only occurs if nothing is passed
    print("Hello " + name + "!") 

def add_numbers(num1, num2):
    return num1 + num2

hello()

hello_name("John")

total = add_numbers(2, 3)
print("The total is: {}".format(total))

# Find out if the word dog is in a string?

sentence = "The dog jumped over the moon!"

def find_dog(words):
    for word in words.split():
        if word == "dog":
            print("The word dog is in the sentence!")
            return
    print("Did not find dog in the sentence!")

find_dog(sentence)

# or 

def dog_check(mystring):
    return "dog" in mystring.lower()

check = dog_check("My dog is always hungry")
print(check)

def pig_latin(word):
    first_letter = word[0].lower()
    
    # check if vowel
    if first_letter in "aeiou":
        pig_word = word + "ay"
    else:
        pig_word = word[1:] + first_letter + "ay"

    return pig_word

pigWord = pig_latin("apple")
print(pigWord)

