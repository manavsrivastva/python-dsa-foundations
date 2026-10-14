"""Introductory two-pointer patterns."""
def pair_sum_sorted(numbers, target):
    """Sorted input required. O(n) time, O(1) auxiliary space."""
    left, right = 0, len(numbers) - 1
    while left < right:
        total = numbers[left] + numbers[right]
        if total == target:
            return numbers[left], numbers[right]
        if total < target:
            left += 1
        else:
            right -= 1
    return None


def remove_duplicates_sorted(numbers):
    """Return unique values from sorted input. O(n) time and output space."""
    if not numbers:
        return []
    result = [numbers[0]]
    for value in numbers[1:]:
        if value != result[-1]:
            result.append(value)
    return result


def reverse_in_place(items):
    """O(n) time and O(1) auxiliary space."""
    left, right = 0, len(items) - 1
    while left < right:
        items[left], items[right] = items[right], items[left]
        left += 1
        right -= 1
    return items


def two_pointer_examples():
    print("Pair sum:", pair_sum_sorted([1, 2, 4, 6, 8], 10))
    print("Unique:", remove_duplicates_sorted([1, 1, 2, 2, 3]))
    print("Reverse in place:", reverse_in_place([1, 2, 3, 4]))
