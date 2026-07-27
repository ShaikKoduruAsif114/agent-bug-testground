"""
String utilities module.
"""


def reverse_string(s: str) -> str:
    return s[::-1]


def is_palindrome(s: str) -> bool:
    return s.casefold() == reverse_string(s).casefold()


def count_words(text: str) -> int:
    return len(text.split())


def capitalize_words(text: str) -> str:
    return ' '.join(word.capitalize() for word in text.split())


def truncate(text: str, max_length: int) -> str:
    if len(text) <= max_length:
        return text
    return text[:max_length - 3] + '...'


def count_vowels(text: str) -> int:
    vowels = 'aeiou'
    return sum(1 for char in text.lower() if char in vowels)


def remove_duplicates(lst: list) -> list:
    seen = set()
    return [x for x in lst if not (x in seen or seen.add(x))]