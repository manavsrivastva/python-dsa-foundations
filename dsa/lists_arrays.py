"""Common Python list operations."""
def access_at(items, index):
    """Index access: O(1)."""
    return items[index]


def append_item(items, value):
    """Amortized O(1); occasional resizing may take O(n)."""
    items.append(value)
    return items


def insert_at(items, index, value):
    """Middle insertion: O(n), because elements may shift."""
    items.insert(index, value)
    return items


def delete_at(items, index):
    """Middle deletion: O(n), because elements may shift."""
    return items.pop(index)


def reverse_copy(items):
    """O(n) time and O(n) extra space."""
    return items[::-1]


def array_examples():
    values = [10, 20, 30]
    print("Access:", access_at(values, 1))
    print("Append:", append_item(values, 40))
    print("Insert:", insert_at(values, 1, 15))
    print("Delete:", delete_at(values, 2))
    print("Reverse copy:", reverse_copy(values))
