# Account class

class Account():
    def __init__(self, name, balance, password):
        self.name = name
        self.balance = int(balance)
        self.password = password

    def deposit(self, amountToDeposit, password):
        if password != self.password:
            print('Sorry, incorrect password\n')
            return None

        if amountToDeposit < 0:
            print('You cannot deposit a negative amount\n')
            return None

        self.balance = self.balance + amountToDeposit
        return self.balance

    def withdraw(self, amountToWithdraw, password):
        if password != self.password:
            print('Sorry, incorrect password for this account\n')
            return None

        if amountToWithdraw < 0:
            print('You cannot withdraw a negative amount\n')
            return None

        if amountToWithdraw > self.balance:
            print('You cannot withdraw more than you have in your account\n')
            return None

        self.balance = self.balance - amountToWithdraw
        return self.balance

    def getBalance(self, password):
        if password != self.password:
            print('Sorry, incorrect password for this account\n')
            return None
        return self.balance

    # Added for debugging
    def show(self):
        print(f'     Name: {self.name}')
        print(f'     Balance: {self.balance}')
        print(f'     Password: {self.password}\n')


# oAccount = Account('JP', 1000, 'magic')
# newBalance = oAccount.deposit(500, 'magic')
# print(newBalance)
# oAccount.withdraw(250, 'magic')
# current_balance = oAccount.getBalance('magic')
# print(current_balance)
