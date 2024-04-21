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

def reverse(node):
        prev = None
        temp = node
       
        while temp:
            next_node = temp.next
            temp.next = prev
            prev = temp
            temp = next_node
        
        return prev


def print_ll(node):
        temp = node
        while temp:
            print(temp.data,end="->")
            temp = temp.next
        print()

def get_mid(ll):
    slow = ll.head
    fast = ll.head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
    
def zig_zag(ll):
    temp = temp_head = Node(-1)
    mid = get_mid(ll)
    head1 = ll.head
    head2 = mid.next
    mid.next = None
    head2 = reverse(head2)
    while head1 or head2:
        if head1:
            temp.next = head1
            temp = temp.next
            head1 = head1.next
        if head2:
            temp.next = head2
            temp = temp.next
            head2 = head2.next
    return temp_head.next



ll = LinkList()
for i in range(10):
   ll.add_last(randint(100,200))
ll.print_ll()

node = zig_zag(ll)
print_ll(node)