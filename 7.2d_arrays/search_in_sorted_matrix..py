def search_in_sorted_mat(mat,key):
    n = len(mat)
    row = 0
    col = n-1
    while row >=0 and row <n and col >=0 and col < n:
        val = mat[row][col]
        if key==val:
            print(f"{key} is {row}  and {col}")
            return 
        elif key < val:
            col = col-1
        else:
            row =row+1
    print(f"not found")

mat = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
search_in_sorted_mat(mat,60)


