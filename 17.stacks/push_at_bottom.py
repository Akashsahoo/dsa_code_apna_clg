from collections import deque

stack = deque()

# append() function to push
# element in the stack
stack.append('a')
stack.append('b')
stack.append('c')

print('Initial stack:')
print(stack)

#print(stack[len(stack)-1])
#print(stack.pop())
# print(stack.pop())
# print(stack.pop())

# print(stack)
# print(len(stack))

def push_at_bottom(stack,data):
    if len(stack) == 0:
        stack.append(data)
        
        return
    top = stack.pop()
    push_at_bottom(stack,data)
    stack.append(top)

push_at_bottom(stack,'d')
print(stack)

