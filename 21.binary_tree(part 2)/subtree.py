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


''' 
       2   
      /  \  
     4    5 
'''

node2 = TreeNode(2)
node2.left = TreeNode(4)
node2.right = TreeNode(5)
node2.left.left = TreeNode(6)





def is_identical(root1,root2):
    if not root1 and not root2:
        return True
    if not root1 or not root2 or (root1.data != root2.data):
        return False
    
    if not is_identical(root1.left,root2.left):
        return False
    if not is_identical(root1.right,root2.right):
        return False
    
    return True


def subtree(tree_node,subtree_node):
    if not tree_node:
        return False
    
    if tree_node.data == subtree_node.data:
        if is_identical(tree_node,subtree_node):
            return True
    
    return subtree(tree_node.left,subtree_node) or subtree(tree_node.right,subtree_node)



print(subtree(node,node2))