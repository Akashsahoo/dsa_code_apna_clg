class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Queue:
    head = None
    tail = None
    def enqueue(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
    def dequeue(self):
        if not self.head:
            print("queue is empty")
        else:
            deque_data = self.head.data
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                self.head = self.head.next
            print(deque_data)

    def print_queue(self):
        temp = self.head
        while temp:
            print(temp.data,end=" ")
            temp = temp.next
        print( )


queue = Queue()
for i in range(1,10):
    queue.enqueue(i)

queue.print_queue()

for i in range(1,10):
    queue.dequeue()
queue.dequeue()