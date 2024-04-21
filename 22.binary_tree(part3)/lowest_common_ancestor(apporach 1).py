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
path1 = []
path2 = []
def get_path(root,n,path):
  if not root:
     return False
  if root.data == n:
    path.append(root)
    return True
  if get_path(root.left,n,path) or get_path(root.right,n,path):
      path.append(root)
      return True
  return False


def lca(root,n1,n2,path1,path2):
  get_path(root,n1,path1)
  get_path(root,n2,path2)
  i = len(path1)-1

  
  while path1[i]==path2[i]:
        i = i-1
  
  return path1[i+1].data


# print(lca(node,4,7,path1,path2))

# print(lca(node,4,5,path1,path2)) 


# print(lca(node,6,7,path1,path2))

print(lca(node,2,3,path1,path2))