
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
    otherChoice = ""
    if choice == "X":
        otherChoice = "O"
    else: 
        otherChoice == "X"
    for i in range(3):
        for j in range(3):
            if board[i][j] == choice or board[i][j] == otherChoice:
                print("That square has been filled")
            elif board[i][j] == number: 
                board[i][j] = choice
                print(board)


# Create a variable to count if number was equal than to increment.
# If increment is greater than 0 than return True and choice was correct
# else than False and choice was taken already

printBoard()

board[0][0] = "X"
board[2][2] = "O"
board[1][1] = "X"

checkBoard("X", 2)

printBoard()