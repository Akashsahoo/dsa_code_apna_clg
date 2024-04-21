class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkList:
    head = None
    
def detect_cycle(ll):
    slow = ll.head
    fast = ll.head
    while  fast and  fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    
    return False

ll = LinkList()
ll.head = node1 =  Node(1)
node1.next = node2 =  Node(2)
node2.next = node3 = Node(3)
node3.next = node4 = Node(4)
node4.next = node5 = Node(5)
node5.next = node3

print(detect_cycle(ll))