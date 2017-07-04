from BankAccount import BankAccount
class CurrentAccount(BankAccount):
    def __init__(self, accNumber,accName, initial_balance, rate):

        BankAccount.__init__(accNumber,accName, initial_balance)
        self.interestrate = rate
       # BankAccount.__init__(self, accNumber, accName, initial_balance=0)

    def withdraw(self, value):
        if value > 100000:
            print("got to bm")
        else:
            self.balance-=value
            print("you now have: ", self.balance)