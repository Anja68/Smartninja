# create a class bank account
# it has 2 fields: name and balance
# it has methods to withdraw and deposit and print statement

class bankaccount(object):
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def withdraw(self):
        userinput = f"Enter the amount " + int(input())
        self.balance -= userinput
        print(userinput)

    def deposit(self):
        userinput1 = f"Enter the amount " + int(input())
        self.balance += userinput1
        print(userinput1)


if __name__ == '__main__':
    meinaccount = bankaccount("Anja", 1000)
    print(meinaccount.name, meinaccount.balance)

    meinaccount.withdraw()
    print(meinaccount.balance)
