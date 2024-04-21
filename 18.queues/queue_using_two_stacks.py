from collections import deque


class Queue: 
    def __init__(self):
        self.stack1 = deque()
        self.stack2 = deque()
    def enqueue(self,data):
        self.stack1.append(data)

    def dequeue(self):
        if not len(self.stack1):
            print("queue is empty")
            return
             
        while len(self.stack1):
            pop_data = self.stack1.pop()
            self.stack2.append(pop_data)
        data = self.stack2.pop()
        while len(self.stack2):
            pop_data = self.stack2.pop()
            self.stack1.append(pop_data)
        print(data)
        return data



queue = Queue()
for i in range(1,10):
    queue.enqueue(i)

for i in range(1,10):
    queue.dequeue()

queue.dequeue()

