# tests/test_calculator.py
import pytest
from src.calculator import (
    add,
    subtract,
    multiply,
    divide,
    percentage,
    power,
    factorial,
)

def test_add():
    """Test the add function."""
    assert add(2, 3) == 5
    assert add(-2, 3) == 1
    assert add(-2, -3) == -5

def test_subtract():
    """Test the subtract function."""
    assert subtract(2, 3) == -1
    assert subtract(-2, 3) == -5
    assert subtract(-2, -3) == 1

def test_multiply():
    """Test the multiply function."""
    assert multiply(2, 3) == 6
    assert multiply(-2, 3) == -6
    assert multiply(-2, -3) == 6

def test_divide():
    """Test the divide function."""
    assert divide(6, 3) == 2
    assert divide(-6, 3) == -2
    assert divide(-6, -3) == 2
    with pytest.raises(ValueError):
        divide(6, 0)

def test_percentage():
    """Test the percentage function."""
    assert percentage(100, 25) == 25
    assert percentage(50, 50) == 25
    assert percentage(0, 100) == 0

def test_power():
    """Test the power function."""
    assert power(2, 3) == 8
    assert power(-2, 3) == -8
    assert power(2, 0) == 1

def test_factorial():
    """Test the factorial function."""
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(2) == 2
    assert factorial(3) == 6
    assert factorial(4) == 24
    with pytest.raises(RecursionError):
        factorial(1000)  # This will exceed the maximum recursion depth

def test_divide_by_zero():
    """Test that divide raises a ValueError when divisor is zero."""
    with pytest.raises(ValueError):
        divide(10, 0)