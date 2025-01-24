SE 320 Software Construction - Module 1 Assignment
Infinite Sequence Generators
Overview

In this assignment, you’ll explore the power of infinite generators by creating generators for mathematical sequences, such as the Fibonacci sequence and prime numbers. You’ll practice lazy evaluation to handle sequences efficiently, even when they are infinite.
Learning Objectives

By completing this assignment, you will:

    Understand how to define and use infinite generators in Python.
    Explore real-world applications of lazy evaluation.
    Gain experience in handling infinite data streams.

Requirements

    Part 1: Fibonacci Generator
        Write a generator function fibonacci() that yields the Fibonacci sequence indefinitely.
        The sequence starts as 0, 1, 1, 2, 3, 5, 8, ....

    Additional Features:
    - Add an optional argument n to limit the number of terms returned (e.g., fibonacci(n=10) yields the first 10 Fibonacci numbers).

    Part 2: Custom Sequence
        Design your own infinite sequence generator!
        Examples:
            Square numbers (1, 4, 9, 16, ...).
            Geometric progression (1, 2, 4, 8, ...).
            Prime Numbers (2, 3, 5, 7, 11,...).
            Explain your choice and include comments to describe its logic.

    Additional Features:
    - Add an optional argument n to stop generating after reaching a given number of values.

Asserts

Part 1: Fibonacci Generator

assert list(fibonacci(10)) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
assert list(fibonacci(-1)) == []
assert list(fibonacci(0)) == []
assert list(fibonacci(1)) == [0]
assert list(fibonacci(2)) == [0, 1]

Part 2: Prime Generator

assert list(primes(10)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
assert list(primes(-1)) == []
assert(list(primes(0))) == []
assert(list(primes(1))) == [2]
assert(list(primes(2))) == [2, 3]

Deliverables

Code File
- Submit your Python file named infinite_generators.py