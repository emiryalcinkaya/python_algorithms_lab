"""
Create and display a singly linked list.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def append(head, data):

    new_node = Node(data)

    if head is None:
        return new_node

    current = head

    while current.next is not None:
        current = current.next

    current.next = new_node

    return head


def display(head):

    current = head

    while current is not None:
        print(current.data, end=" -> ")
        current = current.next

    print("None")


head = None

head = append(head, 10)
head = append(head, 20)
head = append(head, 30)

display(head)