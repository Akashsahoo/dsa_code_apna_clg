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
     
def root_to_leaf(root):
    if not root: 
        return
    path.append(root.data)
    if not root.left and not root.right:
        print(path)
        path.pop()
        return
    root_to_leaf(root.left)
    root_to_leaf(root.right)
    path.pop()






li = [8,5,3,1,4,6,10,11,14]
root = build_bst(li)
# inorder(root)
root_to_leaf(root)