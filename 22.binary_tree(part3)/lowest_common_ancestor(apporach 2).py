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



def lca(root,n1,n2):
    if not root:
       return None
    
    if root.data == n1 or root.data == n2 :
       return root
    left_lca = lca(root.left,n1,n2)
    right_lca = lca(root.right,n1,n2)

    if not left_lca:
      return right_lca
    elif not right_lca:
      return left_lca
    else:
      return root

# print(lca(node,4,7).data)


# print(lca(node,4,5).data) 


print(lca(node,6,7).data)

# print(lca(node,2,3).data)