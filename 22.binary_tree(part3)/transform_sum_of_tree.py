from collections import deque
queue = deque()
class TreeNode:
    left = None
    right = None
    def __init__(self,data):
        self.data = data
'''
          1
        /   \
       2     3
      /  \  /  \
     4    5 6   7


'''

node = TreeNode(1)
node.left = TreeNode(2)
node.right = TreeNode(3)
node.left.left = TreeNode(4)
node.left.right = TreeNode(5)
node.right.left = TreeNode(6)
node.right.right = TreeNode(7)


def sum_of_tree(root):
    if not root:
        return 0
    left_sub_tree = sum_of_tree(root.left)
    right_sub_tree = sum_of_tree(root.right)
    data = root.data
    if not root.left:
        left_child = 0
    else:
        left_child = root.left.data
    if not root.right:
        right_child = 0
    else:
        right_child = root.right.data
    root.data = left_sub_tree+right_sub_tree+left_child+right_child
    return data


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

sum_of_tree(node)
level_order(node)