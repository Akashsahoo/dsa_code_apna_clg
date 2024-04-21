from collections import deque
queue = deque()

class Node:
    left = None
    right = None
    def __init__(self,data):
        self.data = data

def converted_bst_to_balance_bst(root,inorder_sequence):
    if not root:
        return 
    converted_bst_to_balance_bst(root.left,inorder_sequence)
    inorder_sequence.append(root.data)
    converted_bst_to_balance_bst(root.right,inorder_sequence)

def sorted_arr_to_balanced_bst(arr,lb,ub):
    if lb >ub:
        return
    
    mid = (lb+ub)//2
    root = Node(arr[mid])
    root.left = sorted_arr_to_balanced_bst(arr,lb,mid-1)
    root.right = sorted_arr_to_balanced_bst(arr,mid+1,ub)
    return root



def merge_arr(arr1,arr2):
    arr = []
    i=0
    j=0
    while i<len(arr1) and j < len(arr2):
        if arr1[i]<=arr2[j]:
            arr.append(arr1[i])
            i=i+1
        else:
            arr.append(arr2[j])
            j=j+1
    while i<len(arr1):
        arr.append(arr1[i])
        i=i+1
    while j<len(arr2):
        arr.append(arr2[j])
        j=j+1
    return arr

def level_order(root):
    if not root:
        return
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

root1= Node(2)
root1.left = Node(1)
root1.right=Node(4)

root2= Node(9)
root2.left = Node(3)
root2.right=Node(12)

arr1 = []
arr2 = []
converted_bst_to_balance_bst(root1,arr1)
converted_bst_to_balance_bst(root2,arr2)
arr = merge_arr(arr1,arr2)
root  = sorted_arr_to_balanced_bst(arr,0,len(arr)-1)
level_order(root)