class StackList:
    # list_stack = []
    def __init__(self):
        self.list_stack = []

    def __str__(self):
        print(self.list_stack)
        return " "
    def push(self,data):
        self.list_stack.append(data)
    
    def pop(self):
        if not self.is_empty():
            top = self.list_stack.pop(len(self.list_stack)-1)
            return top

    def is_empty(self):
        if len(self.list_stack) == 0:
            return True
        return False
    
    def peek(self):
        if not self.is_empty():
            return self.list_stack[len(self.list_stack)-1]
    
stack = StackList()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())
print(stack.peek())


stackc = StackList()
stackc.push(1)
stackc.push(2)
stackc.push(3)
print(stackc.pop())
print(stackc.peek())

print(stack)
print(stackc)
 
