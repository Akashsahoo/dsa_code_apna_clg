class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        


class LinkList:
    head = None
    tail = None
    size = 0

    def add_first(self,data):
        new_node = Node(data)
        if not self.head:
            self.tail = self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size +=1

    def add_last(self,data):
        new_node = Node(data)
        if not self.head:
            self.tail = self.head = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size +=1
    
    def add_middle(self,data,index):
        new_node = Node(data)
        if not self.head:
            self.tail = self.head = new_node
        else:
            count = 0
            temp = self.head
            while count < index-1:
                temp = temp.next
                count +=1
                
                
            new_node.next = temp.next
            temp.next = new_node 

        self.size +=1
    
    def remove_first(self):
        if not self.head:
            return None
        elif self.head==self.tail:
            self.tail = self.head = None
        else:
            self.head = self.head.next
        self.size -= 1
    
    def remove_last(self):
        if not self.head:
            return None
        elif self.head==self.tail:
            self.tail = self.head = None
        else:
            temp = self.head
            while temp.next!=self.tail:
                temp = temp.next
            
            temp.next = None
            self.tail = temp
        self.size -= 1
    
    def remove_middle(self,index):
        if not self.head:
            return None
        count = 0
        temp = self.head
        while count < index-1:
            temp = temp.next
            count += 1
        if temp.next == self.tail:
            temp.next = None
            self.tail = temp
        else:
            temp.next = temp.next.next
        self.size -= 1



    def print_ll(self):
        temp = self.head
        while temp:
            print(temp.data,end="->")
            temp = temp.next
        print()
        print(self.size)


ll = LinkList()
node = Node(0)

ll.head = node
ll.tail = node
ll.add_first(1)
ll.add_last(2)
ll.add_last(3)
ll.add_last(4)
ll.add_last(5)
ll.print_ll()

# ll.add_middle(-3,3)
# ll.print_ll()
# ll.remove_first()
# ll.print_ll()
  
# ll.remove_last()
# ll.print_ll()

ll.remove_middle(2)
ll.print_ll()





    
    