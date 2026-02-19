"""
Using TDD: It will fail first as there is no class being created yet only the test cases
"""

from U3_bank_account_tdd import Bank_Account



def test_deposit():
        assert act1.deposit(500) == 2500
        assert act2.deposit(0) == 1000

def test_withdraw():
        assert act1.withdraw(100) == 2400
        assert act2.withdraw(1500) == 1000

def test_interest():
        assert act1.apply_interest(0.02) == 48
        assert act2.apply_interest(0) == 0

def test_pay_bill():
        assert act1.pay_bill(500) == True
        assert act2.pay_bill(1500) == False


act1 = Bank_Account("Anna Smith", 2000)
act2 = Bank_Account("John Doe", 1000)


