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

if __name__ == "__main__":
    print("Welcome to the Bank Account Simulation!")

    accounts = load_accounts()

    name = input("Enter account owner name: ")
    if name.lower() == "quit":
        print("Exiting. Goodbye!")
        exit(0)

if name in accounts:
    acc = accounts[name]
    print(f"Welcome back, {acc.owner}! Current balance: {acc.balance}")
else:
    # Ask for starting balance for new account
    while True:
        balance_input = input("New account detected. Enter starting balance (or type 'quit' to exit): ").strip()
        if balance_input.lower() == "quit":
            print("Exiting. Goodbye!")
            exit(0)
        try:
            balance = float(balance_input)
            acc = Account(name, balance)
            accounts[name] = acc
            print(f"New account created for {name} with balance {balance}")
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# main menu
while True:
    action = input("deposit, withdraw, history, balance, switch account, quit: ").lower().strip()
    if action == "deposit":
        while True:
            amount_input = input("Amount to deposit (or type 'quit' to cancel): ").strip()
            if amount_input.lower() == "quit":
                print("Deposit cancelled.")
                break
            try:
                amount = float(amount_input)
                reason = input("Reason: ")
                acc.deposit(amount, reason)
                break
            except ValueError:
                print("Invalid amount. Please enter a number.")
    elif action == "withdraw":
        while True:
            amount_input = input("Amount to withdraw (or type 'quit' to cancel): ").strip()
            if amount_input.lower() == "quit":
                print("Withdrawal cancelled.")
                break
            try:
                amount = float(amount_input)
                reason = input("Reason: ")
                acc.withdraw(amount, reason)
                break
            except ValueError:
                print("Invalid amount. Please enter a number.")
    elif action == "balance":
        print(f"Current balance: {acc.balance}")
    elif action == "history":
        acc.history()
    elif action == "switch account":
        name = input("Enter account owner name to switch (or type 'quit' to exit): ")
        if name.lower() == "quit":
            print("Exiting. Goodbye!")
            exit(0)
        if name in accounts:
            acc = accounts[name]
            print(f"Switched to account of {acc.owner}. Current balance: {acc.balance}")
        else:
            while True:
                balance_input = input("New account detected. Enter starting balance (or type 'quit' to exit): ").strip()
                if balance_input.lower() == "quit":
                    print("Exiting. Goodbye!")
                    exit(0)
                try:
                    balance = float(balance_input)
                    acc = Account(name, balance)
                    accounts[name] = acc
                    print(f"New account created for {name} with balance {balance}")
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
    elif action == "quit":
        print("Saving accounts...")
        save_accounts(accounts)
        print("Goodbye.")
        break
    else:
        print("Unknown action. Please choose deposit, withdraw, history, or quit.")