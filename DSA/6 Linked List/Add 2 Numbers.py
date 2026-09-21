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

  def addTwoNums(self, list1, list2):
   dummy = Node(None)
   current = dummy

   carry = 0

   while list1 or list2 or carry:
    v1 = list1.val if list1 else 0
    v2 = list2.val if list2 else 0

    val = v1 + v2 + carry
    carry = val // 10
    val = val % 10
    current.next = Node(val)

    current = current.next
    list1 = list1.next if list1 else 0
    list2 = list2.next if list2 else 0
    
    return dummy




sll = SinglyLinkedList()
sll.append(10)
sll.append(20)
sll.append(30)
sll.append(40)
sll.append(50)

sll2 = SinglyLinkedList()
sll2.append(10)
sll2.append(20)
sll2.append(30)
sll2.append(40)
sll2.append(50)

sll.addTwoNums(sll, sll2)