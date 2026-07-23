"""
Find the maximum depth of a binary tree.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def maximum_depth(root):

    if root is None:
        return 0

    left_depth = maximum_depth(root.left)
    right_depth = maximum_depth(root.right)

    return 1 + max(left_depth, right_depth)


root = Node(10)

root.left = Node(5)
root.right = Node(15)

root.left.left = Node(3)
root.left.right = Node(7)

print(maximum_depth(root))