def print_sudoku(board):
    n = len(board)
    for row in range(n):
        for col in range(n):
            print(board[row][col],end=" ")
        print()

def sudoku_solver(sudoku,row,col):
    
    next_row = row
   
    if col==len(sudoku):
        next_row = row+1
        col = 0
    if next_row==len(sudoku):
        print_sudoku(sudoku)
        return
    if sudoku[next_row][col] !=0:
       sudoku_solver(sudoku,next_row,col+1)
       return
       
    for num in range(1,10):
        if is_safe(sudoku,next_row,col,num):
           sudoku[next_row][col]=num
           sudoku_solver(sudoku,next_row,col+1)
           sudoku[next_row][col] =0

def is_safe(sudoku,row,col,num):
   
    bool_safe = True
    # check for row
    for row_index in range(len(sudoku)):
        
           if sudoku[row_index][col] == num:
              bool_safe = False
              return bool_safe
        
    # check for col
    for col_index in range(len(sudoku)):
        
            if sudoku[row][col_index] == num:
                bool_safe = False
                return bool_safe
    
    # check for 3 x 3 grid 
    start_row = (row//3)*3
    end_row = start_row+3

    start_col = (col//3)*3
    end_col = start_col +3
    
    while start_row < end_row:
        i = start_col
        while i < end_col:
            
            if sudoku[start_row][i] == num:
                bool_safe = False
                return bool_safe
            i +=1
        start_row +=1
    return bool_safe






grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]]


sudoku_solver(grid,0,0)




    
