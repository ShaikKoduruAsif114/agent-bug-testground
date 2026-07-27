"""
Bank account module.
BUG #1: withdraw allows balance to go negative (no overdraft check)  
BUG #2: transfer does NOT check if sender has sufficient funds before transferring
BUG #3: interest calculation uses wrong base  compounds on original not current balance
"""


class BankAccount:
    def __init__(self, owner: str, initial_balance: float = 0.0):
        self.owner = owner
        self.balance = initial_balance
        self.transactions = []

    def deposit(self, amount: float) -> float:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount
        self.transactions.append(("deposit", amount))
        return self.balance

    def withdraw(self, amount: float) -> float:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        self.transactions.append(("withdrawal", amount))
        return self.balance

    def transfer(self, amount: float, recipient_account) -> float:
        if amount <= 0:
            raise ValueError("Transfer amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        recipient_account.balance += amount
        self.transactions.append(("transfer", amount))
        recipient_account.transactions.append(("transfer", amount))
        return self.balance

    def calculate_interest(self, interest_rate: float) -> float:
        interest = self.balance * interest_rate
        self.balance += interest
        self.transactions.append(("interest", interest))
        return self.balance

    def divide(self, divisor: float) -> float:
        if divisor == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return self.balance / divisor