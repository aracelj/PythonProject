

class Bank_Account:
    account_no = 1
    def __init__(self, name, balance=0):       #objects
        self.name = name
        self.account_id = Bank_Account.account_no
        Bank_Account.account_no += 1                                                #bank account id assigning
        self.balance = balance
        self.transactions = []
        self.transactions.append(f"Account opening balance: {self.balance} SEK")    #display opening balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

        result = self.balance
        self.transactions.append(f"Deposited: {amount} SEK  New Balance: {self.balance} SEK")
        return result

    def withdraw(self, amount):
        if amount > self.balance:
            print("Not enough money to withdraw!")
            amount = 0
        elif amount <=0:
            print("Withdrawn amount should not be less than 0!")
            amount = 0
        else:
            self.balance -= amount
        self.transactions.append(f"Withdrawn: {amount} SEK  New Balance: {self.balance} SEK")
        result = self.balance
        return result

    def apply_interest(self, interest):
        interest_total = self.balance * interest
        self.balance += interest_total
        self.transactions.append(f"Interest: {interest_total} New Balance: {self.balance} SEK")
        return interest_total

    def pay_bill(self, bill):
        if self.balance > bill:
            result = True
            #return result
        else:
            result = False
            #return result
        self.transactions.append(f"Can pay the bill of {bill} SEK: {result}")
        return result


    def print_info(self):
        if self.name is not None:
            print(f"Bank Account ID: {self.account_id}")
            print(f"Bank Account Name: {self.name}")
            print(f"Bank Account Balance: {self.balance} SEK")
            print("Transactions:")
            for t in self.transactions:
                print(" *", t)

        print("========================================")

""" 
act1 = Bank_Account("Anna Smith", 2000)
act2 = Bank_Account("John Doe", 1000)

act1.deposit(500)
act1.withdraw(100)
act1.apply_interest(0.02)
act1.pay_bill(500)

accounts = [act1, act2]
for account in accounts:
    account.print_info()
    
"""


    









