"""
String utilities module.
BUG #1: is_palindrome fails on mixed-case strings like 'Racecar'
BUG #2: count_words splits on single space only — fails on multiple spaces  
BUG #3: truncate adds '...' even when string is short enough (no length check)
"""


def reverse_string(s: str) -> str:
    return s[::-1]


def is_palindrome(s: str) -> bool:
    # BUG: Does NOT normalize case — 'Racecar' returns False instead of True
    return s == s[::-1]


def count_words(text: str) -> int:
    # BUG: split(' ') splits on single space only, "hello  world" → 3 words instead of 2
    return len(text.split(' '))


def capitalize_words(text: str) -> str:
    return ' '.join(word.capitalize() for word in text.split())


def truncate(text: str, max_length: int) -> str:
    # BUG: Always appends '...' even when text fits within max_length
    return text[:max_length] + '...'


def count_vowels(text: str) -> int:
    vowels = 'aeiou'
    return sum(1 for char in text.lower() if char in vowels)


def remove_duplicates(lst: list) -> list:
    # BUG: Doesn't preserve order — uses set which randomizes order
    return list(set(lst))
