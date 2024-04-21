from collections import deque
queue = deque()
arr = [3,5,6,8,10,11,12]
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

def sorted_arr_to_balanced_bst(arr,lb,ub):
    if lb >ub:
        return
    
    mid = (lb+ub)//2
    root = Node(arr[mid])
    root.left = sorted_arr_to_balanced_bst(arr,lb,mid-1)
    root.right = sorted_arr_to_balanced_bst(arr,mid+1,ub)
    return root




root  = sorted_arr_to_balanced_bst(arr,0,len(arr)-1)
level_order(root)