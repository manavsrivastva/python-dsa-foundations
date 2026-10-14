"""Time and space complexity examples."""
def constant_time_first(items):
    """O(1) time and O(1) auxiliary space."""
    return items[0] if items else None


def linear_search(items, target):
    """O(n) time, O(1) auxiliary space."""
    for index, value in enumerate(items):
        if value == target:
            return index
    return -1


def sum_nested(items):
    """O(total number of elements) time."""
    return sum(value for row in items for value in row)


def make_copy(items):
    """O(n) time and O(n) additional space."""
    return items[:]


def complexity_examples():
    numbers = [3, 7, 2, 9]
    print("First:", constant_time_first(numbers))
    print("Linear search for 2:", linear_search(numbers, 2))
    print("Nested sum:", sum_nested([[1, 2], [3, 4]]))
    print("Copy:", make_copy(numbers))
    print("Typical growth: O(1), O(log n), O(n), O(n log n), O(n²).")
