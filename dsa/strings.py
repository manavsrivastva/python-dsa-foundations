"""String manipulation; Python strings are immutable."""
def reverse_string(text):
    return text[::-1]  # O(n) time and result space


def is_palindrome(text):
    """Ignore spaces, punctuation, and case."""
    normalized = "".join(c.lower() for c in text if c.isalnum())
    return normalized == normalized[::-1]


def count_vowels(text):
    return sum(1 for c in text.lower() if c in "aeiou")


def first_word(text):
    parts = text.split()
    return parts[0] if parts else ""


def remove_spaces(text):
    return "".join(text.split())


def string_examples():
    print("Reverse:", reverse_string("python"))
    print("Palindrome:", is_palindrome("Never odd or even"))
    print("Vowel count:", count_vowels("Data Structures"))
    print("Remove spaces:", remove_spaces("data structures"))
