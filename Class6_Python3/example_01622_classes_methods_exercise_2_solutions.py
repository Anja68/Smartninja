# coding=utf-8

# create a class bank account
# it has 2 fields: name and balance
# it has methods to withdraw and deposit and print statement

class BankAccount(object):
    def __init__(self, balance, name):
        self.balance = balance
        self.name = name

    def print_statement(self):
        print(str(self.name) + " === " + str(self.balance)+"€")

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount


myaccount = BankAccount(1000, "Gregor")

myaccount.print_statement()
myaccount.deposit(1000)
myaccount.print_statement()
myaccount.withdraw(3000)
myaccount.print_statement()
