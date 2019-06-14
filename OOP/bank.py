
# #Object Oriented Programming Challenge

# For this challenge, create a bank account class that has two attributes:

#     owner
#     balance

# and two methods:

#     deposit
#     withdraw

# As an added requirement, withdrawals may not exceed the available balance.

# Instantiate your class, make several deposits and withdrawals, 
# and test to make sure the account can't be overdrawn.

class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        print("Account Owner: {}".format(self.owner))
        print("Account Balance: ${}".format(self.balance))

    def deposit(self, deposit):
        self.balance += deposit
        print("You deposited ${}".format(deposit))
        print("DEPOSIT ACCEPTED!")
        print("Your Balance is: ${}".format(self.balance)) 

    def withdraw(self, withdraw):
        if withdraw > self.balance:
            print("Funds Unavailable")
            print("You have ${} available in your account.".format(self.balance))
        else:
            self.balance -= withdraw
            print("You withdrew ${}".format(withdraw))
            print("WITHDRAWEL ACCEPTED")
            print("Your Balance is: ${}".format(self.balance))


# 1. Instantiate the class
acct1 = Account('John',100)

# 2. Print the object
#print(acct1)

#Account owner:   Jose
#Account balance: $100

# 3. Show the account owner attribute
#print(acct1.owner)

# 4. Show the account balance attribute
#acct1.balance

# 5. Make a series of deposits and withdrawals
acct1.deposit(50)

#Deposit Accepted

acct1.withdraw(75)

#Withdrawal Accepted

# 6. Make a withdrawal that exceeds the available balance
acct1.withdraw(500)

#Funds Unavailable!

#Good job!¶
