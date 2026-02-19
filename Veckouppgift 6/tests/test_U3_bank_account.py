
from U3_bank_account import Bank_Account

class TestBank_Account():
    act1 =  Bank_Account("Anna Smith", 2000)
    assert act1.deposit(500) == 2500
    assert act1.withdraw(100) == 2400
    assert act1.apply_interest(0.02) == 48
    assert act1.pay_bill(500) == True


    act2 =  Bank_Account("John Doe", 1000)
    assert act2.deposit(0) == 1000
    assert act2.withdraw(1500) == 1000
    assert act2.apply_interest(0.02) == 20
    assert act2.pay_bill(1500) == False
