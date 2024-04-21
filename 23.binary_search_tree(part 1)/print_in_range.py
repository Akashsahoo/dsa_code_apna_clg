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
    

def print_in_range(root,k1,k2):
    if not root:
        return
    if root.data >=k1 and root.data<=k2:
         print_in_range(root.left,k1,k2)
         print(root.data,end=" ")
         print_in_range(root.right,k1,k2)
    elif root.data<k1:
         print_in_range(root.right,k1,k2)
    else:
        print_in_range(root.left,k1,k2)

 


#     O(nlogn)
def build_bst(li):
    root = None
    for i in li:
        root = insert_node(root,i)
    # inorder(root)
    return root
     

li = [8,5,3,1,4,6,10,11,14]

root = build_bst(li)
print_in_range(root,5,12)
# print(search_node(root,1))