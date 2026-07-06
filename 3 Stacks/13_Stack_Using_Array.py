class Stack :
  def __init__(self):
    self.items = []

  def is_empty(self):
    return len(self.items) == 0

  def push(self, n):
    self.items.append(n)
  
  def pop(self):
    if len(self.items) == 0:
      return "Can't pop the stack is empty"
    
    x = self.items.pop()
    return x
  
  def top(self):
    if len(self.items) == 0:
      return "Can't pop the stack is empty"
    return self.items[-1]
  
  def size(self):
    return len(self.items)
  

stack = Stack()
stack.push(5)
stack.push(6)
stack.push(7)
stack.pop()
stack.push(100)
stack.top()

print(stack)