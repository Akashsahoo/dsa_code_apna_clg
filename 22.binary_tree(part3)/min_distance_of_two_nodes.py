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
    
def get_min_distance(node,n1,n2):
    if not node:
      return -1
    if node.data == n1 or node.data == n2:
      return 0
    
    distance_left = get_min_distance(node.left,n1,n2)
    distance_right = get_min_distance(node.right,n1,n2)
    
    if distance_left <0 and distance_right < 0:
       return -1
    elif distance_right < 0:
         return distance_left+1
    elif distance_left <0:
         return distance_right+1
    else:
      return distance_left +1+distance_right+1

    


def min_distance_of_two_nodes(root,n1,n2):
    if not root:
      return -1
    lca_node = lca(root,n1,n2)
    min_distance = get_min_distance(lca_node,n1,n2)
    return min_distance

print(min_distance_of_two_nodes(node,4,7)) # 4


print(min_distance_of_two_nodes(node,4,5)) # 2




print(min_distance_of_two_nodes(node,2,3)) # 2