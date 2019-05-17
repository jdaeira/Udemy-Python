answer = False
number = False


def correctAnswer(num):
    if num in range(1,11):
        return True
    else: 
        return False

def getInput():
    number2 = False
    num1 = input("Pick a number between 1 and 10: ")
    num1 = int(num1)
    number = correctAnswer(num1)
    if number == False:
        getInput()  

    while (number2 == False):
        num2 = input("Pick another number between 1 and 10: ")
        num2 = int(num2)
        number2 = correctAnswer(num2)
        if number2 == True:
            getInput()
        

number = False
count = 1

def checkCount(num):
    if num == 20:
        return True
    else:
        return False


while (number == False):
    print(count)
    count += 1
    number = checkCount(count)


getInput() 







