'''
NAME: UGALE GANESH DHONDIRAM
CLASS: BE (COMP)
ROLL NO: 35
SUB: DAA
EXPERIMENT NO: 05
'''

def is_safe(board, row, col, n):
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, n), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True

def solve_nqueens(board, col, n):
    if col >= n:
        return True
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            if solve_nqueens(board, col + 1, n):
                return True
            board[i][col] = 0  # Backtrack
    return False

def print_board(board):
    for row in board:
        print(" ".join("Q" if cell == 1 else "." for cell in row))

# Main program
n = int(input("Enter the size of the board: "))
board = [[0] * n for _ in range(n)]

if solve_nqueens(board, 0, n):
    print_board(board)
else:
    print("Solution does not exist.")
    
    
'''

OUTPUT:
Enter the size of the board: 8
Q . . . . . . .
. . . . . . Q .
. . . . Q . . .
. . . . . . . Q
. Q . . . . . .
. . . Q . . . .
. . . . . Q . .
. . Q . . . . .

'''