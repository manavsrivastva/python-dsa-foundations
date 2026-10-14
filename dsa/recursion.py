"""Recursive examples: base case plus recursive case."""
def factorial(n):
    """O(n) time and O(n) call-stack space."""
    if n < 0:
        raise ValueError("factorial is undefined for negative integers")
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def fibonacci(n):
    """Naive recursive Fibonacci: O(2^n) time, O(n) stack."""
    if n < 0:
        raise ValueError("n must be non-negative")
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_memoized(n, memo=None):
    """Memoized Fibonacci: O(n) time and O(n) space."""
    if n < 0:
        raise ValueError("n must be non-negative")
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memoized(n - 1, memo) + fibonacci_memoized(n - 2, memo)
    return memo[n]


def sum_digits(n):
    """O(d) time and O(d) stack for d decimal digits."""
    n = abs(n)
    if n < 10:
        return n
    return n % 10 + sum_digits(n // 10)


def recursion_examples():
    print("Factorial 5:", factorial(5))
    print("Fibonacci 8:", fibonacci(8))
    print("Fibonacci 30 memoized:", fibonacci_memoized(30))
    print("Sum digits 583:", sum_digits(583))
    print("Recursion fits self-similar problems, but deep calls can hit Python's recursion limit.")
