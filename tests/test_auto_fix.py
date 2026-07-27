# tests/test_bank_account.py
import pytest
from src.bank_account import BankAccount

def test_bank_account_init():
    """Test BankAccount initialization"""
    account = BankAccount("John Doe", 100.0)
    assert account.owner == "John Doe"
    assert account.balance == 100.0
    assert account.transactions == []

def test_bank_account_deposit():
    """Test BankAccount deposit"""
    account = BankAccount("John Doe", 100.0)
    new_balance = account.deposit(50.0)
    assert new_balance == 150.0
    assert account.balance == 150.0
    assert account.transactions == [("deposit", 50.0)]

def test_bank_account_withdraw():
    """Test BankAccount withdrawal"""
    account = BankAccount("John Doe", 100.0)
    new_balance = account.withdraw(50.0)
    assert new_balance == 50.0
    assert account.balance == 50.0
    assert account.transactions == [("withdrawal", 50.0)]

def test_bank_account_withdraw_insufficient_funds():
    """Test BankAccount withdrawal with insufficient funds"""
    account = BankAccount("John Doe", 100.0)
    with pytest.raises(ValueError):
        account.withdraw(150.0)

def test_bank_account_transfer():
    """Test BankAccount transfer"""
    sender = BankAccount("John Doe", 100.0)
    recipient = BankAccount("Jane Doe", 50.0)
    new_balance = sender.transfer(50.0, recipient)
    assert new_balance == 50.0
    assert sender.balance == 50.0
    assert recipient.balance == 100.0
    assert sender.transactions == [("transfer", 50.0, "Jane Doe")]
    assert recipient.transactions == [("transfer", 50.0)]

def test_bank_account_transfer_insufficient_funds():
    """Test BankAccount transfer with insufficient funds"""
    sender = BankAccount("John Doe", 100.0)
    recipient = BankAccount("Jane Doe", 50.0)
    with pytest.raises(ValueError):
        sender.transfer(150.0, recipient)

def test_bank_account_divide():
    """Test BankAccount division (not implemented)"""
    account = BankAccount("John Doe", 100.0)
    with pytest.raises(AttributeError):
        account.divide(2)

def test_bank_account_divide_by_zero():
    """Test BankAccount division by zero (not implemented)"""
    account = BankAccount("John Doe", 100.0)
    with pytest.raises(AttributeError):
        account.divide(0)