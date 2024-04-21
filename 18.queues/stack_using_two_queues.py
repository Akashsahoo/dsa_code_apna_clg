from collections import deque

class Stack:
    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()
    def push(self,data):
        queue =  self.queue1 if not len(self.queue2) else self.queue2
        queue.append(data)
    
    def pop(self):
        if not len(self.queue1) and not len(self.queue2):
            print("stack is empty")
            return None
        queue1 =  self.queue1 if not len(self.queue2) else self.queue2
        queue2  = self.queue2 if queue1==self.queue1 else self.queue1
        
        while len(queue1)>1:
            queue2.append(queue1.popleft())

        pop_data = queue1.popleft()
        print(pop_data)
        return pop_data

stack = Stack()
for i in range(1,10):
    stack.push(i)


for _ in range(1,10):
    stack.pop()       
        
stack.pop()
stack.push(100)
stack.pop()
