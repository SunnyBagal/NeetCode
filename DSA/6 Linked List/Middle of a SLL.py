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
    count = 0
    if self.head is None:
      print("SLL is empty")
      return 

    curr = self.head 
    while curr is not None:
      print(curr.val, end=" ")      
      curr = curr.next
      count += 1

    print()

  def insert_At(self, val, position):
    new_node = Node(val)
    if position == 0:
      new_node.next = self.head
      self.head = new_node
      return 

    current = self.head
    prev = None
    count = 0

    while current is not None and count < position:
      prev = current
      current = current.next
      count += 1

    if count != position:
      print("Invalid Position")
      return
    
    prev.next = new_node
    new_node.next = current

  def delete(self, val):
    if self.head is None:
      print("SLL is empty")
      return
    
    if self.head == val:
      self.head = self.head.next
      return
  
    prev = None
    current = self.head

    while current is not None:
      if current.val == val :
        prev.next = current.next
        return

      prev = current
      current = current.next

    print("Node not Found")

  def middle_val(self):
    if self.head is None:
      print("SLL is empty")
      return

    curr = self.head
    after = self.head

    while after.next is not None:
      curr = curr.next
      after = curr.next.next

    print(curr.val)

sll = SinglyLinkedList()
sll.append(10)
sll.append(20)
sll.append(30)
sll.append(40)
sll.append(50)
sll.append(60)

sll.traversal()
sll.middle_val()
