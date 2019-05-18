
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
            if board[i][j] == "X" or board[i][j] == "O":
                filled += 1
                # print(filled)
            elif board[i][j] == number: 
                board[i][j] = choice
                # print(board)

def checkWinOrDraw(player):
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
        print("Player '{}' is the winner!".format(player))
        

# Create a variable to count if number was equal than to increment.
# If increment is greater than 0 than return True and choice was correct
# else than False and choice was taken already

def getUserInput():
    numX = input("Choose a number for 'X': ")
    checkBoard("X", int(numX))
    checkWinOrDraw("X")
    printBoard()

    numO = input("Choose a number for 'O': ")
    checkBoard("O", int(numO))
    checkWinOrDraw("O")
    printBoard()
    getUserInput()

print()
print("*** Welcome to Tic-Tac-Toe ***")
printBoard()
getUserInput()