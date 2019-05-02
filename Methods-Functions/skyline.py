
def myfunc(word):
    newWord = ""
    for num in range(len(word)):
        if num % 2 == 0:
            newWord = newWord + word[num].upper()
        else:
            newWord = newWord + word[num].lower() 
    return newWord      


myNewWord = myfunc("Google")
print(myNewWord)

