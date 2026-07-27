"""
Calculator module - performs basic arithmetic operations.
"""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def percentage(value, percent):
    return (value * percent) / 100


def power(base, exp):
    return base ** exp


def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)