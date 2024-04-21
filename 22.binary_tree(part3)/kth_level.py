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

def k_th_level_item(root,target_level,curr_level):
    if not root:
        return None
    if curr_level == target_level:
        print(root.data,end=" ")
        return
    k_th_level_item(root.left,target_level,curr_level+1)
    k_th_level_item(root.right,target_level,curr_level+1)

k_th_level_item(node,3,1)