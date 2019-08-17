class BankAccount:
    
    def __init__(self,int_rate=0.01,account_balance=0):   #we deleted "amount" from up here
        self.account_balance= account_balance
        self.int_rate = int_rate      # we also didnt do a self.amount here


    def deposit(self,amount):   # "amount" is only being passed up here because it used in this method.
        self.account_balance = self.account_balance + amount #no need to use "amount" in __init__ method
        return self                # the line above we did not need to use "self.amount" becausr that was 
                                   # never declared.

    def withdraw(self, amount):   #EVERYTHIN WORKING HERE!  
        if self.account_balance < amount:
            self.account_balance-=5
            print("Insufficient Funds: Charging a $5 fee")
        else:
            self.account_balance= self.account_balance - amount
        return self

    def display_user_balance(self):   #no need to add "account_balance" up here
        print("Balance", self.account_balance)
        return self

    def yield_interest(self):    
        if self.account_balance > 0:
           self.account_balance = self.account_balance + self.account_balance * self.int_rate  
        return self  # create a varriable here, ur adding something here,

Steve = BankAccount()

Steve.deposit(100).display_user_balance().withdraw(20).yield_interest().display_user_balance()
