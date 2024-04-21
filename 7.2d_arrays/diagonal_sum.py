def digonal_sum(mat):
    n = len(mat)
    total_sum = 0
    for i in range(n):
        # for primary digognal
        total_sum += mat[i][i]
        # for secondary digognal
        if(i!=n-1-i):
            total_sum += mat[i][n-1-i]
    print(total_sum)

mat = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
digonal_sum(mat)
