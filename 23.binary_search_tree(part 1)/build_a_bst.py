class Node:
    left = None
    right = None
    def __init__(self,data):
        self.data = data


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
    

def search_node(root,target):
    if not root:
        return False
    
    if root.data==target:
        return True
    
    if root.data>target:
        return search_node(root.left,target)
    else:
        return search_node(root.right,target)



#     O(nlogn)
def build_bst(li):
    root = None
    for i in li:
        root = insert_node(root,i)
    inorder(root)
    return root
     

li = [5,1,3,4,2,7]

root = build_bst(li)

print(search_node(root,1))