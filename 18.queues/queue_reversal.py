from collections import deque
def reverse_queue(queue):
    print(queue)
    stack = deque()
    while len(queue):
       data = queue.popleft()
       stack.append(data)
    while len(stack):
        data = stack.pop()
        queue.append(data)
    print(queue)

queue = deque()
for i in range(1,11):
    queue.append(i)
    
reverse_queue(queue)