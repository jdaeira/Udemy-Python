
board = [[7,8,9], [4,5,6], [1,2,3]]

# Prints the TicTacToe Board
def printBoard():
    print()
    for i in range(3):
        tempBoard = "" 
        for j in range(3):
            tempBoard += str(board[i][j]) + " | "
        print(tempBoard)
        
    print()

# Checks if the input is valid by check if
# the input is a digit or a character(string)
def checkInput(num):
    if num.isdigit():
        if int(num) in range(1,10):
            return True
        else: 
            return False
    elif num.isalpha():
        return False

# Checks if number inputed is already in the board
def checkBoard(choice, number):
    filled = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == number: 
                board[i][j] = choice
                filled += 1
    if filled == 0:
        return False
    else: 
        return True            

# Checks is there is a Winner or a Draw
def checkWinOrDraw(player):
    filled = 0
    if (board[0][0] == "X" and board[0][1] == "X" and board[0][2] == "X") \
    or (board[1][0] == "X" and board[1][1] == "X" and board[1][2] == "X") \
    or (board[2][0] == "X" and board[2][1] == "X" and board[2][2] == "X") \
    or (board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X") \
    or (board[0][1] == "X" and board[1][1] == "X" and board[2][1] == "X") \
    or (board[0][2] == "X" and board[1][2] == "X" and board[2][2] == "X") \
    or (board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X") \
    or (board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X") \
    or (board[0][0] == "O" and board[0][1] == "O" and board[0][2] == "O") \
    or (board[1][0] == "O" and board[1][1] == "O" and board[1][2] == "O") \
    or (board[2][0] == "O" and board[2][1] == "O" and board[2][2] == "O") \
    or (board[0][0] == "O" and board[1][0] == "O" and board[2][0] == "O") \
    or (board[0][1] == "O" and board[1][1] == "O" and board[2][1] == "O") \
    or (board[0][2] == "O" and board[1][2] == "O" and board[2][2] == "O") \
    or (board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O") \
    or (board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O"):
        printBoard()
        print("Player '{}' is the winner!".format(player))
        print()
        exit()
    for i in range(3):
        for j in range(3):
            if board[i][j] == "X" or board[i][j] == "O":
                filled += 1
    if filled == 9:
        printBoard()
        print("The game is a DRAW! No Winner!")
        print()
        exit()

# Gets the userinput and runs various checks by calling the above functions    
def getUserInput():
    filledO = False
    answer0 = False
    numX = input("Choose a number for 'X': ")
    answerX = checkInput(numX)
    if answerX == False:
        print("Invalid Input. Try again!")
        getUserInput()
    filledX = checkBoard("X", int(numX))
    if filledX == False:
        print("That square has been taken. Try again")
        getUserInput()
    else:   
        checkWinOrDraw("X")
        printBoard()

    while (filledO == False or answer0 == False): 
        numO = input("Choose a number for 'O': ")
        answerO = checkInput(numO)
        if answerO == False:
            print("Invalid Input. Try again!")
        else:
            filledO = checkBoard("O", int(numO))
            if filledO == False:
                print("That square has been taken. Try again")
            else:
                checkWinOrDraw("O")
                printBoard()
                getUserInput()

        
# Starts running the program
print()
print("*** Welcome to Tic-Tac-Toe ***")
printBoard()
getUserInput()


