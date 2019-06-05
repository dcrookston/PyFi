import datetime

class Account:
    def __init__(self, name):
        self.name = name
        ID = 0
        balance = 0

class Transaction:
    def __init__(self, account, amount, date):
        self.account = account
        self.amount = amount
        if date = 0:
            date = datetime.datetime.now()
        else:
            date = date
        self.account.balance += amount
