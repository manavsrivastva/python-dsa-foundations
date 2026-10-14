"""Linear and binary search."""
def linear_search(items, target):
    """Works on unsorted input: O(n) time, O(1) extra space."""
    for index, value in enumerate(items):
        if value == target:
            return index
    return -1


def binary_search(sorted_items, target):
    """Sorted input required: O(log n) time, O(1) extra space."""
    left, right = 0, len(sorted_items) - 1
    while left <= right:
        middle = (left + right) // 2
        if sorted_items[middle] == target:
            return middle
        if sorted_items[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    return -1


def search_examples():
    data = [2, 4, 6, 8, 10, 12]
    print("Linear search for 8:", linear_search(data, 8))
    print("Binary search for 10:", binary_search(data, 10))
