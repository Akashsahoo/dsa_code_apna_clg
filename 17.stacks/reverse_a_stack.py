from collections import deque

stack = deque()

stack.append(1)
stack.append(2)
stack.append(3)

print(stack)

def push_at_bottom(stack,data):
    if len(stack) == 0:
        stack.append(data)
        return
    top = stack.pop()
    push_at_bottom(stack,data)
    stack.append(top)

def reverse_stack(stack):
    if len(stack)==0:
        return
    top = stack.pop()
    reverse_stack(stack)
    push_at_bottom(stack,top)

reverse_stack(stack)
print(stack)

# O(n^2)