from collections import deque
queue = deque()
class Node:
    left = None
    right = None
    def __init__(self,data):
        self.data = data


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

inorder_sequence = []
def converted_bst_to_balance_bst(root):
    if not root:
        return
    converted_bst_to_balance_bst(root.left)
    inorder_sequence.append(root.data)
    converted_bst_to_balance_bst(root.right)


def sorted_arr_to_balanced_bst(arr,lb,ub):
    if lb >ub:
        return
    
    mid = (lb+ub)//2
    root = Node(arr[mid])
    root.left = sorted_arr_to_balanced_bst(arr,lb,mid-1)
    root.right = sorted_arr_to_balanced_bst(arr,mid+1,ub)
    return root


'''
       8
     /   \
    6     10
   /       \
  5         11
 /           \
3             12    '''


root = Node(8)
root.left = Node(6)
root.right = Node(10)
root.left.left = Node(5)
root.right.right = Node(11)
root.left.left.left = Node(3)
root.right.right.right = Node(12)
level_order(root)
converted_bst_to_balance_bst(root)
root = sorted_arr_to_balanced_bst(inorder_sequence,0,len(inorder_sequence)-1)
level_order(root)