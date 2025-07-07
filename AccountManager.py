import pickle

class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.transactions = []

    def __str__(self):
        return f"Account owner: {self.owner}, \nBalance: {self.balance}"

    def deposit(self, amount, reason=None):
        if amount > 0:
            self.balance += amount
            self.transactions.append({
                'type': 'deposit',
                'amount': amount,
                'reason': reason,
                'balance_after': self.balance
            })
            print(f"Deposited: {amount}, \n New Balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount, reason=None):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transactions.append({
                'type': 'withdraw',
                'amount': amount,
                'reason': reason,
                'balance_after': self.balance
            })
            print(f"Withdrew: {amount}, New Balance: {self.balance}")
        else:
            print("Insufficient Funds.")
    
    def history(self):
        if not self.transactions:
            print("No transactions found.")
            return
        print("Transaction History:")
        for tx in self.transactions:
            print(
                f"{tx['type'].capitalize()} of {tx['amount']} "
                f"for reason: {tx['reason']} "
                f"(Balance after: {tx['balance_after']})"
            )

def save_accounts(accounts, filename="accounts.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(accounts, f)

def load_accounts(filename="accounts.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return {}

    