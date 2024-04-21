def grid_ways(grid,row,col):
    if row == len(grid)-1 and col == len(grid)-1:
        return 1
    if row == len(grid) or col == len(grid):
        return 0
    
    total_ways = grid_ways(grid,row+1,col)+grid_ways(grid,row,col+1)
    return total_ways


n=3
grid_board = [[0 for col in range(n)]for row in range(n)]
print(grid_ways(grid_board,0,0))