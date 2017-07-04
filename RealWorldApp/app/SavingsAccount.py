from BankAccount import BankAccount
class SavingsAccount(BankAccount):
    def __init__(self, accNumber,accName, initial_balance, rate):
        super(SavingsAccount, self).__init__(accNumber,accName, initial_balance)
        self.interestrate = rate

    def addInterest(self):
        interest =  BankAccount.getBalance(self) * self.interestrate / 100
        BankAccount.deposit(self,interest)
