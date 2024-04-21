from collections import deque
queue = deque()
li = [1, 2, 4, -1, -1, 5, -1, -1, 3, -1, 6, -1,-1]
class treenode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
class tree:
    index = -1
    def build_tree_pre_order(self):
        self.index +=1
        if li[self.index]==-1:
            return
        root = treenode(li[self.index])
        root.left = self.build_tree_pre_order()
        root.right = self.build_tree_pre_order()
        return root

def pre_order(root):
    if not root:
        return None
    print(root.data,end=" ")
    pre_order(root.left)
    pre_order(root.right)

def in_order(root):
    if not root:
        return None
    in_order(root.left)
    print(root.data,end=" ")
    in_order(root.right)


def post_order(root):
    if not root:
        return None
    post_order(root.left)
    post_order(root.right)
    print(root.data,end=" ")


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
def max_height(root):
    if not root:
        return 0
    lh = max_height(root.left)
    rh = max_height(root.right)
    return max(lh,rh)+1

def count_nodes(root):
    if not root:
        return 0
    lcount = count_nodes(root.left)
    rcount = count_nodes(root.right)
    return lcount+rcount+1
def sum_nodes(root):
    if not root:
        return 0
    lsum = sum_nodes(root.left)
    rsum = sum_nodes(root.right)
    return lsum+rsum+root.data
Tree = tree()
root = Tree.build_tree_pre_order()
# pre_order(root)
# in_order(root)
# post_order(root)
level_order(root)
print(max_height(root))
print(count_nodes(root))
print(sum_nodes(root))