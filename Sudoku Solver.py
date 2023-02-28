board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def print_board (board):
    # Adds horizontal line to printed sudoku board
    for i in range (len(board)):
        if i%3==0 and i !=0:
            print("- - - - - - - - - - - -")

        #Adds vertical line to printed sudoku board 
        for j in range(len(board[0])):
            if j%3 == 0 and j !=0:
                print (" | ", end="")
                
        #Checks if we're at the last postion in line 
            if j==8:
                print(board[i][j])
            else:
                print(str(board[i][j])+ " ", end="")

def find_empty(board):
    for i in range (len(board)):
        for j in range (len(board[0])):
            if board[i][j]==0:
                return (i,j) #returns the row and column ((y,x) instead of (x,y)) of empty space
    return None

def valid (board,num,pos):
    for i in range(len(board[0])):
        if board[pos[0]][i]==num and pos[1] !=i:
            return False
    
    for i in range(len(board[0])):
        if board[i][pos[1]]==num and pos[0] !=i:
            return False
        
    box_x=pos[1]//3
    box_y= pos[0]//3

    for i in range (box_y*3,box_y*3+3):
        for j in range (box_x*3,box_x*3+3):
            if board[i][j]== num and (i,j) != pos:
                return False
    return True


def solver (board):
    #Uses backtracking algo to solve sudoku board
    empty=find_empty(board)
    if not empty:
        return True
    else :
        row,col = empty

    for i in range (1,10):
        if valid (board,i,(row,col)):
            board[row][col]=i

            if solver(board):
                return True
        
            board[row][col]=0
    return False

print(print_board(board))
solver(board)
print("\n")
print(print_board(board))
