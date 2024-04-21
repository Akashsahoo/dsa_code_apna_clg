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
    
#     O(nlogn)
def build_bst(li):
    root = None
    for i in li:
        root = insert_node(root,i)
    inorder(root)
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

def in_order_sucessor(root):
    temp = root.right
    while temp.left:
        temp = temp.left
    return temp.data
def delete_node(root,target) :
    if not root:
        print("element does not exists")
        return root
    if root.data == target:
        if not root.left:
            root = root.right

        elif not root.right:
            root = root.left
        else:
            sucessor_data = in_order_sucessor(root)
            root = delete_node(root,sucessor_data)
            root.data = sucessor_data
        return root
    if root.data > target:
       root.left =  delete_node(root.left,target)
       
    else:
        root.right = delete_node(root.right,target)
    return root

li = [5,1,3,4,2,7]

root = build_bst(li)
inorder(root)
print()


# root = delete_node(root,4)
# root = delete_node(root,3)
# root = delete_node(root,5)
inorder(root)
print()

