class BankAccount: 
    # TODO: Add class and instance attributes at their appropriate places
    total_accounts = 0
    total_balance = 0

    
    def __init__(self, name: str, balance: int) -> None:
        self.name = name
        self.balance = balance
        BankAccount.total_balance += balance
        BankAccount.total_accounts += 1


# TODO: Create two accounts
# TODO: Print the information using the mentioned format

a = BankAccount("Alice", 1000)
b = BankAccount("Bob", 2000)

print(f"Alice's balance: ${a.balance}")
print(f"Bob's balance: ${b.balance}")
print(f"Total Accounts: {BankAccount.total_accounts}")
print(f"Total Balance: ${BankAccount.total_balance}")