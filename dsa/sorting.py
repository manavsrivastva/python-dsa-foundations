"""Manual elementary sorts and Python built-in sort."""
def bubble_sort(items):
    """Adjacent swaps; O(n²) worst case, O(1) auxiliary space besides copy."""
    arr = items[:]
    for end in range(len(arr) - 1, 0, -1):
        swapped = False
        for i in range(end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        if not swapped:
            break
    return arr


def selection_sort(items):
    """Select minimum for each position; O(n²) time."""
    arr = items[:]
    for start in range(len(arr)):
        minimum = start
        for i in range(start + 1, len(arr)):
            if arr[i] < arr[minimum]:
                minimum = i
        arr[start], arr[minimum] = arr[minimum], arr[start]
    return arr


def insertion_sort(items):
    """Insert each value into sorted prefix; worst O(n²), best O(n)."""
    arr = items[:]
    for i in range(1, len(arr)):
        current = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > current:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current
    return arr


def built_in_sort_examples():
    names = ["Zara", "alex", "Manav", "riya"]
    scores = [("Asha", 82), ("Kabir", 91), ("Mina", 82)]
    return {
        "ascending": sorted([5, 1, 4, 2]),
        "descending": sorted([5, 1, 4, 2], reverse=True),
        "case_insensitive": sorted(names, key=str.lower),
        "score_then_name": sorted(scores, key=lambda pair: (pair[1], pair[0])),
    }


def sorting_examples():
    values = [5, 1, 4, 2, 8]
    print("Bubble:", bubble_sort(values))
    print("Selection:", selection_sort(values))
    print("Insertion:", insertion_sort(values))
    print("Built-in:", built_in_sort_examples())
