from collections import deque

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.right = None
    self.left = None


root = TreeNode(1)

root.left = TreeNode(1)
root.right = TreeNode(1)

root.left.left = TreeNode(3)
root.left.right = TreeNode(2)

root.right.right = TreeNode(5)

root.left.right.left = TreeNode(2)


def goodNode(root):

  

