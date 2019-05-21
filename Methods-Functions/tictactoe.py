
board = [[7,8,9], [4,5,6], [1,2,3]]

def printBoard():
    print()
    for i in range(3):
        tempBoard = "" 
        for j in range(3):
            tempBoard += str(board[i][j]) + " | "
        print(tempBoard)
        
    print()


def checkBoard(choice, number):
    filled = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == number: 
                board[i][j] = choice
                filled += 1
    if filled == 0:
        return True
    else: 
        return False             

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
    

def getUserInput():
    filledO = True
    numX = input("Choose a number for 'X': ")
    filledX = checkBoard("X", int(numX))
    if filledX == True:
        print("That square has been taked. Try again")
        getUserInput()
    else:   
        checkWinOrDraw("X")
        printBoard()

    while (filledO == True): 
        numO = input("Choose a number for 'O': ")
        filledO = checkBoard("O", int(numO))
        if filledO == True:
            print("That square has been taked. Try again")
        else:
            checkWinOrDraw("O")
            printBoard()
            getUserInput()

print()
print("*** Welcome to Tic-Tac-Toe ***")
printBoard()
getUserInput()

# have to check if the input is valid
