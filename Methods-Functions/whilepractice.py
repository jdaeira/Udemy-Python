answer = False
number = True

def correctAnswer(num):
    if num in range(1,11):
        return True
    else: 
        return False

while (number == True):
    num1 = input("Pick a number between 1 and 10: ")
    num1 = int(num1)
    number = correctAnswer(num1)
    print(number)

    while (number == True):
        num2 = input("Pick another number between 1 and 10: ")
        num2 = int(num2)
        number = correctAnswer(num2)
        print(number)
        
        




