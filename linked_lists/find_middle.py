"""
Find the middle element of a singly linked list.
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


def find_middle(head):

    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    return slow.data


head = None

head = append(head, 10)
head = append(head, 20)
head = append(head, 30)
head = append(head, 40)
head = append(head, 50)

print(find_middle(head))