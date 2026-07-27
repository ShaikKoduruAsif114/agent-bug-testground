"""
Calculator module - performs basic arithmetic operations.
BUG #1: Division does not handle ZeroDivisionError
BUG #2: Percentage calculation is wrong (divides by 10 instead of 100)
"""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    # BUG: No check for b == 0 → crashes with ZeroDivisionError
    return a / b


def percentage(value, percent):
    # BUG: Wrong formula → divides by 10 instead of 100
    return (value * percent) / 10


def power(base, exp):
    return base ** exp


def factorial(n):
    # BUG: Missing base case for n == 0 (should return 1)
    if n == 1:
        return 1
    return n * factorial(n - 1)
