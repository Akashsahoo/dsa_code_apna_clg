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


def diameter(root):
    if not root:
        return 0
    lh = max_height(root.left)
    rh = max_height(root.right)
    ld = diameter(root.left)
    rd = diameter(root.right)
    self_dia = lh+rh+1
    return max(ld,rd,self_dia)

Tree = tree()
root = Tree.build_tree_pre_order()
dia = diameter(root)
level_order(root)
print(dia)