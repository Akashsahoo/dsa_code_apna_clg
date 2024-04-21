class Node:
    prev_node = None
    next_node = None
    
    def __init__(self,data):
        self.data = data

class Doublyll:
    head = None
    tail = None
    def add_first(self,data):
        new_node = Node(data)
        if not self.head:
           self.head = self.tail = new_node
        else:
            new_node.next_node = self.head
            self.head.prev_node = new_node
            self.head = new_node
    def add_last(self,data):
        new_node = Node(data)
        if not self.head:
           self.head = self.tail = new_node
        else:
            new_node.prev_node = self.tail
            self.tail.next_node = new_node
            self.tail = new_node

    def remove_first(self):
        if not self.head:
            return 
        self.head.next_node.prev_node = None
        self.head = self.head.next_node
    
    def remove_last(self):
        if not self.head:
            return 
        new_tail = self.tail.prev_node
        self.tail.prev_node.next_node = None
        self.tail.prev_node = None
        self.tail = new_tail
        
    def reverse(self):
        if not self.head:
            return 
        if not self.head.next_node:
            return 
        prev = None
        self.tail = temp = self.head
         
        while temp:
            next_node = temp.next_node
            temp.next_node = prev
            temp.prev_node = next_node
            prev = temp
            temp = next_node
        self.head = prev



    def print_ll(self):
        if not self.head:
            return
        temp = self.head
        while temp:
            print(f"<-{temp.data}",end="->")
            temp = temp.next_node
        print()
    
    def print_backward(self):
        if not self.head:
            return
        temp = self.tail
        while temp:
            print(f"<-{temp.data}",end="->")
            temp = temp.prev_node
        print()


dll = Doublyll()
dll.add_first(1)
dll.add_first(2)
dll.add_first(3)
dll.add_first(4)
dll.add_first(5)
# dll.remove_first()
# dll.remove_last()
dll.reverse()
dll.print_ll()
dll.print_backward()