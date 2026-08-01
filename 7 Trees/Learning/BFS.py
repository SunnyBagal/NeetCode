from collections import deque

class NodeTree:
  def __init__(self, val) :
    self.val = val
    self.left = None
    self.right = None

  
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