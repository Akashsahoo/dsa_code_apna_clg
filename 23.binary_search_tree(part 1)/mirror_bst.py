from collections import deque
queue = deque()
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

def build_bst(li):
    root = None
    for i in li:
        root = insert_node(root,i)
    
    return root

def level_order(root):
    
    queue.append(root)
    queue.append(None)
    level = 0
    while len(queue):
      node = queue.popleft()
      if not node:
        level += 1
        print()
        if  len(queue):
            queue.append(None)
      else:
        print(node.data,end=" ")
        if node.left:
           queue.append(node.left)
        if node.right:
           queue.append(node.right)

def mirror_bst(root):
    if not root:
        return
    if root.left or root.right:
       temp = root.right
       root.right = root.left
       root.left = temp
       mirror_bst(root.left)
       mirror_bst(root.right)
    


li = [8,5,3,1,4,6,10,11,14]
root = build_bst(li)
inorder(root)
print()
mirror_bst(root)
level_order(root)