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


def kth_ancestor_of_node(root,n1,k):
    if not root:
       return -1
    if root.data == n1:
        return 0
    left = kth_ancestor_of_node(root.left,n1,k)
    right = kth_ancestor_of_node(root.right,n1,k)

    if left==-1 and right==-1:
        return -1
    
    level = max(left,right)

    if level+1==k:
        print(root.data)
    return level+1

    

    
kth_ancestor_of_node(node,7,2)