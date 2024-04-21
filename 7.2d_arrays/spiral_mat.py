def spairal_mat(mat):
    print(mat)
    n = len(mat)
    row_start = 0
    row_end = n-1
    col_start = 0
    col_end = len(mat[0])-1
    
    while row_start <=row_end and col_start <= col_end:
        i=col_start
        while i <= col_end:
            print(mat[row_start][i],end=" ")
            i = i+1

        i=row_start+1
        while i<=row_end:
            print(mat[i][col_end],end=" ")
            i=i+1
        i=col_end-1
        while i >= col_start:
            print(mat[row_end][i],end=" ")
            i -= 1
        i=row_end-1
        while i>row_start:
            print(mat[i][col_start],end=" ")
            i -= 1
        row_start += 1
        row_end -= 1
        col_start += 1
        col_end -= 1

# mat = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
# mat = [[1,2,3],[4,5,6],[7,8,9]]
mat = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
# mat = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
spairal_mat(mat)
