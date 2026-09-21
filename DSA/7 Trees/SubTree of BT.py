class TreeNode: 
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None


tree1 = TreeNode(1)
tree2 = TreeNode(2)

tree1.left = TreeNode(2)
tree1.right = TreeNode(3)
tree1.left.left = TreeNode(4)
tree1.left.right = TreeNode(5)

tree2.left = TreeNode(4)
tree2.right = TreeNode(5)


def postorder(root):
  if 