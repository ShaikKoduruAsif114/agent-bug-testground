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
    account = BankAccount("John Doe", 0.0)
    new_balance = account.deposit(100.0)
    assert new_balance == 100.0
    assert account.balance == 100.0
    assert account.transactions == [("deposit", 100.0)]

def test_bank_account_withdraw():
    """Test BankAccount withdraw"""
    account = BankAccount("John Doe", 100.0)
    new_balance = account.withdraw(50.0)
    assert new_balance == 50.0
    assert account.balance == 50.0
    assert account.transactions == [("withdrawal", 50.0)]

def test_bank_account_transfer():
    """Test BankAccount transfer"""
    sender = BankAccount("John Doe", 100.0)
    recipient = BankAccount("Jane Doe", 0.0)
    sender.transfer(50.0, recipient)
    assert sender.balance == 50.0
    assert recipient.balance == 50.0
    assert sender.transactions == [("transfer", 50.0)]
    assert recipient.transactions == [("transfer", 50.0)]

def test_bank_account_insufficient_funds():
    """Test BankAccount insufficient funds"""
    account = BankAccount("John Doe", 100.0)
    with pytest.raises(ValueError):
        account.withdraw(150.0)

def test_bank_account_insufficient_funds_transfer():
    """Test BankAccount insufficient funds transfer"""
    sender = BankAccount("John Doe", 100.0)
    recipient = BankAccount("Jane Doe", 0.0)
    with pytest.raises(ValueError):
        sender.transfer(150.0, recipient)

def test_bank_account_negative_deposit():
    """Test BankAccount negative deposit"""
    account = BankAccount("John Doe", 0.0)
    with pytest.raises(ValueError):
        account.deposit(-100.0)

def test_bank_account_negative_withdrawal():
    """Test BankAccount negative withdrawal"""
    account = BankAccount("John Doe", 100.0)
    with pytest.raises(ValueError):
        account.withdraw(-50.0)

def test_bank_account_negative_transfer():
    """Test BankAccount negative transfer"""
    sender = BankAccount("John Doe", 100.0)
    recipient = BankAccount("Jane Doe", 0.0)
    with pytest.raises(ValueError):
        sender.transfer(-50.0, recipient)