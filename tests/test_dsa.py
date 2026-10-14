"""Regression tests using unittest."""
import unittest
from dsa.lists_arrays import reverse_copy
from dsa.strings import is_palindrome, reverse_string
from dsa.two_pointers import pair_sum_sorted, reverse_in_place
from dsa.searching import binary_search, linear_search
from dsa.sorting import bubble_sort, insertion_sort, selection_sort
from dsa.hashing import frequency_count, has_duplicates, two_sum, group_anagrams
from dsa.stacks_queues import Stack, Queue
from dsa.linked_list import SinglyLinkedList
from dsa.recursion import factorial, fibonacci, fibonacci_memoized, sum_digits


class TestDSA(unittest.TestCase):
    def test_lists_and_strings(self):
        self.assertEqual(reverse_copy([1, 2, 3]), [3, 2, 1])
        self.assertEqual(reverse_string("abc"), "cba")
        self.assertTrue(is_palindrome("Never odd or even"))
        self.assertFalse(is_palindrome("hello"))

    def test_two_pointers(self):
        self.assertEqual(pair_sum_sorted([1, 2, 4, 6, 8], 10), (2, 8))
        self.assertEqual(reverse_in_place([1, 2, 3]), [3, 2, 1])

    def test_searching(self):
        data = [1, 3, 5, 7]
        self.assertEqual(linear_search(data, 5), 2)
        self.assertEqual(binary_search(data, 7), 3)
        self.assertEqual(binary_search(data, 4), -1)

    def test_sorting(self):
        values, expected = [5, 1, 4, 2, 8], [1, 2, 4, 5, 8]
        self.assertEqual(bubble_sort(values), expected)
        self.assertEqual(selection_sort(values), expected)
        self.assertEqual(insertion_sort(values), expected)

    def test_hashing(self):
        self.assertEqual(frequency_count("aba"), {"a": 2, "b": 1})
        self.assertTrue(has_duplicates([1, 2, 1]))
        self.assertEqual(two_sum([2, 7, 11], 9), (0, 1))
        groups = group_anagrams(["eat", "tea", "bat"])
        self.assertEqual(sorted(sorted(group) for group in groups), [["bat"], ["eat", "tea"]])

    def test_stack_queue(self):
        stack = Stack()
        stack.push(1); stack.push(2)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.peek(), 1)
        queue = Queue()
        queue.enqueue(1); queue.enqueue(2)
        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(queue.peek(), 2)

    def test_linked_list(self):
        linked = SinglyLinkedList()
        self.assertEqual(linked.traverse(), [])
        linked.append(10); linked.append(20)
        self.assertEqual(linked.traverse(), [10, 20])
        self.assertTrue(linked.find(20))
        self.assertFalse(linked.find(99))

    def test_recursion(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(fibonacci(8), 21)
        self.assertEqual(fibonacci_memoized(30), 832040)
        self.assertEqual(sum_digits(583), 16)
        with self.assertRaises(ValueError):
            factorial(-1)


if __name__ == "__main__":
    unittest.main()
