# tests/test_string_utils.py
import pytest
from src.string_utils import (
    reverse_string,
    is_palindrome,
    count_words,
    capitalize_words,
    truncate,
    count_vowels,
    remove_duplicates,
)

def test_reverse_string():
    """Test that reverse_string function works correctly."""
    input_str = "hello"
    expected_output = "olleh"
    assert reverse_string(input_str) == expected_output

def test_is_palindrome():
    """Test that is_palindrome function works correctly for different cases."""
    # Test with a palindrome string
    palindrome_str = "madam"
    assert is_palindrome(palindrome_str) == True

    # Test with a non-palindrome string
    non_palindrome_str = "hello"
    assert is_palindrome(non_palindrome_str) == False

    # Test with a mixed-case palindrome string
    mixed_case_palindrome_str = "MaDaM"
    assert is_palindrome(mixed_case_palindrome_str) == True

def test_count_words():
    """Test that count_words function works correctly."""
    input_str = "hello world this is a test"
    expected_output = 6
    assert count_words(input_str) == expected_output

def test_capitalize_words():
    """Test that capitalize_words function works correctly."""
    input_str = "hello world this is a test"
    expected_output = "Hello World This Is A Test"
    assert capitalize_words(input_str) == expected_output

def test_truncate():
    """Test that truncate function works correctly."""
    # Test with a string that is shorter than the max length
    input_str = "hello"
    max_length = 10
    expected_output = "hello"
    assert truncate(input_str, max_length) == expected_output

    # Test with a string that is longer than the max length
    input_str = "hello world this is a test"
    max_length = 10
    expected_output = "hello w..."
    assert truncate(input_str, max_length) == expected_output

def test_count_vowels():
    """Test that count_vowels function works correctly."""
    input_str = "hello world"
    expected_output = 3
    assert count_vowels(input_str) == expected_output

def test_remove_duplicates():
    """Test that remove_duplicates function works correctly."""
    input_list = [1, 2, 2, 3, 4, 4, 5, 6, 6]
    expected_output = [1, 2, 3, 4, 5, 6]
    assert remove_duplicates(input_list) == expected_output

def test_remove_duplicates_with_strings():
    """Test that remove_duplicates function works correctly with strings."""
    input_list = ["hello", "world", "hello", "world", "test"]
    expected_output = ["hello", "world", "test"]
    assert remove_duplicates(input_list) == expected_output