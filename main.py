from AccountManager import Account, save_accounts, load_accounts

def main():
        print("Welcome to the Bank Account Simulation!")

        accounts = load_accounts()

        name = input("Enter account owner name: ")
        if name.lower() == "quit":
            print("Exiting. Goodbye!")
            return

        if name in accounts:
            acc = accounts[name]
            print(f"Welcome back, {acc.owner}! Current balance: {acc.balance}")
        else:
            while True:
                balance_input = input("New account detected. Enter starting balance (or type 'quit' to exit): ").strip()
                if balance_input.lower() == "quit":
                    print("Exiting. Goodbye!")
                    return
                try:
                    balance = float(balance_input)
                    acc = Account(name, balance)
                    accounts[name] = acc
                    print(f"New account created for {name} with balance {balance}")
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")

        # main menu loop
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
                    return

                if name in accounts:
                    acc = accounts[name]
                    print(f"Switched to account of {acc.owner}. Current balance: {acc.balance}")
                else:
                    while True:
                        balance_input = input("New account detected. Enter starting balance (or type 'quit' to exit): ").strip()
                        if balance_input.lower() == "quit":
                            print("Exiting. Goodbye!")
                            return
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
                print("Unknown action. Please choose deposit, withdraw, history, balance, switch account, or quit.")

if __name__ == "__main__":
    main()
