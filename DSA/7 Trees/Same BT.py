class TreeNode: 
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None


tree1 = TreeNode(1)
tree2 = TreeNode(1)

tree1.left = TreeNode(2)
tree1.right = TreeNode(3)

tree2.left = TreeNode(2)
tree2.right = TreeNode(3)


def preorder(root, arr):
  if root is None: 
    arr.append(None)
    return 

  arr.append(root.val)
  preorder(root.left, arr)
  preorder(root.right, arr)


tree11 = []
tree22 = []

preorder(tree1, tree11)
preorder(tree2, tree22)

print(tree11 == tree22)
