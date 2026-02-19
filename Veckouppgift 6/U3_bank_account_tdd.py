

class Bank_Account:
    account_no = 1
    def __init__(self, name, balance):       #objects
        self.name = name
        self.account_id = Bank_Account.account_no
        Bank_Account.account_no += 1                                                #bank account id assigning
        self.balance = balance
        self.transactions = []
        self.transactions.append(f"Account opening balance: {self.balance} SEK")    #display opening balance

    def deposit(self, amount):                                                      #checks amount deposit
        if amount > 0:
            self.balance += amount

        deposit = self.balance
        self.transactions.append(f"Deposited: {amount} SEK  New Balance: {self.balance} SEK")
        return deposit

    def withdraw(self, amount):                                                     #checks amount withdrawn
        if amount > self.balance:
            print("Not enough money to withdraw!")
            amount = 0
        elif amount <=0:
            print("Withdrawn amount should not be less than 0!")
            amount = 0
        else:
            self.balance -= amount
        self.transactions.append(f"Withdrawn: {amount} SEK  New Balance: {self.balance} SEK")
        withdraw = self.balance
        return withdraw

    def apply_interest(self, interest):                                             #computes the interest rate
        interest_total = self.balance * interest
        self.balance += interest_total
        self.transactions.append(f"Interest: {interest_total} New Balance: {self.balance} SEK")
        return interest_total

    def pay_bill(self, bill):                                                       #checks if balance can pay the bill
        if self.balance > bill:
            result = True
            #return result
        else:
            result = False
            #return result
        self.transactions.append(f"Can pay the bill of {bill} SEK: {result}")
        return result


    def print_info(self):                                                           #prints bank account details
        if self.name is not None:
            print(f"Bank Account ID: {self.account_id}")
            print(f"Bank Account Name: {self.name}")
            print(f"Bank Account Balance: {self.balance} SEK")
            print("Transactions:")
            for t in self.transactions:
                print(" *", t)

        print("========================================")