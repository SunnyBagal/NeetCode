class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# ----------------------------
# Traversals
# ----------------------------

def preorder(node):
    if node is None:
        return

    print(node.val, end=" ")
    preorder(node.left)
    preorder(node.right)


def inorder(node):
    if node is None:
        return

    inorder(node.left)
    print(node.val, end=" ")
    inorder(node.right)


def postorder(node): 
    if node is None:
        return

    postorder(node.left)
    postorder(node.right)
    print(node.val, end=" ")


# ----------------------------
# Create the Tree
# ----------------------------
#
#         1
#        / \
#       2   3
#      / \   \
#     4   5   6
#

root = TreeNode(1)

root.left = TreeNode(2)
root.right = TreeNode(3)

root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

root.right.right = TreeNode(6)


# ----------------------------
# Print Traversals
# ----------------------------

print("Preorder Traversal:")
preorder(root)
print("\n")

print("Inorder Traversal:")
inorder(root)
print("\n")

print("Postorder Traversal:")
postorder(root)
print("\n")


# ----------------------------
# Access Individual Nodes
# ----------------------------

print("Root:", root.val)
print("Left Child:", root.left.val)
print("Right Child:", root.right.val)
print("Left Right Child:", root.left.right.val)