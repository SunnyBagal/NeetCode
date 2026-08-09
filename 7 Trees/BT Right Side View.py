from collections import deque

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.right = None
    self.left = None


root = TreeNode(1)

root.left = TreeNode(2)
root.right = TreeNode(3)

root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

root.right.right = TreeNode(6)

root.left.right.right = TreeNode(7)


def rightSideView(root):
  que = deque([root])
  res = []

  while que:
    level_size = len(que)

    for i in range(level_size):
      current = que.popleft()

      if i == level_size - 1:
          res.append(current.val)

      if current.left is not None:
          que.append(current.left)

      if current.right is not None:
          que.append(current.right)

  return res


print(rightSideView(root))