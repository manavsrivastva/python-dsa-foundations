"""Hashing patterns with dict and set."""
from collections import defaultdict


def frequency_count(items):
    """Average O(n) time, O(k) space for k distinct items."""
    counts = {}
    for item in items:
        counts[item] = counts.get(item, 0) + 1
    return counts


def has_duplicates(items):
    """Average O(n) time, O(n) space."""
    seen = set()
    for item in items:
        if item in seen:
            return True
        seen.add(item)
    return False


def two_sum(numbers, target):
    """Return indices of two values summing to target; average O(n) time."""
    seen = {}
    for index, number in enumerate(numbers):
        needed = target - number
        if needed in seen:
            return seen[needed], index
        seen[number] = index
    return None


def group_anagrams(words):
    """Group by sorted lowercase letters."""
    groups = defaultdict(list)
    for word in words:
        groups[tuple(sorted(word.lower()))].append(word)
    return list(groups.values())


def hashing_examples():
    print("Frequencies:", frequency_count("mississippi"))
    print("Has duplicates:", has_duplicates([1, 2, 3, 2]))
    print("Two-sum indices:", two_sum([2, 7, 11, 15], 9))
    print("Anagrams:", group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
