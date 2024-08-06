import sys
class customer:
    '''BANK REGULAR ACTIVITIES'''
    bank = 'Indian Bank'
    def __init__(self, name, accountNo, balance = 0):
        self.name = name
        self.accountNo = accountNo
        self.balance = balance
    def deposit(self,amount):
        self.balance+= amount
        print('Avaliabe Balance: ',self.balance)
    def withdraw(self,amount):
        if self.balance < amount:
            print('Insufficient Balance')
        else:
            self.balance-= amount
            print('Avaliable Balance: ',self.balance)

    def myAccount(self):
        print('D-Deposit, W-Withdraw, S-Stop')
        choice = input('Enter your choice: ')
        if choice == 'D':
            amount = int(input('Enter the amount: '))
            customer1.deposit(amount)

            print('Do you want to continue')
            Option = input('Enter Y-Yes, N-No: ')
            if Option == 'Y':
                self.myAccount()
            elif Option == 'N':
                sys.exit()
        elif choice == 'W':
            amount = int(input('Enter the amount: '))
            customer1.withdraw(amount)

            print('Do you want to continue')
            Option = input('Enter Y-Yes, N-No: ')
            if Option == 'Y':
                self.myAccount()
            elif Option == 'N':
                sys.exit()
        elif choice == 'S':
            sys.exit()

print('Welcome to',customer.bank)
name = input('Enter your Name: ')
accountNo = int(input('Enter your accountNO: '))
customer1 = customer(name, accountNo)
customer1.myAccount()
