# Q5 Model and verify preconditions, postconditions, and invariants for a bank account system using formal methods in py

class BankAccount:
    def __init__(self, initial_balance: float):
        assert isinstance(initial_balance, (int, float)), "Initial balance must be a number"
        assert initial_balance >= 0, "Initial balance must be non-negative"
        self.balance = initial_balance
        self._check_invariant()

    def _check_invariant(self):
        # Invariant: balance should always be non-negative
        assert self.balance >= 0, f"Invariant violated: balance is {self.balance}"

    def deposit(self, amount: float):
        # Precondition
        assert amount > 0, "Deposit amount must be positive"
        old_balance = self.balance

        # Operation
        self.balance += amount

        # Postcondition
        assert self.balance == old_balance + amount, "Postcondition failed: Incorrect deposit logic"
        self._check_invariant()

    def withdraw(self, amount: float):
        # Preconditions
        assert amount > 0, "Withdrawal amount must be positive"
        assert self.balance >= amount, "Insufficient balance"
        old_balance = self.balance

        # Operation
        self.balance -= amount

        # Postcondition
        assert self.balance == old_balance - amount, "Postcondition failed: Incorrect withdrawal logic"
        self._check_invariant()

    def get_balance(self) -> float:
        # Postcondition
        assert self.balance >= 0, "Postcondition failed: balance should be non-negative"
        self._check_invariant()
        return self.balance


# -------------------------------
# ✅ Sample Usage & Test Cases
# -------------------------------

if __name__ == "__main__":
    # Creating a bank account
    account = BankAccount(100)

    # Deposit test
    account.deposit(50)
    print("Balance after deposit:", account.get_balance())  # Expected: 150

    # Withdraw test
    account.withdraw(30)
    print("Balance after withdrawal:", account.get_balance())  # Expected: 120

    # Uncomment to test assertion failures
    # account.deposit(-10)      # Should raise: Deposit amount must be positive
    # account.withdraw(200)     # Should raise: Insufficient balance
    # account2 = BankAccount(-5) # Should raise: Initial balance must be non-negative