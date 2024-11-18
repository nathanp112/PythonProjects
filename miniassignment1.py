class BankAccount:
    def __init__(self, owner: str, balance: float):
        if len(owner) < 10:
            raise ValueError("Owner name must contains at least 10 characters")
        if balance < 0:
            raise ValueError("Balance cannot be a negative value")
        self.owner = owner
        self.balance = balance
        self.transactions = []

    def __str__(self):
        return f"Owner: {self.owner}, Balance: ${self.balance}"

    def deposit(self, amount: float):
        if amount < 1:
            raise ValueError("Deposit amount must be greater than $1.00")
        self.balance += amount
        self.transactions.append(f"Deposited: ${amount}")

    def withdraw(self, amount: float):
        if amount > self.balance:
            print("Insufficient funds.")
        self.balance -= amount
        self.transactions.append(f"Withdrawn: ${amount}")

    def display_balance(self):
        print(f"Current Balance: {self.balance}")

    def display_transactions(self):
        for index, transaction in enumerate(self.transactions):
            print(f"{index}  {transaction}")
