from collections import deque

def interleave_two_halves_queues(queue):
    size = len(queue)
    count = 1
    queue2 = deque()
    while count <= size//2:
        data = queue.popleft()
        queue2.append(data)
        count += 1
    while len(queue2):
        data2 = queue2.popleft()
        queue.append(data2)
        data = queue.popleft()
        queue.append(data)
    
    











queue = deque()
for i in range(1,11):
    queue.append(i)
print(queue)
interleave_two_halves_queues(queue)
print(queue)