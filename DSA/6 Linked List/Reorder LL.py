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
      print(curr.val, end=" ")
      curr = curr.next
    
    print()


  def reorder(self):

    #~.        1 -> 2 -> 3 -> 4 -> 5
    #~                     -> null 

    slow = self.head 
    fast = self.head.next

    while fast and fast.next :
      slow = slow.next
      fast = fast.next.next

    second = slow.next
    prev = None
    slow.next = None

    while second:
      temp = second.next
      second.next = prev 
      prev = second
      second = temp

    first = self.head
    second = prev

    while second:
      temp1 = first.next
      temp2 = second.next
      first.next = second
      second.next = temp1
      first = temp1
      second = temp2

    curr = self.head
    while curr is not None:
      print(curr.val, end=" ")
      curr = curr.next

    print()


sll = SinglyLinkedList()
sll.append(2)
sll.append(4)
sll.append(6)
sll.append(8)
sll.append(10)

sll.traversal()
sll.reorder()