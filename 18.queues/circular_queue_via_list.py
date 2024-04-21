class CircularQueue:
    def __init__(self,size):
        self.size = size
        self.front = -1
        self.rear = -1
        self.circular_queue = [None for _ in range(size)]

    def is_empty(self):
        if self.front == -1:
            return True
        return False
    
    def is_full(self):
        if (self.rear+1)%self.size == self.front:
            return True
        else:
            return False

    def peek(self):
        if not self.is_empty():
           return self.circular_queue[self.front]
        return None

    def enqueue(self,data):
        if self.is_empty():
            self.front = self.rear = self.rear+1
            self.circular_queue[self.front] = data
        elif self.is_full():
            print("queue is full")
            return
        else:
            self.rear = (self.rear+1)%self.size
            self.circular_queue[self.rear] = data
        self.display()
    
    def dequeue(self):
        if self.is_empty():
            print("queue is empty")
            return
        elif self.front==self.rear:
             dequeue_data = self.circular_queue[self.rear]
             self.circular_queue[self.rear] = None
             self.front = -1
             self.rear = -1
             print(dequeue_data)
        else:
            dequeue_data = self.circular_queue[self.front]
            self.circular_queue[self.front] = None
            self.front = (self.front +1)%self.size
            print(dequeue_data)
        self.display()
    
    def display(self):
        print(self.circular_queue)
           

ob = CircularQueue(5)
ob.enqueue(14)
ob.enqueue(22)
ob.enqueue(13)
ob.enqueue(18)
ob.enqueue(45)
ob.dequeue()
ob.dequeue()
ob.enqueue(114)
ob.enqueue(212)
ob.dequeue()
ob.dequeue()
ob.dequeue()
ob.dequeue()
ob.dequeue()
ob.dequeue()

        
    
         



