from collections import deque
queue = deque()
max_bst_size = 0
min_val = -999999
max_val = 999999
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

class Info:
      def __init__(self,is_bst,size,min_val,max_val): 
          self.is_bst = is_bst
          self.size = size
          self.min_val = min_val
          self.max_val = max_val

# global max_bst_size
# global min_val
# global max_val

def largest_bst(root):
    global min_val,max_val,max_bst_size
    if not root:
        return Info(True,0,min_val,max_val)
    if not root.left and not root.right:
        return Info(True,1,root.data,root.data)
    left_bst = largest_bst(root.left)
    right_bst = largest_bst(root.right)
    size = left_bst.size+right_bst.size+1
    min_val = min(root.data,left_bst.min_val,right_bst.min_val)
    max_val = max(root.data,left_bst.max_val,right_bst.max_val)
    
    if root.data< left_bst.min_val or root.data> right_bst.max_val:
         return Info(False,size,min_val,max_val)
    if left_bst.is_bst and right_bst.is_bst:
        max_bst_size = max(max_bst_size,size)
        
        return Info(True,size,min_val,max_val)
    else:
        return Info(False,size,min_val,max_val)
    
        '''

                   50
                  /  \
                30    60
               /  \   /  \
              5    20 45  70
                          /  \
                         65   80   
        '''

root = Node(50)
root.left = Node(30)
root.right = Node(60)
root.left.left = Node(5)
root.left.right = Node(20)
root.right.left = Node(45)
root.right.right = Node(70)
root.right.right.left = Node(65)
root.right.right.right = Node(80)
# level_order(root)
largest_bst(root)
print(max_bst_size)