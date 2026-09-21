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

    def insert_at(self, val, position):
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

        # Delete head node
        if self.head.val == val:
            self.head = self.head.next
            return

        prev = None
        curr = self.head

        while curr is not None:
            if curr.val == val:
                prev.next = curr.next
                return

            prev = curr
            curr = curr.next

        print("Node Not Found")

sll = SinglyLinkedList()

sll.append(10)
sll.append(20)
sll.append(30)

sll.traversal()
# 10 20 30

sll.insert_at(15, 1)
sll.traversal()
# 10 15 20 30

sll.delete(20)
sll.traversal()
# 10 15 30

sll.delete(10)
sll.traversal()
# 15 30