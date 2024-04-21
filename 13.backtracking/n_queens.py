global total_nqueen
total_nqueen=0
def is_safe(board,row,col):
    start_col = col
    start_row = row
    bool_safe = True
  
    # upper direction
    while start_row>=0:
      if board[start_row][start_col] == 1:
        bool_safe = False
        return bool_safe
      start_row -=1
    # left direction
    start_col = col
    start_row = row
    while start_row>=0 and start_col>=0:
        if board[start_row][start_col] == 1:
            bool_safe = False
            return bool_safe
        start_row -=1
        start_col -=1
    
    # right diagonal
    start_col = col
    start_row = row
    while start_row>=0 and start_col<len(board):
      if board[start_row][start_col] == 1:
        bool_safe = False
        return bool_safe
      start_row -=1
      start_col +=1
    return bool_safe

    

    
def nqueens(board,row):
    if row==len(board):
        print_board(board)
        print("#"*20)
        global total_nqueen
        total_nqueen +=1
        return
    
    for col in range(len(board)):
        if is_safe(board,row,col):
            board[row][col]=1
            nqueens(board,row+1)
            board[row][col]=0










n=5
chess_board = [[0 for col in range(n)]for row in range(n)]


# chess_board = []
# for i in range(n):
#     board = []
#     for j in range(n):
#         board.append(0)
#     chess_board.append(board)



def print_board(board):
    n = len(board)
    for row in range(n):
        for col in range(n):
            if board[row][col] == 1:
                print("Q",end=" ")
            else:
                print("_",end=" ")
        print()
    

# print_board(chess_board)
nqueens(chess_board,0)
print(total_nqueen)