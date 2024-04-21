class Node:
    def __init__(self,data):
        self.data = data
        self.next_node = None

class LinkList:
    head = None
    def add_first(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

    def remove_first(self):
        if not self.head:
            return 
        else:
            top = self.head.data
            self.head = self.head.next_node
            return top


class StackLinkList:
    def __init__(self):
        self.linklist = LinkList()

    def is_empty(self):
        if not self.linklist.head:
            return True
        return False

    def push(self,data):
        self.linklist.add_first(data)

    def pop(self):
        if not self.is_empty():
            return self.linklist.remove_first()
        return False

    def peek(self):
        if not self.is_empty():
            return self.linklist.head.data
        return False


stack = StackLinkList()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())
print(stack.peek())