
def checkInput(num):
    if num.isdigit():
        if int(num) in range(1,10):
            return True
        else: 
            return False
    elif num.isalpha():
        return False



num = input("Type a number for X: ")
answerX = checkInput(num)
print(answerX)