"""
Create a simple binary tree.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


root = Node(10)

root.left = Node(5)
root.right = Node(15)

root.left.left = Node(3)
root.left.right = Node(7)

print(root.data)
print(root.left.data)
print(root.right.data)
print(root.left.left.data)
print(root.left.right.data)