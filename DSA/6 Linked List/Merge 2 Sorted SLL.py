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
      print("SLL is empty")
      return 
    
    curr = self.head
    while curr is not None:
      print(curr.val, end=", ")
      curr = curr.next

    print()

  
  def merge_Sorted(self, sll_1, sll_2):
    dummy = node = Node(None)
    while sll_1 and sll_2:
      if sll_1.val < sll_2.val:
        node.next = sll_1
        sll_1 = sll_1.next

      else:
        node.next = sll_2
        sll_2 = sll_2.next
      
      node = node.next
    
    node.next = sll_1 or sll_2

    return dummy.next


sll_1 = SinglyLinkedList()

sll_1.append(10)
sll_1.append(20)
sll_1.append(30)

sll_1.traversal()

sll_2 = SinglyLinkedList()
sll_2.append(10)
sll_2.append(30)
sll_2.append(50)
sll_2.traversal()


sll_1.merge_Sorted(sll_1.head, sll_2.head)
