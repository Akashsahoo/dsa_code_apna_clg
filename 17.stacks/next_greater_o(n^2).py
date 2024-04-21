def next_greater(arr):
    nxt_greater = []
    for i in range(len(arr)):
        j=i+1
        while j<len(arr) and arr[j]<=arr[i]:
            j=j+1
        if j==len(arr):
            nxt_greater.append(-1)
        else:
            nxt_greater.append(arr[j])
    print(nxt_greater)

arr = [6,8,0,1,3]
next_greater(arr)