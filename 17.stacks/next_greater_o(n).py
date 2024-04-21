from collections import deque
stack = deque()

def next_greater(arr,stack):
    n = len(arr)
    nxt_greater = [0 for _ in range(n)]
    
    for i in range(n-1,-1,-1):
        while len(stack) and arr[stack[len(stack)-1]] <= arr[i]:
            stack.pop()
        if not len(stack):
            nxt_greater[i] = -1
        else:
            nxt_greater[i] = arr[stack[len(stack)-1]]
        stack.append(i)

    print(nxt_greater)   


arr = [6,8,0,1,3]
next_greater(arr,stack)
