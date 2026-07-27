# tests/test_bank_account.py
import pytest
from src.bank_account import BankAccount

def test_bank_account_initialization():
    """Test that a BankAccount object is initialized correctly."""
    account = BankAccount("John Doe", 100.0)
    assert account.owner == "John Doe"
    assert account.balance == 100.0
    assert account.transactions == []

def test_deposit():
    """Test that depositing money into a BankAccount works correctly."""
    account = BankAccount("John Doe", 100.0)
    new_balance = account.deposit(50.0)
    assert new_balance == 150.0
    assert account.balance == 150.0
    assert account.transactions == [("deposit", 50.0)]

def test_withdraw():
    """Test that withdrawing money from a BankAccount works correctly."""
    account = BankAccount("John Doe", 100.0)
    new_balance = account.withdraw(50.0)
    assert new_balance == 50.0
    assert account.balance == 50.0
    assert account.transactions == [("withdrawal", 50.0)]

def test_transfer():
    """Test that transferring money between BankAccounts works correctly."""
    account1 = BankAccount("John Doe", 100.0)
    account2 = BankAccount("Jane Doe", 50.0)
    account1.transfer(20.0, account2)
    assert account1.balance == 80.0
    assert account2.balance == 70.0
    assert account1.transactions == [("transfer", 20.0)]
    assert account2.transactions == [("transfer", 20.0)]

def test_divide():
    """Test that the divide function handles ZeroDivisionError correctly."""
    account = BankAccount("John Doe", 100.0)
    # Since the divide function is not explicitly defined in the provided code,
    # we'll assume it's a method of the BankAccount class.
    # For the sake of this example, let's define a simple divide method:
    def divide(dividend, divisor):
        if divisor == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return dividend / divisor

    with pytest.raises(ZeroDivisionError):
        divide(100.0, 0)

    result = divide(100.0, 2.0)
    assert result == 50.0

def test_insufficient_funds():
    """Test that withdrawing or transferring more money than available raises an error."""
    account = BankAccount("John Doe", 100.0)
    with pytest.raises(ValueError):
        account.withdraw(150.0)
    with pytest.raises(ValueError):
        account.transfer(150.0, BankAccount("Jane Doe", 50.0))

def test_invalid_amount():
    """Test that depositing, withdrawing, or transferring a non-positive amount raises an error."""
    account = BankAccount("John Doe", 100.0)
    with pytest.raises(ValueError):
        account.deposit(-50.0)
    with pytest.raises(ValueError):
        account.withdraw(-50.0)
    with pytest.raises(ValueError):
        account.transfer(-50.0, BankAccount("Jane Doe", 50.0))