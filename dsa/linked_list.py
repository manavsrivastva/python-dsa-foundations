"""Singly linked list basics."""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        """Append via traversal: O(n)."""
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = node

    def traverse(self):
        """O(n) time and O(n) output space."""
        values = []
        current = self.head
        while current is not None:
            values.append(current.data)
            current = current.next
        return values

    def find(self, target):
        """O(n) time."""
        current = self.head
        while current is not None:
            if current.data == target:
                return True
            current = current.next
        return False

    def __len__(self):
        count, current = 0, self.head
        while current is not None:
            count += 1
            current = current.next
        return count


def linked_list_examples():
    linked = SinglyLinkedList()
    for value in [10, 20, 30]:
        linked.append(value)
    print("Traversal:", linked.traverse())
    print("Find 20:", linked.find(20), "| length:", len(linked))
