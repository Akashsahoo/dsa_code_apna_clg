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
class Infodiameter:
      def __init__(self,height,dia):
          self.dia = dia
          self.height = height
    
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
        return Infodiameter(0,0)
   
    ld = diameter(root.left)
    rd = diameter(root.right)
    ht = max(ld.height, rd.height)+1
    dia = max(ld.dia,rd.dia,ld.height+rd.height+1)
    return Infodiameter(ht,dia)

Tree = tree()
root = Tree.build_tree_pre_order()
dia_info = diameter(root)
level_order(root)
print(dia_info.dia)