from collections import deque
class TreeNode:
    left = None
    right = None
    def __init__(self,data):
        self.data = data


class Info:
    def __init__(self,node,hd):
        self.node = node
        self.hd = hd





def topview(tree_node):
    hash_map = dict()
    queue = deque()
    queue.append(Info(tree_node,0))
    queue.append(None)
    min_val = 0
    max_val = 0
    while len(queue):
       cur = queue.popleft()
       if not cur:
          if len(queue): 
             queue.append(None)
          else:
            break
       else:
            node = cur.node
            if cur.hd not in hash_map.keys():
                hash_map[cur.hd] = node.data
            if node.left:
                queue.append(Info(node.left,cur.hd-1))
                min_val = min(min_val,cur.hd-1)
                
            if node.right:
                queue.append(Info(node.right,cur.hd+1))
                max_val = max(max_val,cur.hd+1)

    for num in range(min_val,max_val+1):
        print(hash_map[num],end=" ")
    
    

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


topview(node)