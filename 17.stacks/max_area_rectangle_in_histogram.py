from collections import deque


def get_nxt_smaller_right(heights):
    n = len(heights)
    nxt_smaller_right = [0 for _ in range(n)]
    stack = deque()
    for i in range(n-1,-1,-1):
        while len(stack) and heights[stack[len(stack)-1]] >= heights[i]:
            stack.pop()
        if not len(stack):
            nxt_smaller_right[i] = n
        else:
            nxt_smaller_right[i] = stack[len(stack)-1]
        stack.append(i)
    return nxt_smaller_right

def get_nxt_smaller_left(heights):
    n = len(heights)
    nxt_smaller_left = [0 for _ in range(n)]
    stack = deque()
    for i in range(0,n):
        while len(stack) and heights[stack[len(stack)-1]] >= heights[i]:
            stack.pop()
        if not len(stack):
            nxt_smaller_left[i] = -1
        else:
            nxt_smaller_left[i] = stack[len(stack)-1]
        stack.append(i)
    return nxt_smaller_left

def max_area_rectangle_in_histogram(heights):
    n = len(heights)
    nxt_smaller_left = get_nxt_smaller_left(heights)
    nxt_smaller_right = get_nxt_smaller_right(heights)
    max_area = -9999
    for i in range(n):
        width = nxt_smaller_right[i]-nxt_smaller_left[i]-1
        area = width* heights[i]
        max_area = max(max_area,area)
    
    print(max_area)

heights = [2,1,5,6,2,3]
max_area_rectangle_in_histogram(heights)

