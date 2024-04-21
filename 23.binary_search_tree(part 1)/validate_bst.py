class Node:
    left = None
    right = None
    def __init__(self,data):
        self.data = data

path = []
def insert_node(root,elem):
    if not root:
        return Node(elem)                                
    if root.data>elem:
        root.left = insert_node(root.left,elem)
    else:
        root.right = insert_node(root.right,elem)
    return root

def inorder(root):
    if not root:
        return 
    inorder(root.left)
    print(root.data,end=" ")
    inorder(root.right)

def build_bst(li):
    root = None
    for i in li:
        root = insert_node(root,i)
    
    return root
     

def vaild_bst(root,min_value,max_value):
    if not root:
        return True
    if root.data > min_value and root.data < max_value:
        if not (vaild_bst(root.left,min_value,root.data)):
            return False
        if not (vaild_bst(root.right,root.data,max_value)):
            return False
        return True
    return False




min_value = -999999
max_value = 999999
li = [8,5,3,1,4,6,10,11,14]
root = build_bst(li)
# inorder(root)


# example
root = Node(4)
root.left = Node(2)
root.right = Node(5)
# root.right.left = Node(7)
root.left.left = Node(1)
root.left.right = Node(3)
print(vaild_bst(root,min_value,max_value))
