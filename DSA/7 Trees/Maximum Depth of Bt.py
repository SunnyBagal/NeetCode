class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.left.left = TreeNode(7)

def maxDepth(self):
  if root.val == None:
    return None

  count = 0
  