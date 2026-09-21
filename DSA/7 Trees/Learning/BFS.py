from collections import deque

class TreeNode:
  def __init__(self, val) :
    self.val = val
    self.left = None
    self.right = None

#
#         1
#        / \
#       2   3
#      / \   \
#     4   5   6

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.left.left = TreeNode(7)


def level_order (node):
  result = []
  queue = deque([])
  queue.append(node)

  while len(queue) != 0:
    e = queue.popleft()
    result.append(e.val)
    
    if e.left is not None:
      queue.append(e.left)

    if e.right is not None:
      queue.append(e.right)

  return print(result)

print("Level-order Traversal")
level_order(root)