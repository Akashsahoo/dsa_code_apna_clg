from random import randint
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkList:
    head = None
    tail = None
    

    def add_last(self,data):
        new_node = Node(data)
        if not self.head:
            self.tail = self.head = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        
    

    def print_ll(self):
        temp = self.head
        while temp:
            print(temp.data,end="->")
            temp = temp.next
        print()
def get_mid(head1):
    slow = head1
    fast = head1.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
def merge(head1,head2):
    temp = temp_head= Node(-1)
    left_head = head1
    right_head = head2
    while left_head and right_head:
        if left_head.data <= right_head.data:
            temp.next = left_head
            left_head = left_head.next
            
        else:
            temp.next = right_head
            right_head = right_head.next
        temp = temp.next
    
    while left_head:
        temp.next = left_head
        temp = temp.next
        left_head = left_head.next
    
    while right_head:
        temp.next = right_head
        temp = temp.next
        right_head = right_head.next
    
    return temp_head.next
    

    



def print_ll(node):
        temp = node
        while temp:
            print(temp.data,end="->")
            temp = temp.next
        print()



def merge_sort(head1):
    if not head1:
      return head1
    if not head1.next:
        return head1
    mid_elem = get_mid(head1)
    head2 = mid_elem.next
    mid_elem.next = None
    new_head1 = merge_sort(head1)
    new_head2 = merge_sort(head2)
    return merge(new_head1,new_head2)

ll = LinkList()
for i in range(10):
   ll.add_last(randint(100,200))

ll.print_ll()

ll1 = merge_sort(ll.head)

print_ll(ll1)