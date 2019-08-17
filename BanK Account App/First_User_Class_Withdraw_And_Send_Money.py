

class User:
    def __init__(self, name, email_address,amount): #arguments
        self.name = name    #attribute
        self.email=email_address  #attribute
        self.account = BankAccount(int_rate=0.02, balance=0)
        
    
    def make_withdrawal(self, amount): # this is a method
        self.account_balance= self.account_balance-amount
        return self # the self is what makes the chaining work
    def make_deposit(self, amount): # this is a method
        self.account_balance= self.account_balance+amount
        return self
    
    def display_user_balance(self):     #i deleted "balance" from inside this parameter. THIS IS A METHOD
        print("User:", self.name, ", Balance:", self.account_balance)
        return self

    def transfer_money(self, other_user, amount):
        self.account_balance= self.account_balance-amount
        other_user.make_deposit(amount)
        return self


armando = User("Armando", "romeroarmando173@gmail.com", 500)
other_user = User("RandomName", "blah@gmail.com", 0)

armando.make_withdrawal(100).display_user_balance().transfer_money(other_user,100)
other_user.display_user_balance() 

# rafael=User()
# attribute is what can it HAVE
# method is ACTION
#Theres extra withdrawals and depostis I didnt do but should come back to it to make extra practice

        