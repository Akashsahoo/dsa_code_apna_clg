class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
def reverse(head):
    prev = None
    ll = LinkList()
    temp = head
    ll.tail = temp
    while temp:
        next_node = temp.next
        temp.next = prev
        prev = temp
        temp = next_node
    ll.head = prev
    return ll.head
    

class LinkList:
    head = None
    tail = None
    size = 0

    def add_last(self,data):
        new_node = Node(data)
        if not self.head:
            self.tail = self.head = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size +=1
    

    def print_ll(self):
        temp = self.head
        while temp:
            print(temp.data,end="->")
            temp = temp.next
        print()
        print(self.size)

    def get_middle_elem(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow
    
    
    def check_palendrom(self):
        if not self.head.next:
            return True
        mid_elem =  self.get_middle_elem()
        head1 = self.head
        
        reverse_head2 = reverse(mid_elem)
        while reverse_head2:
            if head1.data != reverse_head2.data:
               return False
            head1 = head1.next
            reverse_head2 = reverse_head2.next
        return True
    






ll = LinkList()
ll.add_last(1)
ll.add_last(2)
ll.add_last(2)
ll.add_last(1)
ll.print_ll()
print(ll.check_palendrom())









    
    