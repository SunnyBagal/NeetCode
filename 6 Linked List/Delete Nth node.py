class Node:
  def __init__(self, val):
    self.val = val
    self.next = None


class SinglyLinkedList:
  def __init__(self):
    self.head = None

  def append(self, val):
    new_node = Node(val)

    if self.head is None:
      self.head = new_node
      return

    curr = self.head
    while curr.next is not None:
      curr = curr.next

    curr.next = new_node
  

  def traversal(self):
    if self.head is None:
      return

    curr = self.head
    while curr is not None:
      print(curr.val, end=" ")
      curr = curr.next
    
    print()

  def delete_from_end(self, n):
    N = 0
    curr = self.head
    while curr:
      N += 1
      curr = curr.next

    removeIndex = N - n
    if removeIndex == 0:
      return self.head.next

    curr = self.head
    for i in range(N - 1):
      if (i + 1) == removeIndex:
        curr.next = curr.next.next
        break
      curr = curr.next

    curr = self.head
    while curr is not None:
      print(curr.val, end=" ")
      curr = curr.next
    
    print()
  
sll = SinglyLinkedList()
sll.append(10)
sll.append(20)
sll.append(30)
sll.append(40)
sll.append(50)

sll.traversal()
sll.delete_from_end(2)