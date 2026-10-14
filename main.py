"""Run a tour of the DSA practice modules."""
from dsa.big_o import complexity_examples
from dsa.lists_arrays import array_examples
from dsa.strings import string_examples
from dsa.two_pointers import two_pointer_examples
from dsa.searching import search_examples
from dsa.sorting import sorting_examples
from dsa.hashing import hashing_examples
from dsa.stacks_queues import stack_queue_examples
from dsa.linked_list import linked_list_examples
from dsa.recursion import recursion_examples


def main():
    sections = [
        ("Big-O", complexity_examples),
        ("Lists and arrays", array_examples),
        ("Strings", string_examples),
        ("Two pointers", two_pointer_examples),
        ("Searching", search_examples),
        ("Sorting", sorting_examples),
        ("Hash maps and sets", hashing_examples),
        ("Stacks and queues", stack_queue_examples),
        ("Singly linked list", linked_list_examples),
        ("Recursion", recursion_examples),
    ]
    for title, run_examples in sections:
        print(f"\\n{'=' * 12} {title} {'=' * 12}")
        run_examples()


if __name__ == "__main__":
    main()
