"""
Bank account module.
BUG #1: withdraw allows balance to go negative (no overdraft check)  
BUG #2: transfer does NOT check if sender has sufficient funds before transferring
BUG #3: interest calculation uses wrong base — compounds on original not current balance
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
        # BUG: No check for sufficient funds! Balance can go negative.
        self.balance -= amount
        self.transactions.append(("withdraw", amount))
        return self.balance

    def get_balance(self) -> float:
        return self.balance

    def transfer(self, target_account: "BankAccount", amount: float) -> bool:
        # BUG: Does NOT check self.balance >= amount before transferring
        self.balance -= amount
        target_account.balance += amount
        return True

    def apply_interest(self, rate: float, years: int) -> float:
        # BUG: Uses self.balance as original but should accumulate compound interest
        # Should be: balance * (1 + rate) ** years
        # Instead does: balance + (balance * rate * years) — simple interest, not compound
        original = self.balance
        self.balance = original + (original * rate * years)
        return self.balance

    def transaction_count(self) -> int:
        return len(self.transactions)
