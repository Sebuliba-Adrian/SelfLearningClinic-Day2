class BankAccount(object):
    def __init__(self,  accNumber,accName, initial_balance=0):
        self.accountNumber = accNumber
        self.accountName = accName
        self.balance = initial_balance
    def getAccountNumber(self):
        return self.accountNumber


    def getAccountName(self):
        return self.accountName
    def getBalance(self):
        return self.balance

    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
            return True

        else:
            return False





    def withdraw(self, amount):
        if amount > self.balance:
            return False
        else:
            self.balance -= amount
            return True

    def overdrawn(self):
        return self.balance < 0

