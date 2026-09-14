class BankAccount:
    bank_title = "Bank of Charlotte"
    def __init__(self, customer_name, customer_balance, minimum_balance):
        self.customer_name = customer_name
        self.customer_balance = customer_balance
        self.minimum_balance = minimum_balance

    #methods
    def deposit(self, deposit_amount):
        self.customer_balance += deposit_amount
        print(f"You deposited ${deposit_amount:.2f}")

    def withdraw(self, withdraw_amount):
        if self.customer_balance - withdraw_amount < self.minimum_balance:
            print("You don't have enough money to withdraw")
        else:
            self.customer_balance -= withdraw_amount
            print(f"You withdrew ${withdraw_amount:.2f}")

    def print_customer_info(self):
        print("Bank:", BankAccount.bank_title)
        print("Customer:", self.customer_name)
        print(f"Current Balance: ${self.customer_balance:.2f}")
        print(f"Minimum Balance: ${self.minimum_balance:.2f}")


#Tests
# First instance
account1 = BankAccount("Victor", 1000, 200)

account1.print_customer_info()
account1.deposit(300)
account1.withdraw(500)
account1.print_customer_info()

print()

# Second instance
account2 = BankAccount("John", 500, 100)

account2.print_customer_info()
account2.deposit(100)
account2.withdraw(550)
account2.print_customer_info()
